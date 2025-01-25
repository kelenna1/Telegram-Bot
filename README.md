
# Telegram Daily Quote Bot

This project is a Telegram bot that sends daily motivational quotes to subscribers at a specified time. Users can subscribe to receive the quotes and unsubscribe at any time. The bot is built with Python, using the `python-telegram-bot` library and is hosted on Render.

---

## Features

- **Daily Quotes**: Subscribers receive a random motivational quote daily at 7:00 AM.
- **Subscribe/Unsubscribe**: Users can subscribe using the `/start` command and unsubscribe with the `/stop` command.
- **Persistent Storage**: Subscriber data is stored in an SQLite database to ensure persistence.

---

## Requirements

- Python 3.9+
- Telegram Bot Token (from BotFather)
- Required Python libraries (see `requirements.txt`):
  - `python-telegram-bot`
  - `apscheduler`
  - `python-dotenv`

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/username/telegram-daily-quote-bot.git
   cd telegram-daily-quote-bot
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file and add your Telegram Bot Token:
   ```
   BOT_TOKEN=your-telegram-bot-token
   ```

5. Run the bot:
   ```bash
   python kelenna.py
   ```

---

## Deployment

This bot is deployed using Render. Follow these steps to deploy:

1. Push your code to a GitHub repository.

2. Log in to [Render](https://render.com/) and create a new **Web Service**.

3. Connect the repository and configure the build and start commands:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `bash start.sh`

4. Add your environment variables (e.g., `BOT_TOKEN`) in Render's dashboard.

5. Deploy the service.

---

## Commands

- `/start`: Subscribes the user to daily quotes.
- `/stop`: Unsubscribes the user from daily quotes.

---

## File Structure

- `kelenna.py`: Main bot script.
- `requirements.txt`: List of dependencies.
- `start.sh`: Script to start the bot.
- `.env`: Environment variables (not included in the repository for security).

---

## Quotes

The bot includes a pre-defined list of motivational quotes. You can edit the `quotes` list in the script to customize the messages.

---

## Future Improvements

- Add user-specific customization for delivery times.
- Introduce more advanced quote categories.
- Add analytics to track active subscribers.
- Implement a web interface for managing quotes and subscribers.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See `LICENSE` for more details.

---

## Author

**Okolie Emmanuel**  
For any questions, feel free to reach out on [Telegram](https://t.me/yourusername).

---

Happy Coding! 🚀

