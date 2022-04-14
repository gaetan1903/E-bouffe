from ampalibe import Model

class Database(Model):
    def __init__(self, conf):
        super().__init__(conf)

    @Model.verif_db
    def get_list_users(self):
        '''
            CREATE CUSTOM method to communicate with database
        '''
        req = "SELECT * from amp_user"
        self.cursor.execute(req)
        data = self.cursor.fetchall()
        self.db.commit()
        return data