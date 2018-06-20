from flask_login import login_user

from app.models.GetObjeto import GetObjeto


class Logar():

    def logar(self, objUser):
        if GetObjeto.getUser(self, objUser) == False:
            return False  # login errado
        print(login_user(objUser))
        return True  # usuario já cadastrado
