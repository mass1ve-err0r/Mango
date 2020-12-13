import motor.motor_asyncio as am


class MailObject:
    def __init__(self):
        self.mail = None
        self.subject = None
        self.message = None
        self.date = None


class MongoHandler:
    def __init__(self):
        self.client = am.AsyncIOMotorClient("mongodb://localhost:27017/")
        self.dbHandler = self.client["your_db_name"]
        self.collectionMail = self.dbHandler['your_collection_name']

    async def checkMongo(self):
        try:
            await self.client.admin.command('ismaster')
            print("Successfully connected to mongodb")
        except Exception:
            print("Could not connect to mongodb, check server settings or consider increasing the timeout value.")

    async def fetchNewEMails(self):
        _mails = []
        mailsCursor = self.collectionMail.find()
        async for document in mailsCursor:
            newMail = MailObject()
            newMail.mail = document['email']
            newMail.subject = document['subject']
            newMail.message = document['message']
            newMail.date = document['date']
            _mails.append(newMail)
        return _mails

    async def deleteMails(self):
        await self.collectionMail.drop()
        return
