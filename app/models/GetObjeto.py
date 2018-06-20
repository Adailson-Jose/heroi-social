from app.models.Tabelas import usuario


class GetObjeto():

    def getUser(self, user):
        user = usuario.query.filter_by(email=user.email).first()
        if user == None:
            return False  # não tem esse user no banco
        return True
