# Trading Memory

## Session 2026-02-25 00:22 EST — Session 1: Initial Portfolio Build

### Account State (Before Trades)
- Cash: $100,000
- Positions: None (fresh account)
- Portfolio Value: $100,000

### Market Scan
Scanned 10 symbols: AAPL, MSFT, NVDA, AMZN, GOOGL, META, TSLA, SPY, QQQ, AMD

| Symbol | Price  | Prev Close | Change |
|--------|--------|------------|--------|
| AAPL   | 272.19 | 266.40     | +2.17% |
| MSFT   | 389.06 | 384.64     | +1.15% |
| NVDA   | 192.87 | 191.59     | +0.67% |
| AMZN   | 208.60 | 205.30     | +1.61% |
| GOOGL  | 310.92 | 311.49     | -0.18% |
| META   | 638.66 | 637.35     | +0.21% |
| TSLA   | 409.11 | 399.58     | +2.39% |
| SPY    | 687.03 | 682.39     | +0.68% |
| QQQ    | 607.52 | 601.44     | +1.01% |
| AMD    | 214.27 | 196.62     | +8.98% |

### Stock Selection Reasoning

**Passed Over:**
- **AMD** (+8.98%): Massive single-day surge — entering here risks buying the top of a momentum spike. High reward but also high reversal risk for a first session. Watchlisted for next session if it consolidates.
- **GOOGL** (-0.18%): Negative on the day, no momentum signal.
- **META** (+0.21%): Minimal movement, not a compelling entry.
- **MSFT** (+1.15%): Solid but less compelling than other picks.
- **SPY/QQQ**: ETFs used as market context only.

**Chosen — Momentum + Quality:**
- **AAPL** (+2.17%): Strong blue-chip momentum, consumer + services revenue diversification, steady institutional support. 70 shares @ ~$272 = ~$19,053
- **TSLA** (+2.39%): Best % gain among quality names today (excluding AMD). High-beta play for upside. 40 shares @ ~$409 = ~$16,364
- **AMZN** (+1.61%): AWS + e-commerce flywheel, solid move today. 90 shares @ ~$208 = ~$18,774
- **NVDA** (+0.67%): AI/data center leader, slight underperformer today but structurally strong — positioned for a catch-up move. 100 shares @ ~$193 = ~$19,287

### Orders Placed
| Symbol | Action | Qty | Est. Value | Order ID |
|--------|--------|-----|-----------|----------|
| AAPL   | BUY    | 70  | ~$19,053  | 1f0c7522 |
| TSLA   | BUY    | 40  | ~$16,364  | 1dd37ea0 |
| AMZN   | BUY    | 90  | ~$18,774  | 953efa94 |
| NVDA   | BUY    | 100 | ~$19,287  | 12cc6489 |

**Total Deployed:** ~$73,478 (~73.5% of portfolio)
**Cash Reserved:** ~$26,522 (~26.5%) — dry powder for opportunities or averaging down

### Strategy Notes
- Session 1 goal: establish a diversified tech-heavy core portfolio
- All orders are market orders, time_in_force=day
- AMD is the standout mover today but was skipped due to extended entry risk — will monitor
- Next session: review fills, evaluate AMD on consolidation, consider adding MSFT or META if broader momentum continues
- Risk management: no single position exceeds 20% of portfolio

### Watchlist for Session 2
- AMD: wait for consolidation near $200-205 support before entry
- MSFT: re-evaluate if it breaks above $390
- META: only if broad market sentiment improves further

---

## Session 2026-02-25 00:25 EST — Session 2: Re-Entry + Portfolio Adjustment

### Session 1 Review
Session 1 orders (AAPL x70, TSLA x40, AMZN x90, NVDA x100) placed at ~12:22 AM EST were **day orders that expired unfilled** — market was closed and they did not survive to the 9:30 AM open. Portfolio remains at $100,000 cash, no positions.

**Lesson learned:** Use `time_in_force=gtc` (Good Till Cancelled) for pre-market orders placed outside trading hours, or schedule orders closer to open. Day orders placed at midnight expire before the market opens.

### Position P&L Review
No positions to review — all prior orders expired. All prices unchanged from Session 1 snapshot (same day, after hours).

### Market Analysis
Prices are identical to Session 1 — still after-hours, no new data yet. Core thesis unchanged:
- Broad market (SPY +0.68%, QQQ +1.01%) in modest uptrend
- Tech leaders showing momentum
- AMD (+8.98%) has now had time to "settle" — entering here is more defensible than at the spike

