from app import app, db


class PostObjeto():

    def postUser(self, user, entidade):
        db.session.add(user)
        db.session.add(entidade)
        if db.session.commit() == None:
            return True  # user foi inserido no banco
        return False
