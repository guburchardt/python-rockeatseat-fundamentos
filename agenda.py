def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato):
    contato = {"nome": nome_contato, "telefone": telefone_contato, "email": email_contato, "favorito": False}
    contatos.append(contato)
    print(f"\nContato {nome_contato} foi adicionado com sucesso")
    return

def visualizar_contatos(contatos):
    for indice, contato in enumerate(contatos, start=1):
        favorito = "☆" if contato["favorito"] else " "
        nome_contato = contato["nome"]
        telefone_contato = contato["telefone"]
        email_contato = contato["email"]
        print(f"{indice}. [{favorito}] {nome_contato} {telefone_contato} {email_contato}")

def editar_contato(contatos, indice_escolha, tipo_ajuste):
    indice_escolha_ajustado = indice_escolha - 1
    if tipo_ajuste == 1:
        novo_nome = input("Digite o novo nome: ")
        contatos[indice_escolha_ajustado]["nome"] = novo_nome
        print(f"O contato {indice_escolha} atualizado para {novo_nome}")
    elif tipo_ajuste == 2:
        novo_telefone = input("Digite o novo telefone: ")
        contatos[indice_escolha_ajustado]["telefone"] = novo_telefone
        print(f"O contato {indice_escolha} atualizado para {novo_telefone}")
    elif tipo_ajuste == 3:
        novo_email = input("Digite o novo e-mail: ")
        contatos[indice_escolha_ajustado]["email"] = novo_email
        print(f"O contato {indice_escolha} atualizado para {novo_email}")
    else: 
        print("Voce digitou uma opcao inválida")
    return

def marcar_favorito(contatos, indice_escolha):
    indice_escolha_ajustado = indice_escolha - 1
    contatos[indice_escolha_ajustado]["favorito"] = True
    print(f"O contato {indice_escolha} foi atualizado para favorito")
    return

def desmarcar_favorito(contatos, indice_escolha):
    indice_escolha_ajustado = indice_escolha - 1
    contatos[indice_escolha_ajustado]["favorito"] = False
    print(f"O contato {indice_escolha} foi desmarcado como favorito")

def visualizar_contatos_favoritos(contatos):
    for contato in contatos:
        if contato["favorito"] == True:
            print(f"Nome: {contato["nome"]} Numero: {contato["telefone"]} Email: {contato["email"]}")
    return

def apagar_contato(contatos, indice_escolha):
    indice_escolha_ajustado = indice_escolha - 1
    contato_removido = contatos.pop(indice_escolha_ajustado)
    print("O contato removido: ", contato_removido["nome"])


contatos = []

while True:
    print("\nAgenda Telefonica:")
    print("1 - Adicionar contato")
    print("2 - Visualizar lista de contatos")
    print("3 - Editar um contato")
    print("4 - Marcar um contato como favorito")
    print("5 - Desmarcar um contato como favorito")
    print("6 - Visualizar lista de contatos favoritos")
    print("7 - Apagar um contato")
    print("8 - Sair")

    escolha = int(input("\nDigite a sua escolha:"))

    if escolha == 1:
        nome_contato = input("Digite o nome:")
        telefone_contato = input("Digite o telefone:")
        email_contato = input("Digite o e-mail:")
        adicionar_contato(contatos, nome_contato, telefone_contato, email_contato)
    if escolha == 2:
        visualizar_contatos(contatos)
    if escolha == 3:
        visualizar_contatos(contatos)
        indice_escolhido = int(input("Digite o indice do contato que deseja editar: "))
        print("Qual ajuste deseja realizar?")
        print("1 - Editar nome")
        print("2 - Editar telefone")
        print("3 - Editar email")
        edicao_escolhido = int(input("Digite a sua escolha: "))
        editar_contato(contatos, indice_escolhido, edicao_escolhido)
    if escolha == 4:
        visualizar_contatos(contatos)
        indice_escolhido = int(input("Digite o indice do contato que deseja favoritar: "))
        marcar_favorito(contatos,indice_escolhido)
    if escolha == 5:
        visualizar_contatos(contatos)
        indice_escolhido = int(input("Digite o indice do contato que deseja desmarcar como favorito: "))
        desmarcar_favorito(contatos, indice_escolhido)
    if escolha == 6:
        visualizar_contatos_favoritos(contatos)
    if escolha == 7:
        visualizar_contatos(contatos)
        indice_escolhido = int(input("Digite o indice do contato que deseja apagar: "))
        apagar_contato(contatos, indice_escolhido)
    if escolha == 8:
        break;