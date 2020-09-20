# 3rd-party
import discord

CHARACTERS = {
    "charlie": "Charlie Barnes",
    "dakota": "Dakota Travis",
    "evan": "Evan Holwell",
    "jack": "Jack Briarwood",
    "julia": "Julia North",
}

# Image paths
CHARACTER_IMAGE_DIR = "Images/Cards/Characters"
SUSPECT_IMAGE_DIR = "Images/Cards/Suspects"
LOCATION_IMAGE_DIR = "Images/Cards/Locations"

# Game length in seconds (90 minutes)
GAME_LENGTH = 90 * 60
# How often the bot should check the timer
TIMER_GAP = 10

# Times to send clue cards
CLUE_TIMES = (90, 80, 70, 60, 50, 45, 40, 35, 30, 20)
BUCKET_SIZES = {3: (3, 3, 4), 4: (2, 2, 3, 3), 5: (2, 2, 2, 2, 2)}

class Data:
    def __init__(self, guild):
        self.guild = guild
        self.setup = False
        self.started = False
        self.show_timer = False
        self.char_roles = {
            role.name: role
            for role in guild.roles
            if role.name.lower() in CHARACTERS and role.members
        }
