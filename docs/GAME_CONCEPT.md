# ✨ Chess Roguelike - Game Concept One-Pager

## 🌟 Core Idea
**"What if chess pieces could evolve, learn skills, and fight in dungeons?"**

A fast-paced, turn-based tactics game inspired by chess, where the player controls a small squad of evolving chess pieces through procedurally generated dungeon battles. Each piece retains its signature movement pattern but gains unique abilities and perks over time.

---

## ⚔️ Core Mechanics
- **8x8 Grid-Based Combat**: Pieces are placed on a chessboard-style grid.
- **Squad of Pieces**: Player starts with 2–3 controllable units (Pawn, Knight, etc.).
- **Chess-Like Movement**: Each unit moves according to their traditional chess rules.
- **Turn-Based Battles**: Player and enemy squads alternate turns.
- **Basic AI Enemies**: Enemies move towards and attack player units.
- **One-Hit Kills** (for now): Simplified combat for prototyping.
- **Piece Selection System**: Player selects pieces to move via indexed list rather than typing grid coordinates.
- **Per-Piece Turn Tracking**: Only unused pieces are available for action in a round.

---

## 📈 PoC Progress Overview

### ✅ Core PoC Progress  
> Tracking all features defined for the prototype phase.

**6 / 11 complete**  
```
[██████████████░░░░░░░░░░░░░░░░░░] 55%
```

| Feature                                      | Status        |
|----------------------------------------------|---------------|
| 8x8 grid rendering                           | ✅ Done        |
| Piece movement (Pawn, Knight)                | ✅ Done        |
| Basic capturing / combat                     | ✅ Done        |
| Enemy AI (move + attack)                     | ✅ Done        |
| Turn-based loop                              | ✅ Done        |
| Piece selection by index                     | ✅ Done        |
| Per-piece turn tracking                      | ⏳ In progress |
| Victory / defeat conditions                  | ⬛ Not yet     |
| HP system (non-instant kills)                | ⬛ Not yet     |
| Upgrades (e.g. promote Pawn)                 | ⬛ Not yet     |
| Turn counter / combat log                    | ⬛ Not yet     |

---

## 🔄 Progression Ideas (For Later)
These are noted but *not* part of the PoC:
- **Piece Upgrades**:
  - Pawn → promote to Knight/Bishop/etc.
  - Knight → double jump.
  - Rook → cleave attack.
- **Meta Progression**:
  - Unlock new piece types and passives.
  - Improve squad options between runs.
- **Randomized Events**:
  - Battle, elite, shop, shrine.
- **DnD-Inspired Combat**:
  - Skill-based exchanges instead of one-hit kills.

---

## 🎯 PoC Scope (Prototype Focus)
| Feature            | Included in PoC? | Notes                                |
|--------------------|------------------|--------------------------------------|
| 8x8 Grid           | Yes              | Terminal-based                       |
| Player Movement    | Yes              | Pawn and Knight movement logic       |
| Enemy AI           | Yes              | Basic movement + capture             |
| Turn System        | Yes              | Player and enemy take alternating turns |
| Combat             | Yes              | One-hit kills on capture             |
| Victory Condition  | WIP              | Win when all enemies are dead       |
| Upgrades           | No               | Planned for later                    |
| Events / Map       | No               | Out of scope for PoC                 |
| Piece Selection    | Yes              | Select piece by number rather than grid manually |
| Piece Turn Tracking| Yes              | Only unused pieces are selectable    |
| HP System          | No               | Might replace one-hit logic later    |
| Turn Counter       | No               | Optional display/log feature         |

---

## 🚀 Goal of the PoC
> Validate that chess-inspired movement + small-squad roguelike combat is **fun**, **tactical**, and **extendable**.

Once validated, expand into upgrades, evolving pieces, meta-unlocks, and deeper combat systems.

---

## 📚 Notes
- Visual style, tone, and full theme are *not yet decided*. Core mechanics take priority.
- Combat could eventually shift from one-hit captures to **health-based**, skill-driven exchanges.
- Focus is to stay minimal and not overwhelm during early development.

---

## 🕰️ Development History

*Moved to* [`docs/HISTORY.md`](docs/HISTORY.md)

---

## 💼 Cover Art
See attached image: *"Chess Roguelike - Game Concept Cover"*