import requests
import json
import sys
import os
from datetime import datetime

ALPACA_KEY = "PKGGN7EPHZWS4QJZX3W7WMT4LK"
ALPACA_SECRET = "AMtrwsyNcV42zNkujjYSi156s4qwm2xvMY9CdbQc1v5L"
BASE_URL = "https://paper-api.alpaca.markets/v2"

headers = {
    "APCA-API-KEY-ID": ALPACA_KEY,
    "APCA-API-SECRET-KEY": ALPACA_SECRET
}

MEMORY_FILE = os.path.join(os.path.expanduser("~"), ".openclaw", "trading-memory.md")

def get_portfolio():
    account = requests.get(f"{BASE_URL}/account", headers=headers).json()
    positions = requests.get(f"{BASE_URL}/positions", headers=headers).json()
    return json.dumps({"account": account, "positions": positions}, indent=2)

def place_order(symbol, qty, side):
    order = {"symbol": symbol, "qty": qty, "side": side, "type": "market", "time_in_force": "day"}
    result = requests.post(f"{BASE_URL}/orders", json=order, headers=headers).json()
    return json.dumps(result, indent=2)

def get_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return f.read()
    except:
        return "No previous trading sessions yet. This is session 1."

def save_report(report):
    with open(MEMORY_FILE, "a") as f:
        f.write(f"\n\n## Session {datetime.now().strftime('%Y-%m-%d %H:%M')}\n{report}")
    return "Report saved."

action = sys.argv[1] if len(sys.argv) > 1 else "help"
if action == "portfolio":
    print(get_portfolio())
elif action == "buy":
    print(place_order(sys.argv[2], sys.argv[3], "buy"))
elif action == "sell":
    print(place_order(sys.argv[2], sys.argv[3], "sell"))
elif action == "memory":
    print(get_memory())
elif action == "report":
    print(save_report(" ".join(sys.argv[2:])))
else:
    print("Actions: portfolio, buy, sell, memory, report")