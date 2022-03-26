import ampalibe
from ampalibe import Payload
from conf import Configuration

bot = ampalibe.init(Configuration())

# create a get started option to get permission of user.
bot.chat.get_started()

@ampalibe.command('/')
def main(sender_id, cmd, **extends):
    bot.chat.send_message(sender_id, "Bonjour, Bienvenue chez E-bouffe")
    text = 'Que puis-je faire pour vous ?'
    quick_rep = [
      {
        "content_type":"text",
        "title":"Liste de menu",
        "payload":"/listes/",
        "image_url":"https://img.icons8.com/nolan/64/restaurant-menu.png"
      },
      {
        "content_type":"text",
        "title":"Nous contacter",
        "payload":"/contact",
        "image_url":"https://img.icons8.com/nolan/64/ringer-volume.png"
      }
    ]
    bot.chat.send_quick_reply(sender_id, quick_rep, text)

@ampalibe.command('/contact')
def contact(sender_id, cmd, **extends):
    bot.chat.send_quick_reply(
        sender_id,
        [
            {
                "content_type":"text",
                "title":"+261 32 53 984 96",
                "payload": Payload("/print", value="+261325398496")
            },
            {
                "content_type":"text",
                "title":"gaetan@iteam-s.mg",
                "payload": Payload("/print", value="gaetan@iteam-s.mg")
            }
        ],
        'Eamil ou Telephone?'
    )    

@ampalibe.command('/print')
def afficher(sender_id, value, **extends):
    bot.chat.send_message(sender_id, value)