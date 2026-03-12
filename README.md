# Confession Bot

This is a Discord bot designed to handle user confessions. Users can submit their confessions, and the bot will manage the submission process, ensuring that each confession is handled appropriately.

## Features

- Users can send confessions through a designated command.
- Confessions are processed and sent to a specific channel.
- The bot automatically closes the confession after it is sent.

## Project Structure

```
confession-bot
├── src
│   ├── bot.py               # Entry point for the bot
│   ├── config.py            # Configuration and environment variable handling
│   ├── commands
│   │   └── confession.py     # Command for submitting confessions
│   ├── handlers
│   │   └── confession_handler.py # Logic for handling confessions
│   └── utils
│       └── helpers.py        # Utility functions
├── .env                      # Environment variables
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd confession-bot
   ```

2. Create a `.env` file in the root directory and add your Discord bot token:
   ```
   TOKEN=your_discord_bot_token
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the bot:
   ```
   python -m src.bot
   ```

## Deploy Notes

- This repo includes a `Procfile` for worker platforms.
- If your platform asks for commands, use:
  - Build Command: `pip install -r requirements.txt`
  - Start Command: `python -m src.bot`
- If the platform auto-detects `main.py`, this repo already provides it.

## Usage

- To submit a confession, use the command defined in `src/commands/confession.py`. The bot will process the confession and send it to the designated channel.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the bot!

# DPNPCNFS