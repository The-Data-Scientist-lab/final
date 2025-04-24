# Telegram Model Assistant Bot

A beautiful and interactive Telegram bot for model content delivery.

## Features

- 🌟 Beautiful welcome message with user's name
- 👩‍💼 Three model options with detailed information
- 💰 Two pricing plans (30 minutes and 1 hour)
- 📸 Payment verification system
- 🎨 Attractive UI with emojis and formatting

## Setup

1. Install Python 3.13
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root and add your Telegram bot token:
   ```
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   ```
4. Run the bot:
   ```bash
   python bot.py
   ```

## Usage

1. Start the bot by sending `/start` command
2. Choose from three available models
3. Select your preferred duration (30 minutes or 1 hour)
4. Complete the payment
5. Send the payment screenshot for verification

## Note

Make sure to replace the model images in the `images` directory with your actual model photos. 