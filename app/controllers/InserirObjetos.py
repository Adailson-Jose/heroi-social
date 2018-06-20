from app.models.PostObjeto import PostObjeto
from app.models.GetObjeto import GetObjeto


class InserirObjetos():

    def inserirUser(self, objUser, objEntidade):
        if GetObjeto.getUser(self, objUser) == False:
            if PostObjeto.postUser(self, objUser, objEntidade):
                return True  # cadastro ok
            return False  # cadastro não ok
        return False  # usuario já cadastrado
