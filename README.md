# Mango
> Python 3.6+ | discordpy v1.5.1

## Prelude / Purpose
I use this bot as message broker essentially. I store messages inside a MongoDB instance and this bot fetches them hourly and informs me about new mails ever since the last refresh.

Purges the Database afterwards.

## Setup / Requirements
**This guide assumes you have Python 3.6+ installed.**
Setup a virtual environment in the bot's root directory, activate the venv and run `pip install -r req.txt` to install all needed requirements.

Afterwards you should be good to go, make sure you got your own token set inside the `bot.env` and you can run it.

I recommend using PM2 to launch and keep it alive. Here's how you can if you have PM2 installed and you're in the root directory of the bot with a venv:
`pm2 start ./bot.py --interpreter ./your_venv/bin/python`


## License
This project is licensed as **MIT**. I don't care what you do lmao, feel free to build on it.