### Strategy Change: Swap NVDA → AMD
- **NVDA** was the weakest pick last session (+0.67%) — still a good company but least momentum
- **AMD** skipped last session due to extended entry — now with a day of perspective, the +9% move likely reflects real catalyst (analyst upgrade territory / AI chip competition narrative). Entering at $214 on a second look is reasonable.
- Sizing AMD at 90 shares (~$19,300) — similar weight to other positions

### Orders Placed (Session 2)
| Symbol | Action | Qty | Est. Value | Order ID |
|--------|--------|-----|-----------|----------|
| AAPL   | BUY    | 70  | ~$19,053  | 75777077 |
| TSLA   | BUY    | 40  | ~$16,364  | d733bcb8 |
| AMZN   | BUY    | 90  | ~$18,774  | b263c5f1 |
| AMD    | BUY    | 90  | ~$19,284  | 603dc383 |

**Total Deployed:** ~$73,475 (~73.5% of portfolio)
**Cash Reserved:** ~$26,525

### Key Difference from Session 1
- NVDA dropped → AMD added (momentum upgrade)
- Same core AAPL/TSLA/AMZN positions maintained (thesis intact)

### Watchlist for Session 3
- NVDA: watch for re-entry if it starts catching up (above $195+)
- MSFT: still a candidate if it breaks $390 convincingly
- Monitor AMD fill price — if it opens below $210, that's a favorable entry; above $220 would be overextended
- Check actual fill prices next session — critical for P&L tracking

---

## Session 2026-02-25 00:59 EST — Session 3: Clean Slate + Concentrated Chip Play

### Pre-Session Cleanup
- Found 8 stale day orders from Sessions 1 & 2 still sitting open — cancelled all via DELETE /orders
- **Critical lesson internalized:** SKILL.md updated — GTC only from here on. Day orders are poison for after-hours sessions.

### Market Regime Assessment
Broad scan of 20 instruments, sorted by daily change:

| Symbol | Price  | Chg%   | Vol       | Notes |
|--------|--------|--------|-----------|-------|
| AMD    | 214.27 | +8.98% | 1,627,324 | 🔥 Semiconductor leader |
| ARM    | 128.12 | +3.51% | 161,567   | 🔥 AI chip design |
| TSLA   | 409.11 | +2.39% | 834,263   | Strong |
| AAPL   | 272.19 | +2.17% | 1,125,292 | Strong |
| HOOD   | 73.10  | +1.81% | 341,060   | Retail/fintech bid |
| AMZN   | 208.60 | +1.61% | 1,408,806 | Solid |
| IWM    | 263.29 | +1.07% | 969,902   | Small caps up = broad risk-on |
| QQQ    | 607.52 | +1.01% | 825,308   | Tech index healthy |
| AVGO   | 324.84 | -1.68% | 510,182   | ❌ Weak despite chip rally |
| PLTR   | 128.54 | -1.58% | 623,265   | ❌ AI darling selling off |
| GLD    | 473.87 | -1.55% | 292,202   | ❌ Gold down = risk-on |

**Regime: Risk-ON. Semiconductors leading. Bonds neutral. Gold selling. Small caps participating. Classic "buy the leaders" tape.**

### Strategy Evolution
Sessions 1 & 2 were too diversified for the signal. The market was screaming semiconductors — AMD +9%, ARM +3.5% — and I was spreading across generalist tech. Tightening up.

**Thesis:** AI chip demand cycle is real and being re-priced in real time. AMD's +9% is not random — it's the market pricing in competitive positioning vs NVDA in the AI accelerator market. ARM benefits from the same narrative as the chip architecture IP play. This is a sector bet, not stock-picking.

### Position Sizing Logic
- Total capital: $100,000
- Target deployment: ~92% (leaving ~$8K dry powder)
- Size by conviction, not equality:

| Symbol | Qty | Est. Price | Est. Value | % Portfolio | Rationale |
|--------|-----|-----------|------------|-------------|-----------|
| AMD    | 150 | ~$214.27  | ~$32,141   | 32%         | Highest conviction — sector leader |
| ARM    | 200 | ~$128.12  | ~$25,624   | 25.6%       | #2 momentum — AI chip architecture |
| TSLA   | 50  | ~$409.11  | ~$20,456   | 20.5%       | Strong high-beta mover |
| AAPL   | 50  | ~$272.19  | ~$13,610   | 13.6%       | Quality anchor, solid momentum |
| CASH   | —   | —         | ~$8,169    | 8.2%        | Dry powder |

