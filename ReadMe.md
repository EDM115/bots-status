# BotStatus
Updates your bot status in the message, every hour
  
[![⚡️ Bot status update ⚡️](https://github.com/EDM115/bots-status/actions/workflows/updater.yml/badge.svg?branch=master)](https://github.com/EDM115/bots-status/actions/workflows/updater.yml)  
  
**_NOTE:_** This branch uses github workflows to host your code, and doesn't rely on another hosting platform. If you want to deploy on heroku/vps/whereever, go to [this branch](https://github.com/xditya/BotStatus/tree/deploy).

# Secrets.

Add them to [Settings ⇢ Secrets ⇢ New Repository Secret.](https://docs.github.com/en/actions/reference/encrypted-secrets)

- `APP_ID` and `API_HASH` from [my.telegram.org](https://my.telegram.org).
- `BOTS` - TG UserName of your bots separated by space.
- `SESSION` - Telethon SessionString of the User to edit the message.
- `REPO_NAME` - yourGitHubUserName/RepositoryName, eg: xditya/BotStatus (fork this repo first).
- `CHANNEL_ID` - ID of your channel.
- `MESSAGE_ID` - ID of the message to edit.

# Credits
- [Jainam Oswal](https://github.com/jainamoswal/BotStatus).
- [Me](https://xditya.me)
