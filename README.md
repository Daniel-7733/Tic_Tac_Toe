# 🎮 Tic Tac Toe (Python)

A simple terminal-based Tic Tac Toe game written in Python.  
This project is a beginner-friendly implementation of the classic game, built to practice Python fundamentals and Git/GitHub workflows.  

## ✨ Features
- Two-player mode (play with a friend in the terminal)
- 3x3 grid display
- Input validation (no overwriting moves)
- Detects winner or draw
- Easy-to-read code for learning

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/tic_tac_toe.git
   ```
2. Navigate into the project folder:
   ```bash
   cd tic_tac_toe
   ```
3. Run the game:
   ```bash
   python main.py
   ```

## 📂 Project Structure
```
tic_tac_toe/
├─ core/
│  ├─ players.py        # HumanPlayer, RandomBot, SmartBot, base Player, EMPTY constant
│  └─ game.py           # Game class (board, winner checks, turn order)
├─ ui_cli/
│  └─ main.py           # Your current terminal game
├─ ui_pygame/
│  ├─ main.py           # New Pygame front-end 
│  └─ img/
│     └─ board.jpeg        
├─ README.md      # Project description
└─ requirements.txt
```

## 📖 Future Improvements
- Add single-player mode (AI opponent)
- GUI version with Tkinter or PyGame
- Online multiplayer option

## 🛠️ Technologies Used
- Python 3.x
- Git & GitHub for version control

---

👨‍💻 Created as a practice project to learn Python and GitHub.