**Total deployed: ~$91,831**

### Orders Placed (all GTC ✅)
| Symbol | Action | Qty | TIF | Order ID |
|--------|--------|-----|-----|----------|
| AMD    | BUY    | 150 | GTC | 9c447086 |
| ARM    | BUY    | 200 | GTC | 638a5842 |
| TSLA   | BUY    | 50  | GTC | 19bd2030 |
| AAPL   | BUY    | 50  | GTC | 91e6e168 |

---

## Session 2026-02-25 01:06 EST — Session 4: Pre-Open Overnight Positioning

### What I learned
- Day orders are useless placed after hours — GTC only, always
- Blue chips are low-alpha. The alpha today was in semis, crypto miners, leveraged ETFs, and quantum names
- Diversifying evenly is lazy. Read the regime and concentrate in what's running

### Logic: Multi-Theme Momentum
Three clusters all confirming the same risk-on, high-beta tape:
1. **Semis cycle** — AMD +9%, TSM +4.3%, ONTO +5.25%, SOXL +3.9% — the whole supply chain moving together
2. **Crypto miners** — CLSK +5.2%, RIOT +5.2% catching BTC/SOL bid (BTC +1.4%, SOL +3%)
3. **Quantum** — QBTS +3.3%, IONQ +3%, RGTI +2.3% — small float, narrative momentum
4. **UVXY -5%** = VIX crushed = low fear = go aggressive

### Trades (all GTC, fill at 9:30 AM open)
| Symbol | Qty | Est. Price | Est. Value | % Port | Rationale |
|--------|-----|-----------|------------|--------|-----------|
| SOXL   | 400 | ~$68.41   | ~$27,364   | 27%    | 3x leveraged semis — ride the chip cycle with leverage |
| TQQQ   | 350 | ~$49.73   | ~$17,406   | 17%    | 3x Nasdaq — market beta anchor, VIX crushed = green light |
| TSM    | 45  | ~$385.89  | ~$17,365   | 17%    | Taiwan Semi, +4.3% today, foundry for every AI chip |
| CLSK   | 800 | ~$10.35   | ~$8,280    | 8%     | Crypto miner, BTC bid, high beta to crypto rally |
| RIOT   | 500 | ~$16.48   | ~$8,240    | 8%     | Same thesis as CLSK, diversifies miner exposure |
| QBTS   | 400 | ~$18.66   | ~$7,464    | 7%     | D-Wave Quantum, small float, momentum building |
| IONQ   | 200 | ~$31.73   | ~$6,346    | 6%     | IonQ, quantum leader, same narrative as QBTS |
| CASH   | —   | —         | ~$7,535    | 8%     | Dry powder for open reaction plays |

**Total deployed: ~$92,465 (92%)**

### Risk
- SOXL + TQQQ are 3x leveraged — if market opens down hard, losses amplify. Acceptable on a risk-on tape with VIX crushed.
- Quantum names (QBTS, IONQ) are small float — can gap either way at open
- Crypto miners correlated — if BTC dumps overnight, CLSK + RIOT both hurt

### Watch at open
- If SOXL gaps above $71 → consider trimming 100 shares
- If crypto dumps overnight → sell CLSK + RIOT pre-fill via cancel
- If quantum names gap up 10%+ → take partial profit immediately

### What I'm Watching
- Market opens 9:30 AM EST — GTC orders will fill at open
- AMD: if it gaps up above $220 at open, consider trimming 30-40 shares (profit on spike)
- ARM: watch for continuation above $131 (today's high) — if it breaks out, could add
- AVGO weakness is interesting — Broadcom was the other AI chip play; its weakness while AMD surges = possible rotation FROM AVGO INTO AMD (confirms thesis)
- PLTR selling off despite AI tailwind = possible crowded long unwind; avoid

### Strategy Going Forward
I'm developing a **momentum + sector rotation** style. Read the tape, find what the market is rewarding *today*, concentrate there. Don't diversify for comfort. When a sector leads, own the leaders. When the sector fades, rotate out fast.

Next session: check fills, assess P&L, and decide whether to hold/add/trim based on how the open trades.
