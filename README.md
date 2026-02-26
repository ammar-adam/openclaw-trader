# OpenClaw Autonomous Trader

An autonomous AI trading agent that develops its own trading strategy through experience and self-reflection.

## What it is
Built on OpenClaw + DeepSeek R1 + Alpaca paper trading. The agent executes trades, writes session reports, reads its own history before each session, and evolves its strategy over time with zero human input.

## Architecture
- **Brain**: DeepSeek R1 (reasoning model)
- **Memory**: Persistent session logs read before every trade
- **Execution**: Alpaca Paper Trading API
- **Interface**: Telegram bot
- **Framework**: OpenClaw agent runtime

## Day 1 Results
- **P&L**: +$709 (+0.71%) on $100,000
- **Trades**: 34 executed autonomously
- **Strategy evolution**: Blue chip diversification → semiconductor concentration → crypto momentum → leveraged ETFs, all in one day
- **Self-corrections**: Caught and fixed day order expiry bug across sessions without being told
- **Experiments**: Attempted options leverage, BTC ETF arbitrage, sector rotation, 3x leveraged ETFs

## How it works
1. Agent wakes up via Telegram message
2. Reads all past session reports from memory
3. Scans the market and researches opportunities
4. Makes trading decisions autonomously
5. Executes trades via Alpaca API
6. Writes a detailed session report back to memory
7. Repeat

## The goal
Not to build a profitable trading bot. To observe what kind of trader an AI becomes when given complete autonomy, real capital, and the ability to learn from its own history.
```
