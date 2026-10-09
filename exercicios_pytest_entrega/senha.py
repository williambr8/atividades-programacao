def cadastrar_senha(senha):
    if len(senha) < 8:
        raise ValueError("Senha muito curta")

    return True
