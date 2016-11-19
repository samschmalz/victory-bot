# victory-bot
A bot user for the Discord Chat application

This is a single-file script for now, but it may be expanded in the future if I look into the Discord API a bit more.  For now, it offers some basic functionality in how it operates.

Current features:
* Replies to messages starting with correct commands
* Sends messages starting with !victory to a victory channel
* Sends a message to another user when the !highfive @user command is issued

To implement:
* given a group of users, will randomly assign a different user to each user (useful for secret santa or other events).
* message a list of commands when a help command is issued
* store victories in a database to be retrieved later

I have removed the last line, which has the OAuth2 key in it. This is for security reasons so that there aren't multiple instances of the bot trying to log in at the same time.
