# Telegram Quiz Bot

This project is a Telegram bot that sends video content and follows up with a quiz to test the user's knowledge about the video. The bot helps in educational purposes by offering an interactive learning experience.

## Features
- Sends video content to the user.
- After the video, the bot sends a multiple-choice quiz.
- Tracks the user's responses and progress.
- Uses Google Sheets for storing quiz data.

## Setup and Installation

### Prerequisites
- Python 3.x
- A Telegram bot token from BotFather
- Google Sheets API credentials

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up Google Sheets API credentials:
    - Follow [this guide](https://developers.google.com/sheets/api/quickstart/python) to enable Google Sheets API and get credentials.
    - Place the credentials file in the project directory and rename it `credentials.json`.

4. Set up your Telegram Bot:
    - Go to [BotFather](https://core.telegram.org/bots#botfather) on Telegram to create a bot and get the bot token.
    - Replace `YOUR_BOT_TOKEN` in the code with your actual bot token.

5. Run the bot:
    ```bash
    python bot.py
    ```

## Usage
- Start a conversation with your bot on Telegram.
- The bot will send a video, followed by a quiz with multiple-choice questions.
- Answer the questions to continue with the video series.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
