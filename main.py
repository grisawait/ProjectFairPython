import random
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

adventure_games = [
    'The Legend of Zelda: Breath of the Wild',
    'Uncharted 4: A Thief\'s End',
    'Tomb Raider (2013)',
    'Life is Strange',
    'Brothers: A Tale of Two Sons',
    'Firewatch',
    'Oxenfree',
    'The Walking Dead (Telltale Games)',
    'Night in the Woods',
    'What Remains of Edith Finch'
]

role_play_games = [
    'The Elder Scrolls V: Skyrim',
    'The Witcher 3: Wild Hunt',
    'Final Fantasy VII',
    'Mass Effect 2',
    'Dark Souls',
    'Dragon Age: Origins',
    'Diablo II',
    'Fallout 3',
    'Baldur\'s Gate II: Shadows of Amn',
    'Chrono Trigger'
]
strategy_games = [
    'Civilization VI',
    'Starcraft II',
    'XCOM 2',
    'Total War: Warhammer II',
    'Age of Empires II',
    'Crusader Kings III',
    'Company of Heroes 2',
    'Europa Universalis IV',
    'Command and Conquer: Red Alert 2',
    'Homeworld Remastered Collection'
]
sports_games = [
    'FIFA 22',
    'NBA 2K22',
    'Madden NFL 22',
    'MLB The Show 21',
    'WWE 2K22',
    'PGA Tour 2K21',
    'UFC 4',
    'NHL 22',
    'Mario Tennis Aces',
    'Top Spin 4'
]
fighting_games = [
    'Street Fighter V',
    'Mortal Kombat 11',
    'Tekken 7',
    'Dragon Ball FighterZ',
    'Super Smash Bros. Ultimate',
    'Injustice 2',
    'Marvel vs. Capcom: Infinite',
    'Guilty Gear Strive',
    'Killer Instinct',
    'Soulcalibur VI'
]
action_games = [
    'Grand Theft Auto V',
    'Red Dead Redemption 2',
    'The Last of Us Part II',
    'God of War',
    'Assassin\'s Creed Valhalla',
    'Horizon Zero Dawn',
    'Control',
    'Doom Eternal',
    'Devil May Cry 5',
    'Nier: Automata'
]

button1 = KeyboardButton("Action🎬")
button2 = KeyboardButton("Adventure🏔️")
button3 = KeyboardButton("Role-Play🧛")
button4 = KeyboardButton("Sports🏐")
button5 = KeyboardButton("Fighting🥊")
button6 = KeyboardButton("Strategy🎯")
buttons = [button1, button2, button3, button4, button5, button6]
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, keyboard=[buttons])

# Define a function to handle incoming messages
def handle_message(update, context):
    # Get the message text from the user
    message = update.message.text.lower()

    # Check user's message for keywords and suggest games
    if 'adventure' in message:
        reply = "I think you would like "+random.choice(adventure_games)
    elif 'strategy' in message:
        reply = "I think you would like " + random.choice(strategy_games)
    elif 'action' in message:
        reply = "I think you would like " + random.choice(action_games)
    elif 'sports' in message:
        reply = "I think you would like " +random.choice(sports_games)
    elif 'fighting' in message:
        reply = "I think you would like " +random.choice(fighting_games)
    elif 'role-play' in message:
        reply = "I think you would like " + random.choice(role_play_games)

    # Send the reply back to the user
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply)


# Define a function to handle /start commands
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Hi! I'm a game recommendation bot. What kind of game are you interested in?", reply_markup=keyboard1)


# Create a new bot instance and start the bot
bot = telegram.Bot(token='5659969870:AAH6C5DCC6MhomkXkp_T90Gne6C091E25Lk')
updater = Updater(token='5659969870:AAH6C5DCC6MhomkXkp_T90Gne6C091E25Lk', use_context=True)
dispatcher = updater.dispatcher

# Add handlers for incoming messages and /start commands
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
dispatcher.add_handler(CommandHandler('start', start))

# Start the bot and keep it running
updater.start_polling()
updater.idle()