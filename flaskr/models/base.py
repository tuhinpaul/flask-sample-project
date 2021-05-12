from flaskr.database import Database

class Base(Database.Base):
    __abstract__ = True

    def get_all(self):
        return self.query.all()
