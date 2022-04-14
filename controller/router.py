import ampalibe 
from model import Database
from view import Client
from conf import Configuration


req = Database(Configuration())
client = Client()

@ampalibe.command('/')
def main(sender_id, cmd, **extends):
    # print(req.get_list_users())
    client.greet(sender_id)


class Client:
    
    @ampalibe.command('/contact')
    def contact(sender_id, cmd, **extends):
        client.contact(sender_id)

    @ampalibe.command('/print')
    def afficher(sender_id, value, **extends):
        client.afficher(sender_id, value)

class Admin:
    pass
