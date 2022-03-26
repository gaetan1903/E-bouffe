import ampalibe
from conf import Configuration

bot = ampalibe.init(Configuration())

# create a get started option to get permission of user.
bot.chat.get_started()

@ampalibe.command('/')
def main(sender_id, cmd, **extends):
    bot.chat.send_message(sender_id, "Hello, Ampalibe")
    
