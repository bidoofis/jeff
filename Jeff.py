import discord
import random
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

class Jeff(discord.Client):
    async def on_ready(self):
        print(f'{self.user} is pissing CORRECTLY!')

    async def on_message(self, message):
        #print(f'Message from {message.author}: {message.content}')

        if "You're welcome :)" in message.content:
            await message.reply("<:mahirobruh:1155998284876353617>") 

        # If the message is from the bot don't give a shit
        if message.author.bot: 
            return
        # 1/500 chance for chance
        chance1000 = 0.002

        # i'm getting CRAZY with this 1/5,000 chance!!
        chance10k = 0.0002

        # random.random() generates a number between 0 and 1.0 
        # 0.001 is just 1/1000, so that's the chance it rrepresents., therefore we check if the number is less than to get that chance.
        if random.random() < chance1000:
            await message.channel.send("The liberals would not approve of this.")

        # guess bro.
        if random.random() < chance10k:
            await message.channel.send("The liberals WOULD approve of this!")

        # Third verse same as the first
        chanceLvl = 0.002

        # Define categories, choose from list, store level up message, do!!!!!
        if random.random() < chanceLvl:
            category1 = random.choice(["Mustache Points", "Epicness", "Gamer Skill", "Ls recieved", "False Statements"])
            category2 = random.choice(["Hours of Anime Watched", "Backflips accomplished", "Toes collected","Tweets ratio'd", "BKZ twitter accounts reported", "Media Literacy Credits"])
            category3 = random.choice(["Embarassment points", "Persona slots gained", "Bogos binted", "is a number", "ignore the number, this is a cry for help"])
            randomNum1 = int(random.random() * 100 * (1 if random.random() < 0.8 else -1))
            randomNum2 = int(random.random() * 100 * (1 if random.random() < 0.8 else -1))
            randomNum3 = int(random.random() * 100 * (1 if random.random() < 0.8 else -1))

            levelupmsg = 'You leveled up!\n {:+} {}\n{:+} {}\n{:+} {}'.format(randomNum1, category1, randomNum2, category2, randomNum3, category3)

            await message.reply(levelupmsg)        
               
        # If you send 'pee pee' you are gross!!! EWWWWWW!!!!
        if "pee pee" in message.content:
            await message.channel.send("Gross! GRODY!!! ERM, DO YOU HAVE COOTIES OR SMTH?? idk i'm making this up")
            return
        
        if "mahirobot, what are you" in message.content.lower():
            await message.channel.send("I'm glad you asked!\nMahiroBot is a discord bot. Hope this helps!")
            return

        if "false" in message.content.lower():
            async with message.channel.typing():
                await asyncio.sleep(9)
                await message.channel.send("Hey, just noticed that you said something was false! Sadly, I have to inform you that the thing in question that you said was false was actually true. Please reflect on your actions, and come back with better facts.")
                return

        if "halloween" in message.content.lower():
            await message.channel.send("https://cdn.discordapp.com/attachments/1153004175077150752/1158063483007533067/rawr.png?ex=651ae22a&is=651990aa&hm=ad45827a791597d1366d07ed8a4f6d4320d94f1829f1566db1dcddf4c5416df4&")
            return

        if "banana" in message.content.lower():
            await message.channel.send("<:yooo:1153062892099358861>🍌")
            return

        if "chicken nug" in message.content.lower():
            await message.channel.send("<a:ChickenNugEat:1153192868136103966> <a:MahiroEat:1153195991399411732>")
            return

        # Do not kys ;(
        if "kys" in message.content:
            await message.reply("Not very poggers of you. MODERATOR!!!!! BAN THIS MAN PLEASE!")
            return

        if "proof" in message.content.lower():
            await message.reply("It's in the pudding.")
            return
        
        if "danbo" in message.content.lower():
            await message.channel.send("https://media.discordapp.net/attachments/678770209527693322/1349571889663840307/danbo2.gif?ex=67ebfa04&is=67eaa884&hm=b69ff7a9de48a50784e3ecf4ab549b4f06103e4af9b18f50407a80c487ad717c&=&width=1096&height=1402")
            return

    # This shit not bussin' bussin' on god fr
    #async def on_reaction_add(reaction, user, member):
     #   print(str(reaction.emojis))
      #  if "⭐" in reaction.emojis:
       #     print("john2")
        #    reaction.message.add_reaction("◀️")

intents = discord.Intents.default()
intents.message_content = True

client = Jeff(intents=intents)

client.run(os.getenv('DISCORD_TOKEN'))