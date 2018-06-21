from app import lm

from app.models.Tabelas import usuario


@lm.user_loader
def load_user(id):
    print(usuario.email)
    return usuario.query.filter_by(id=usuario.id).first()
