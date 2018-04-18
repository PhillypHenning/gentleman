import discord
import asyncio
import platform
import json
import sqlite3

from discord.ext.commands import Bot
from discord.ext import commands

#client = Bot(description="I am a Gentleman droid, made for your service. Beep Boop", command_prefix="$", pm_help = False)

class Gentleman(commands.AutoShardedBot):

    def __init__(self, token, conn):
        super().__init__(command_prefix='$')
        self.token = token
        self.conn = conn
        self.check_database_status()

    def __exit__(self):
        self.conn.close()

    def run(self):
        super().run(self.token, reconnect=True)

    def check_database_status(self):
        c = conn.cursor()
        try:
            c.execute("Select * from POST")

        except sqlite3.OperationalError as e:
            print('Could not connect to table. Make sure you have followed the README.md and create the tables.\n')
            raise e

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    ## Monitoring & Moderation
    async def on_message(self, message):
        # Will be used for language monitoring
        print('{}\n\tType of: {}\n\tMessage value: {}'.format(message, type(message), message.content))

    async def on_reaction_add(self, reaction, user):
        # TODO: Add this reaction to a list of reactions. 
        # TODO: If the reaction is in the list, update the 'seen'
        # TODO: If value goes over threshhold number post to facebook
        # TODO: If post has already been posted don't do it twice.
        pass



if __name__ == '__main__':
    with open('gentleman/conf/credentials.json') as f:
        file_dict = json.load(f)

    token = file_dict['token']
    conn = sqlite3.connect('gentleman.db')

    bot = Gentleman(token, conn)
    #bot.run()
    print('success :)')