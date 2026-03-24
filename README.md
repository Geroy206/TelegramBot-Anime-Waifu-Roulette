# TelegramBot-Anime-Waifu-Roulette

A simple Telegram bot for picking your next waifu from a massive database of anime and games.

Status: MVP (Minimum Viable Product) reached. The core logic is functional, and the database is populated.

## 🚀 Features
- **Total Random:** Get a character from a random title.
- **Selective Random:** Pick a title and get a random character from it.
- **Huge-Small Database:** Includes titles from *Genshin Impact*, *Touhou*, *Zenless Zone Zero*, *Danganronpa*, *Azur Lane*, and more.
- **Debug CL interface:** Debug CLI, for implements and test new modes

## 🛠 Tech Stack
- **Language:** Python 3.x
- **Library:** `pyTelegramBotAPI` (telebot)
- **State Management:** `StateMemoryStorage`
- **Environment:** `python-dotenv` 

## ⚙️ Installation
1. Install dependencies:
   ```bash
   pip install pytelegrambotapi python-dotenv
2. Clone the repo.
3. Create a `.env` file and add your `BOT_TOKEN`.
4. Fill the `data.py` or keep it as is (already contains 100+ characters).
5. Launch `python main.py`.

## 🏗️ TODO
- **Change data.py to SQLite database or JSON database**
- **Add more modes. For example: Random selection by tags.**
- **Add automatic addition of characters and titles.**

---
*Note: This project is currently in a "frozen" state as I'm returning to my main development. Feel free to fork and play around!*
