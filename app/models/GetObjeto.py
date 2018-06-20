from app.models.Tabelas import usuario


class GetObjeto():

    def getUser(self, user):
        user = usuario.query.filter_by(email=user.email).first()
        print(user.email)
        if user == None:
            return False  # não tem esse user no banco
        return True
