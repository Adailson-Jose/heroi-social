from flask_login import login_user

from app.persistence.UserDao import getUser, postUser


def valida_user(objUser):
    if getUser(objUser) == False:
        return False  # login errado
    print(login_user(objUser))
    return True  # usuario já cadastrado


def inserirUser(objUser, objEntidade):
    if postUser(objUser, objEntidade):
        return True  # cadastro ok
    return False  # cadastro não ok
    return False  # usuario já cadastrado
