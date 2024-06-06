from config.db import conn

def verificacao_usuario_banco(usuario, senha):
    for x in conn.local.user.find({}, {"_id": 0, "name": 0}):
        if usuario == x["user"] and senha == x["password"]:
            return True

    return False