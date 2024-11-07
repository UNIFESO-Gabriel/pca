"""
Escreva um programa que valide senhas com base nos critérios: tenha pelo menos 8 caracteres,
contendo letras maiúsculas, minúsculas, números e caracteres especiais.
"""

def ler_senha() -> str:
    senha: str = input("Crie uma senha válida. A senha deve conter, pelo menos:\n1- 8 caracteres;\n2- Uma letra maiúscula;\n3- Uma letra minúscula;\n4- Um dígito\n5- Um caractere especial.\nDigite sua senha: ")
    
    return senha


def validar_senha(senha: str) -> bool:
    
    # testa se há 8 caracteres.
    if len(senha) < 8:
        print("Senha contém menos de 8 caracteres!")
        return False
    
    # Verifica se a senha tem pelo menos uma letra maiúscula.
    elif not any([char.isupper() for char in senha]):
        print("Senha não contém pelo menos uma letra maiúscula!")
        return False
    
    # Verifica se a senha tem pelo menos uma letra minúscula.
    elif not any([char.islower() for char in senha]):
        print("Senha não contém pelo menos uma letra minúscula!")
        return False

    # Verifica se a senha tem pelo menos um dígito.
    elif not any([char.isdigit() for char in senha]):
        print("Senha não contém pelo menos um dígito!")
        return False
    
    # Verifica se a senha tem pelo menos um caractere especial.
    elif not any([not char.isalnum() and not char.isspace() for char in senha]):
        print("Senha não contém pelo menos um caractere especial!")
        return False
    
    return True


def main() -> None:
    senha: str = ler_senha()
    
    print(f"Senha {senha} é válida!") if validar_senha(senha) else \
    print(f"Senha {senha} é inválida!")
    
    
if __name__ == "__main__":
    main()