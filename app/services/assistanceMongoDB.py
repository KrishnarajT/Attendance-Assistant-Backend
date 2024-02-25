from mongodb import connect_to_mongo

class AssistanceService:
    def __init__(self):
        self.db = connect_to_mongo()

    