import discord
import asyncio
# import platform # Not sure what I'm using this for.
import json
import sqlite3
import logging as log
from datetime import datetime

from discord.ext.commands import Bot
from discord.ext import commands

log.basicConfig(filename='gentleman/log/gentleman.log',level=log.INFO)

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
        log.info('Testing databases')

        #Check the status of POST database.
        try:
            c.execute("Select * from POSTS")

        except sqlite3.OperationalError as e:
            print('Could not connect to table. Make sure you have followed the README.md and create the tables.')
            raise e
    
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    ## Monitoring & Moderation
    async def on_message(self, message):
        # Will be used for language monitoring
        pass

    async def on_reaction_add(self, reaction, user):
        c = self.conn.cursor()
        post = (str(reaction.message.id),)

        c.execute("select * FROM POSTS where post_id=?", post)
        if c.fetchone() == None and reaction.count >= 1: # TODO: CREATE A MORE DYNAMIC OPTION (25% of server member count) 
            post = (post[0], str(reaction.message.content), datetime.now().strftime('%Y-%m-%d'))
            
            log.info('Inserting new post: {}'.format(post))
            c.execute('insert into POSTS values(?,?,?)', post)
            self.conn.commit()

            # TODO: POST TO FACEBOOK
        



if __name__ == '__main__':
    with open('gentleman/conf/credentials.json') as f:
        file_dict = json.load(f)

    token = file_dict['token']
    conn = sqlite3.connect('gentleman.db')

    bot = Gentleman(token, conn)
    bot.run()
