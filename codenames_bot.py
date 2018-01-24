from PIL import Image, ImageDraw, ImageFont
import discord
import asyncio
import words
import random

# whos first (9 cards)
# blue = 0, red = 1
def whos_first():
    coin = random.randint(0, 1)
    return coin

def check(msg):
    return msg.content.endswith(('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'беск', 'inf'))

# generating words for game session
def generate_words():
    i = 0
    game_words = []
    rand_index_list = []
    while i != 25:
        rand_index = random.randint(0, len(words.Words)-1)
        while rand_index_list.count(rand_index) != 0:
            rand_index = random.randint(0, len(words.Words)-1)
        rand_index_list.append(rand_index)
        i = i + 1
    for number in rand_index_list:    
        game_words.append(words.Words[number])
    return game_words


# generating blue/red/neutral/killer cards
def generate_cards(coin):
    i = 0
    j = 0
    k = 0
    blue_words = []
    red_words = []
    neutral_words = []
    rand_index_list = []
    if coin == 0:
        while i != 9: # first
            rand_index = random.randint(0, 24)
            while blue_words.count(rand_index) != 0:
                rand_index = random.randint(0, 24)
            blue_words.append(rand_index)
            i = i + 1
        while j != 8: # second
            rand_index = random.randint(0, 24)
            while blue_words.count(rand_index) != 0 or red_words.count(rand_index) != 0:
                rand_index = random.randint(0, 24)
            red_words.append(rand_index)
            j = j + 1
        while k != 7: # neutral
            rand_index = random.randint(0, 24)
            while blue_words.count(rand_index) != 0 or red_words.count(rand_index) != 0 or neutral_words.count(rand_index) != 0:
                rand_index = random.randint(0, 24)
            neutral_words.append(rand_index)
            k = k + 1
        rand_index = random.randint(0, 24)
        while blue_words.count(rand_index) != 0 or red_words.count(rand_index) != 0 or neutral_words.count(rand_index) != 0:
            rand_index = random.randint(0, 24)
        killer = rand_index
    else:
        while i != 8: # first
            rand_index = random.randint(0, 24)
            while blue_words.count(rand_index) != 0:
                rand_index = random.randint(0, 24)
            blue_words.append(rand_index)
            i = i + 1
        while j != 9: # second
            rand_index = random.randint(0, 24)
            while blue_words.count(rand_index) != 0 or red_words.count(rand_index) != 0:
                rand_index = random.randint(0, 24)
            red_words.append(rand_index)
            j = j + 1
        while k != 7: # neutral
            rand_index = random.randint(0, 24)
            while blue_words.count(rand_index) != 0 or red_words.count(rand_index) != 0 or neutral_words.count(rand_index) != 0:
                rand_index = random.randint(0, 24)
            neutral_words.append(rand_index)
            k = k + 1
        rand_index = random.randint(0, 24)
        while blue_words.count(rand_index) != 0 or red_words.count(rand_index) != 0 or neutral_words.count(rand_index) != 0:
            rand_index = random.randint(0, 24)
        killer = rand_index
    return blue_words, red_words, neutral_words, killer


#generate field
def generate_field():
    field = Image.open("field.png")
    field = field.convert("RGBA")
    return field

#generate field with words
def generate_field_with_words(field, game_words):
    field_with_words = field.copy()
    idraw = ImageDraw.Draw(field_with_words)
    arial = ImageFont.truetype('font/ArialBlack.otf', size=20)
    i = 0
    l = 0
    k = 0
    j = 0
    h = 0
    m = 0
    while i != 25:
        arial = ImageFont.truetype('font/ArialBlack.otf', size=20)
        if len(game_words[i]) == 1:
            m = 50
        if len(game_words[i]) == 2:
            m = 40
        if len(game_words[i]) == 3:
            m = 35
        if len(game_words[i]) == 4:
            m = 29
        if len(game_words[i]) == 5:
            m = 20
        if len(game_words[i]) == 6:
            m = 13
        if len(game_words[i]) == 7:
            m = 8
        if len(game_words[i]) == 8:
            m = 0
        if len(game_words[i]) == 9:
            m = -5
        if len(game_words[i]) == 10:
            m = -10
        if len(game_words[i]) == 11:
            m = -20
        if len(game_words[i]) == 12:
            m = -18
            arial = ImageFont.truetype('font/ArialBlack.otf', size=18)
        if len(game_words[i]) == 13:
            m = -20
            arial = ImageFont.truetype('font/ArialBlack.otf', size=17)
        if i < 5:
            idraw.text((45 + i * 200 + m, 80), game_words[i], font=arial, fill=(0,0,0,0))
        if i >= 5 and i < 10:
            idraw.text((45 + l * 200 + m, 213), game_words[i], font=arial, fill=(0,0,0,0))
            l = l + 1
        if i >= 10 and i < 15:
            idraw.text((45 + k * 200 + m, 346), game_words[i], font=arial, fill=(0,0,0,0))
            k = k + 1
        if i >= 15 and i < 20:
            idraw.text((45 + j * 200 + m, 479), game_words[i], font=arial, fill=(0,0,0,0))
            j = j + 1
        if i >= 20 and i < 25:
            idraw.text((45 + h * 200 + m, 612), game_words[i], font=arial, fill=(0,0,0,0))
            h = h + 1
        i = i + 1
    return field_with_words

#generate field for captains
def generate_field_for_captains(field, blue_words, red_words, neutral_words, killer, game_words, coin):
    borders = Image.new('RGBA', field.size, (255,255,255,0))
    idraw = ImageDraw.Draw(borders)
    if coin == 0:
        i = 0
        while i != 9:
            if blue_words[i] < 5:
                idraw.rectangle((0 + blue_words[i] * 200, 0, 200 + blue_words[i] * 200, 133), fill=(0, 0, 255, 120))
            if blue_words[i] >=5 and blue_words[i] < 10:
                idraw.rectangle((0 + (blue_words[i] - 5) * 200, 133, 200 + (blue_words[i] - 5) * 200, 266), fill=(0, 0, 255, 120))
            if blue_words[i] >=10 and blue_words[i] < 15:
                idraw.rectangle((0 + (blue_words[i] - 10) * 200, 266, 200 + (blue_words[i] - 10) * 200, 399), fill=(0, 0, 255, 120))
            if blue_words[i] >=15 and blue_words[i] < 20:
                idraw.rectangle((0 + (blue_words[i] - 15) * 200, 399, 200 + (blue_words[i] - 15) * 200, 532), fill=(0, 0, 255, 120))
            if blue_words[i] >=20 and blue_words[i] < 25:
                idraw.rectangle((0 + (blue_words[i] - 20) * 200, 532, 200 + (blue_words[i] - 20) * 200, 665), fill=(0, 0, 255, 120))
            i = i + 1
        i = 0
        while i != 8:
            if red_words[i] < 5:
                idraw.rectangle((0 + red_words[i] * 200, 0, 200 + red_words[i] * 200, 133), fill=(255, 0, 0, 120))
            if red_words[i] >=5 and red_words[i] < 10:
                idraw.rectangle((0 + (red_words[i] - 5) * 200, 133, 200 + (red_words[i] - 5) * 200, 266), fill=(255, 0, 0, 120))
            if red_words[i] >=10 and red_words[i] < 15:
                idraw.rectangle((0 + (red_words[i] - 10) * 200, 266, 200 + (red_words[i] - 10) * 200, 399), fill=(255, 0, 0, 120))
            if red_words[i] >=15 and red_words[i] < 20:
                idraw.rectangle((0 + (red_words[i] - 15) * 200, 399, 200 + (red_words[i] - 15) * 200, 532), fill=(255, 0, 0, 120))
            if red_words[i] >=20 and red_words[i] < 25:
                idraw.rectangle((0 + (red_words[i] - 20) * 200, 532, 200 + (red_words[i] - 20) * 200, 665), fill=(255, 0, 0, 120))
            i = i + 1
        if killer < 5:
            idraw.rectangle((0 + killer * 200, 0, 200 + killer * 200, 133), fill=(32, 32, 32, 120))
        if killer >=5 and killer < 10:
            idraw.rectangle((0 + (killer - 5) * 200, 133, 200 + (killer - 5) * 200, 266), fill=(32, 32, 32, 120))
        if killer >=10 and killer < 15:
            idraw.rectangle((0 + (killer - 10) * 200, 266, 200 + (killer - 10) * 200, 399), fill=(32, 32, 32, 120))
        if killer >=15 and killer < 20:
            idraw.rectangle((0 + (killer - 15) * 200, 399, 200 + (killer - 15) * 200, 532), fill=(32, 32, 32, 120))
        if killer >=20 and killer < 25:
            idraw.rectangle((0 + (killer - 20) * 200, 532, 200 + (killer - 20) * 200, 665), fill=(32, 32, 32, 120))
        i = 0
        while i != 7:
            if neutral_words[i] < 5:
                idraw.rectangle((0 + neutral_words[i] * 200, 0, 200 + neutral_words[i] * 200, 133), fill=(192, 192, 192, 70))
            if neutral_words[i] >=5 and neutral_words[i] < 10:
                idraw.rectangle((0 + (neutral_words[i] - 5) * 200, 133, 200 + (neutral_words[i] - 5) * 200, 266), fill=(192, 192, 192, 70))
            if neutral_words[i] >=10 and neutral_words[i] < 15:
                idraw.rectangle((0 + (neutral_words[i] - 10) * 200, 266, 200 + (neutral_words[i] - 10) * 200, 399), fill=(192, 192, 192, 70))
            if neutral_words[i] >=15 and neutral_words[i] < 20:
                idraw.rectangle((0 + (neutral_words[i] - 15) * 200, 399, 200 + (neutral_words[i] - 15) * 200, 532), fill=(192, 192, 192, 70))
            if neutral_words[i] >=20 and neutral_words[i] < 25:
                idraw.rectangle((0 + (neutral_words[i] - 20) * 200, 532, 200 + (neutral_words[i] - 20) * 200, 665), fill=(192, 192, 192, 70))
            i = i + 1
    else:
        i = 0
        while i != 8:
            if blue_words[i] < 5:
                idraw.rectangle((0 + blue_words[i] * 200, 0, 200 + blue_words[i] * 200, 133), fill=(0, 0, 255, 120))
            if blue_words[i] >=5 and blue_words[i] < 10:
                idraw.rectangle((0 + (blue_words[i] - 5) * 200, 133, 200 + (blue_words[i] - 5) * 200, 266), fill=(0, 0, 255, 120))
            if blue_words[i] >=10 and blue_words[i] < 15:
                idraw.rectangle((0 + (blue_words[i] - 10) * 200, 266, 200 + (blue_words[i] - 10) * 200, 399), fill=(0, 0, 255, 120))
            if blue_words[i] >=15 and blue_words[i] < 20:
                idraw.rectangle((0 + (blue_words[i] - 15) * 200, 399, 200 + (blue_words[i] - 15) * 200, 532), fill=(0, 0, 255, 120))
            if blue_words[i] >=20 and blue_words[i] < 25:
                idraw.rectangle((0 + (blue_words[i] - 20) * 200, 532, 200 + (blue_words[i] - 20) * 200, 665), fill=(0, 0, 255, 120))
            i = i + 1
        i = 0
        while i != 9:
            if red_words[i] < 5:
                idraw.rectangle((0 + red_words[i] * 200, 0, 200 + red_words[i] * 200, 133), fill=(255, 0, 0, 120))
            if red_words[i] >=5 and red_words[i] < 10:
                idraw.rectangle((0 + (red_words[i] - 5) * 200, 133, 200 + (red_words[i] - 5) * 200, 266), fill=(255, 0, 0, 120))
            if red_words[i] >=10 and red_words[i] < 15:
                idraw.rectangle((0 + (red_words[i] - 10) * 200, 266, 200 + (red_words[i] - 10) * 200, 399), fill=(255, 0, 0, 120))
            if red_words[i] >=15 and red_words[i] < 20:
                idraw.rectangle((0 + (red_words[i] - 15) * 200, 399, 200 + (red_words[i] - 15) * 200, 532), fill=(255, 0, 0, 120))
            if red_words[i] >=20 and red_words[i] < 25:
                idraw.rectangle((0 + (red_words[i] - 20) * 200, 532, 200 + (red_words[i] - 20) * 200, 665), fill=(255, 0, 0, 120))
            i = i + 1
        if killer < 5:
            idraw.rectangle((0 + killer * 200, 0, 200 + killer * 200, 133), fill=(32, 32, 32, 120))
        if killer >=5 and killer < 10:
            idraw.rectangle((0 + (killer - 5) * 200, 133, 200 + (killer - 5) * 200, 266), fill=(32, 32, 32, 120))
        if killer >=10 and killer < 15:
            idraw.rectangle((0 + (killer - 10) * 200, 266, 200 + (killer - 10) * 200, 399), fill=(32, 32, 32, 120))
        if killer >=15 and killer < 20:
            idraw.rectangle((0 + (killer - 15) * 200, 399, 200 + (killer - 15) * 200, 532), fill=(32, 32, 32, 120))
        if killer >=20 and killer < 25:
            idraw.rectangle((0 + (killer - 20) * 200, 532, 200 + (killer - 20) * 200, 665), fill=(32, 32, 32, 120))
        i = 0
        while i != 7:
            if neutral_words[i] < 5:
                idraw.rectangle((0 + neutral_words[i] * 200, 0, 200 + neutral_words[i] * 200, 133), fill=(192, 192, 192, 70))
            if neutral_words[i] >=5 and neutral_words[i] < 10:
                idraw.rectangle((0 + (neutral_words[i] - 5) * 200, 133, 200 + (neutral_words[i] - 5) * 200, 266), fill=(192, 192, 192, 70))
            if neutral_words[i] >=10 and neutral_words[i] < 15:
                idraw.rectangle((0 + (neutral_words[i] - 10) * 200, 266, 200 + (neutral_words[i] - 10) * 200, 399), fill=(192, 192, 192, 70))
            if neutral_words[i] >=15 and neutral_words[i] < 20:
                idraw.rectangle((0 + (neutral_words[i] - 15) * 200, 399, 200 + (neutral_words[i] - 15) * 200, 532), fill=(192, 192, 192, 70))
            if neutral_words[i] >=20 and neutral_words[i] < 25:
                idraw.rectangle((0 + (neutral_words[i] - 20) * 200, 532, 200 + (neutral_words[i] - 20) * 200, 665), fill=(192, 192, 192, 70))
            i = i + 1
    field_for_captains = Image.alpha_composite(field, borders)
    field_for_captains = generate_field_with_words(field_for_captains, game_words)
    return field_for_captains

def generate_solved_field(field_with_words, word, game_words, blue_words, red_words, neutral_words, killer, first):
    index = game_words.index(word)
    generated_field = field_with_words.copy()
    if first == 0:
        if index in blue_words:
            blue_card = Image.open('blue_agent.png')
            if index < 5:
                generated_field.alpha_composite(blue_card, dest=(0 + 200 * index, 0))
            if index >=5 and index < 10:
                generated_field.alpha_composite(blue_card, dest=(0 + 200 * (index - 5), 133))
            if index >=10 and index < 15:
                generated_field.alpha_composite(blue_card, dest=(0 + 200 * (index - 10), 266))
            if index >=15 and index < 20:
                generated_field.alpha_composite(blue_card, dest=(0 + 200 * (index - 15), 399))
            if index >=20 and index < 25:
                generated_field.alpha_composite(blue_card, dest=(0 + 200 * (index - 20), 532))
            return generated_field
        elif index in red_words:
            red_card = Image.open('red_agent.png')
            if index < 5:
                generated_field.alpha_composite(red_card, dest=(0 + 200 * index, 0))
            if index >=5 and index < 10:
                generated_field.alpha_composite(red_card, dest=(0 + 200 * (index - 5), 133))
            if index >=10 and index < 15:
                generated_field.alpha_composite(red_card, dest=(0 + 200 * (index - 10), 266))
            if index >=15 and index < 20:
                generated_field.alpha_composite(red_card, dest=(0 + 200 * (index - 15), 399))
            if index >=20 and index < 25:
                generated_field.alpha_composite(red_card, dest=(0 + 200 * (index - 20), 532))
            return generated_field
        elif index in neutral_words:
            neutral = Image.open('neutral.png')
            if index < 5:
                generated_field.alpha_composite(neutral, dest=(0 + 200 * index, 0))
            if index >=5 and index < 10:
                generated_field.alpha_composite(neutral, dest=(0 + 200 * (index - 5), 133))
            if index >=10 and index < 15:
                generated_field.alpha_composite(neutral, dest=(0 + 200 * (index - 10), 266))
            if index >=15 and index < 20:
                generated_field.alpha_composite(neutral, dest=(0 + 200 * (index - 15), 399))
            if index >=20 and index < 25:
                generated_field.alpha_composite(neutral, dest=(0 + 200 * (index - 20), 532))
            return generated_field
        elif index == killer:
            killer_card = Image.open('killer.png')
            if index < 5:
                generated_field.alpha_composite(killer_card, dest=(0 + 200 * index, 0))
            if index >=5 and index < 10:
                generated_field.alpha_composite(killer_card, dest=(0 + 200 * (index - 5), 133))
            if index >=10 and index < 15:
                generated_field.alpha_composite(killer_card, dest=(0 + 200 * (index - 10), 266))
            if index >=15 and index < 20:
                generated_field.alpha_composite(killer_card, dest=(0 + 200 * (index - 15), 399))
            if index >=20 and index < 25:
                generated_field.alpha_composite(killer_card, dest=(0 + 200 * (index - 20), 532))
            return generated_field
    else:
        if index in blue_words:
            blue_card = Image.open('blue_agent.png')
            if index < 5:
                generated_field.alpha_composite(blue_card, dest=(0 + 200 * index, 0))
            if index >=5 and index < 10:
                generated_field.alpha_composite(blue_card, dest=(0 + 200 * (index - 5), 133))
            if index >=10 and index < 15:
                generated_field.alpha_composite(blue_card, dest=(0 + 200 * (index - 10), 266))
            if index >=15 and index < 20:
                generated_field.alpha_composite(blue_card, dest=(0 + 200 * (index - 15), 399))
            if index >=20 and index < 25:
                generated_field.alpha_composite(blue_card, dest=(0 + 200 * (index - 20), 532))
            return generated_field
        elif index in red_words:
            red_card = Image.open('red_agent.png')
            if index < 5:
                generated_field.alpha_composite(red_card, dest=(0 + 200 * index, 0))
            if index >=5 and index < 10:
                generated_field.alpha_composite(red_card, dest=(0 + 200 * (index - 5), 133))
            if index >=10 and index < 15:
                generated_field.alpha_composite(red_card, dest=(0 + 200 * (index - 10), 266))
            if index >=15 and index < 20:
                generated_field.alpha_composite(red_card, dest=(0 + 200 * (index - 15), 399))
            if index >=20 and index < 25:
                generated_field.alpha_composite(red_card, dest=(0 + 200 * (index - 20), 532))
            return generated_field
        elif index in neutral_words:
            neutral = Image.open('neutral.png')
            if index < 5:
                generated_field.alpha_composite(neutral, dest=(0 + 200 * index, 0))
            if index >=5 and index < 10:
                generated_field.alpha_composite(neutral, dest=(0 + 200 * (index - 5), 133))
            if index >=10 and index < 15:
                generated_field.alpha_composite(neutral, dest=(0 + 200 * (index - 10), 266))
            if index >=15 and index < 20:
                generated_field.alpha_composite(neutral, dest=(0 + 200 * (index - 15), 399))
            if index >=20 and index < 25:
                generated_field.alpha_composite(neutral, dest=(0 + 200 * (index - 20), 532))
            return generated_field
        elif index == killer:
            killer_card = Image.open('killer.png')
            if index < 5:
                generated_field.alpha_composite(killer_card, dest=(0 + 200 * index, 0))
            if index >=5 and index < 10:
                generated_field.alpha_composite(killer_card, dest=(0 + 200 * (index - 5), 133))
            if index >=10 and index < 15:
                generated_field.alpha_composite(killer_card, dest=(0 + 200 * (index - 10), 266))
            if index >=15 and index < 20:
                generated_field.alpha_composite(killer_card, dest=(0 + 200 * (index - 15), 399))
            if index >=20 and index < 25:
                generated_field.alpha_composite(killer_card, dest=(0 + 200 * (index - 20), 532))
        return generated_field

def check_player_first(msg):
    if msg.author in blue_team_wo_cap:
        return True
    else:
        return False

def check_player_second(msg):
    if msg.author in red_team_wo_cap:
        return True
    else:
        return False

description = '''Codenames is a board game for 2-8 players designed by Vlaada Chvátil and published by Czech Games. Two teams compete by each having a
Spymaster give one word clues which can point to multiple words on the board.'''
bot = discord.Client()

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='!codenames help'))
    print("Logged in as: " + (bot.user.name))
    print("ID: " + str(bot.user.id))
    print("READY!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    elif message.content.startswith("!codenames help"):
        help_string = "Список команд" + ''':
:closed_book: !codenames rules
:writing_hand: !codenames suggest
:game_die: !codenames start
:white_check_mark: !accept
:x: !decline'''
        await bot.send_message(message.channel, help_string)
        
    elif message.content.startswith("!codenames rules"):
        await bot.send_message(message.channel, "will be added soon!")
        
    elif message.content.startswith("!codenames suggest"):
        await bot.send_message(message.channel, "will be added soon!")
        
    elif message.content.startswith("!codenames start"): #first = red , second = blue
        player_list = message.author.voice.voice_channel.voice_members
        try:
            if len(player_list) < 4:
                await bot.send_message(message.channel, 'Необходимое большее количество игроков (4 или больше)')
                raise Exception("Not enough players")
            first = whos_first()
            next_first = first
            global blue_team
            global red_team
            global blue_cap_num
            global red_cap_num
            global blue_team_wo_cap
            global red_team_wo_cap
            blue_team, red_team, blue_cap_num, red_cap_num, blue_team_wo_cap, red_team_wo_cap = words.generate_teams(first, player_list)
            blue_player_string = ''
            red_player_string = ''
            for player in blue_team_wo_cap:
                if player == blue_team_wo_cap[0]:
                    blue_player_string = player.mention
                else:
                    blue_player_string = blue_player_string + ' ' + player.mention
            for player in red_team_wo_cap:
                if player == red_team_wo_cap[0]:
                    red_player_string = player.mention
                else:
                    red_player_string = red_player_string + ' ' + player.mention
            await bot.send_message(message.channel, '''Игра началась!
    :red_circle::red_circle::red_circle:
    :spy: Капитан красной команды: ''' + blue_team[blue_cap_num].mention + '''
    :busts_in_silhouette: Игроки красной команды: ''' + blue_player_string + '''
    :large_blue_circle::large_blue_circle::large_blue_circle:
    :spy: Капитан синей команды: ''' + red_team[red_cap_num].mention + '''
    :busts_in_silhouette: Игроки синей команды: ''' + red_player_string + '''
    Памятка: капитаны шифруют слово в виде: ```шифр количество_слов```
    Например: ```Вода 3```''')
            game_words = generate_words()
            blue_words, red_words, neutral_words, killer = generate_cards(first)
            field = generate_field()
            field_with_words = generate_field_with_words(field, game_words)
            field_for_captains = generate_field_for_captains(field, blue_words, red_words, neutral_words, killer, game_words, first)
            field_with_words.save('fww.png')
            field_for_captains.save('ffc.png')
            await bot.send_file(message.channel, 'fww.png')
            await bot.send_file(blue_team[blue_cap_num], 'ffc.png')
            await bot.send_file(red_team[red_cap_num], 'ffc.png')
            await bot.send_message(blue_team[blue_cap_num], ''':red_circle::red_circle::red_circle:
    Ваши карточки красного цвета!''')
            await bot.send_message(red_team[red_cap_num], ''':large_blue_circle::large_blue_circle::large_blue_circle:
    Ваши карточки синего цвета!''')
            win_condition = 0
            solved_field = field_with_words.copy()
            solved_field_for_caps = field_for_captains.copy()
            blue_death = 0
            red_death = 0
            while win_condition != 1:
                if next_first == 0:
                    await bot.send_message(message.channel, ''':large_blue_circle::large_blue_circle::large_blue_circle:
    Ход синих. Слово за капитаном ''' + red_team[red_cap_num].mention)
                    question = await bot.wait_for_message(timeout=300.0, author=red_team[red_cap_num], check=check)
                    last_num = question.content[len(question.content)-1]
                    word_nums = int(last_num)
                    while int(word_nums) > -1:
                        await bot.send_message(message.channel, 'Шифр ' + question.content + '. Слово за игроками ' + red_player_string)
                        answer = await bot.wait_for_message(timeout=300.0, check=check_player_second)
                        get_text = answer.content.upper()
                        try:
                            index = game_words.index(get_text)
                            if index in blue_words:
                                await bot.add_reaction(answer, '\U00002705')
                                await bot.add_reaction(answer, '\N{THUMBS UP SIGN}')
                                solved_field = generate_solved_field(solved_field, get_text, game_words, blue_words, red_words, neutral_words, killer, first)
                                solved_field.save('sf.png')
                                await bot.send_file(message.channel, 'sf.png')
                                solved_field_for_caps = generate_solved_field(solved_field_for_caps, get_text, game_words, blue_words, red_words, neutral_words, killer, first)
                                solved_field_for_caps.save('sfc.png')
                                await bot.send_file(red_team[red_cap_num], 'sfc.png')
                                await bot.send_file(blue_team[blue_cap_num], 'sfc.png')
                                blue_words.remove(index)
                                word_nums = int(word_nums) - 1
                                if len(blue_words) == 0:
                                    win_condition = 1
                                    word_nums = -1
                                if word_nums >= 1:
                                    await bot.send_message(message.channel, 'Отлично! Следующее слово? (Можно отгадать слов: ' + str(word_nums + 1)+ ')' + '''
    Напишите !done, чтобы закончить ход''')
                                elif word_nums == 0:
                                    await bot.send_message(message.channel, 'Отлично!')
                            else:
                                await bot.add_reaction(answer, '\U0000274C')
                                await bot.add_reaction(answer, '\N{THUMBS DOWN SIGN}')
                                solved_field = generate_solved_field(solved_field, get_text, game_words, blue_words, red_words, neutral_words, killer, first)
                                solved_field.save('sf.png')
                                await bot.send_file(message.channel, 'sf.png')
                                solved_field_for_caps = generate_solved_field(solved_field_for_caps, get_text, game_words, blue_words, red_words, neutral_words, killer, first)
                                solved_field_for_caps.save('sfc.png')
                                if index in red_words:
                                    red_words.remove(index)
                                await bot.send_file(red_team[red_cap_num], 'sfc.png')
                                await bot.send_file(blue_team[blue_cap_num], 'sfc.png')
                                if index in neutral_words or index in red_words:
                                    await bot.send_message(message.channel, 'К сожалению, ты обосрался. Ход переходит к красной команде')
                                elif index == killer:
                                    win_condition = 1
                                    red_death = 0
                                    blue_death = 1
                                word_nums = -1
                        except ValueError:
                            if answer.author == bot.user:
                                None
                            elif answer.content == '!done':
                                await bot.send_message(message.channel, 'Ход завершён, переход к синей команде')
                                word_nums = -1
                            else:
                                await bot.send_message(message.channel, 'Такого слова нет на поле')
                    next_first = 1
                else:
                    await bot.send_message(message.channel, ''':red_circle::red_circle::red_circle:
    Ход красных. Слово за капитаном ''' + blue_team[blue_cap_num].mention)
                    question = await bot.wait_for_message(timeout=300.0, author=blue_team[blue_cap_num], check=check)
                    last_num = question.content[len(question.content)-1]
                    word_nums = int(last_num)
                    while int(word_nums) > -1:
                        await bot.send_message(message.channel, 'Шифр ' + question.content + '. Слово за игроками ' + blue_player_string)
                        answer = await bot.wait_for_message(timeout=300.0, check=check_player_first)
                        get_text = answer.content.upper()
                        try:
                            index = game_words.index(get_text)
                            if index in red_words:
                                await bot.add_reaction(answer, '\U00002705')
                                await bot.add_reaction(answer, '\N{THUMBS UP SIGN}')
                                solved_field = generate_solved_field(solved_field, get_text, game_words, blue_words, red_words, neutral_words, killer, first)
                                solved_field.save('sf.png')
                                await bot.send_file(message.channel, 'sf.png')
                                solved_field_for_caps = generate_solved_field(solved_field_for_caps, get_text, game_words, blue_words, red_words, neutral_words, killer, first)
                                solved_field_for_caps.save('sfc.png')
                                await bot.send_file(red_team[red_cap_num], 'sfc.png')
                                await bot.send_file(blue_team[blue_cap_num], 'sfc.png')
                                red_words.remove(index)
                                word_nums = int(word_nums) - 1
                                if len(red_words) == 0:
                                    win_condition = 1
                                    word_nums = -1
                                if word_nums >= 1:
                                    await bot.send_message(message.channel, 'Отлично! Следующее слово? (Можно отгадать слов: ' + str(word_nums + 1)+ ')' + '''
    Напишите !done, чтобы закончить ход''')
                                elif word_nums == 0:
                                    await bot.send_message(message.channel, 'Отлично!')
                            else:
                                await bot.add_reaction(answer, '\U0000274C')
                                await bot.add_reaction(answer, '\N{THUMBS DOWN SIGN}')
                                solved_field = generate_solved_field(solved_field, get_text, game_words, blue_words, red_words, neutral_words, killer, first)
                                solved_field.save('sf.png')
                                await bot.send_file(message.channel, 'sf.png')
                                solved_field_for_caps = generate_solved_field(solved_field_for_caps, get_text, game_words, blue_words, red_words, neutral_words, killer, first)
                                solved_field_for_caps.save('sfc.png')
                                if index in blue_words:
                                    blue_words.remove(index)
                                await bot.send_file(red_team[red_cap_num], 'sfc.png')
                                await bot.send_file(blue_team[blue_cap_num], 'sfc.png')
                                if index in neutral_words or index in blue_words:
                                    await bot.send_message(message.channel, 'К сожалению, ты обосрался. Ход переходит к синей команде')
                                elif index == killer:
                                    win_condition = 1
                                    blue_death = 0
                                    red_death = 1
                                word_nums = -1
                        except ValueError:
                            if answer.author == bot.user:
                                None
                            elif answer.content == '!done':
                                await bot.send_message(message.channel, 'Ход завершён, переход к синей команде')
                                word_nums = -1
                            else:
                                await bot.send_message(message.channel, 'Такого слова нет на поле')
                    next_first = 0
            if len(blue_words) == 0 or red_death == 1:
                await bot.send_message(message.channel, ''':large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle:
    Игра закончена! Победа за синей командой!
    Капитан: ''' + red_team[red_cap_num].mention + '''
    Игроки: ''' + red_player_string + '''
    :large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle:''')
            elif len(red_words) == 0 or blue_death == 1:
                await bot.send_message(message.channel, ''':red_circle::red_circle::red_circle::red_circle::red_circle:
    Игра закончена! Победа за красной командой!
    Капитан: ''' + blue_team[blue_cap_num].mention + '''
    Игроки: ''' + blue_player_string + '''
    :red_circle::red_circle::red_circle::red_circle::red_circle:''')
        except Exception:
            print(Exception)
            
bot.run('place_your_token_here')
