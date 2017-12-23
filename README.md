A bot user for the Discord Chat application

For now this is just a simple script, but I will likely expand it a bit further.  birbBot.py is the reworked version, victoryBot.py is the old version.

This script requires the use of discord.py as well as SQLite3 


Current functionality:
* add or remove points from users
* issue a "fuck you" to a user
* roll dice with advantage and disadvantage using /roll

To install requirements, use `pip install -r requirements.txt`

To do:
* re-implement victories as in victoryBot.py
* add more error checking


To prepare your system to run this:
1. Install virtualenv
2. CD into the directory you want to work in (preferably the cloned git repo)
3. run `virtualenv victoryBot -p python3`
4. activate the virtual environment with `source victoryBot/bin/activate`
5. Install required modules with `pip3 install -r requirements.txt`
6. Run python as necessary
7. To exit the virtualenv, use `deactivate`
