# 🕰️ Development History

## ✨ Initial Spark
The idea came from a conversation about mixing chess with roguelike elements—we wanted something turn-based, tactical, and familiar but with a progression twist. The concept "what if chess pieces could evolve and gain skills" immediately clicked.

We decided to make it fast-paced and **focus on game mechanics first**, postponing decisions about story, art style, or world-building. The goal was to validate the tactical fun of chess-movement in a roguelike system.

---

## 🌟 Setup & First Prototype
We chose **Python** because the user wanted to learn it, and it's great for quick prototyping in the terminal.

- Created a Git repo and basic structure with `main.py`
- Displayed a simple 8x8 board using ASCII and 2D lists
- Added Pawn and Knight as starting pieces with movement logic
- Created `algebraic_to_coords()` to allow user to input "A2" positions

---

## ⚔️ Movement & Combat
We refined movement by building `get_possible_moves()` functions per piece.

- Added logic for forward Pawn movement + diagonal attacks
- Knight L-shaped movement + enemy capture

Combat started as simple overwriting, then upgraded to basic feedback:

- Captures printed a message to the console
- Game now checks for enemy presence and only allows valid captures

---

## ⚡ Enemy AI
Initially only one enemy moved per turn.

- Added basic AI: move toward nearest player, capture if adjacent
- Display simple messages for AI turns

Later planned to expand to all enemies per turn.

---

## 🔁 Flow Improvements
To avoid tedious input (e.g. typing "D4"), we added the idea to let the player:

- Choose from a list of available pieces
- Only select pieces that haven't acted this round

This also led to the idea of **per-piece turn tracking**.

---

## 🏆 Concept Document
At this point, we paused and wrote a Game Concept One-Pager:

- Defined what we’re building
- Set boundaries for the PoC
- Logged future ideas for upgrades, events, and meta-progression

Also created a cover image to visualize the idea.

---

## 📊 Project Organization
We set up GitLab to:

- Store the project and docs
- Create simple issues with labels (no heavy Scrum/Kanban)
- Use `README.md`, `GAME_CONCEPT.md`, and this `HISTORY.md` to track ideas

---

## ✅ Current State
The project now has:

- A playable turn-based prototype
- Basic piece movement and combat
- A plan for next steps like win/lose conditions, upgrades, and HP

Next: improve flow, test combat depth, and experiment with procedural setups.