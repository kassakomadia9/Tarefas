

# Questao numero 5

# SISTEMA DE REGSTO DE NASCIMENTOS

# guardar nascimentos
nascimentos = []

# registar um nascimento
def registar_nascimento():

    print("\n--- REGISTO DE NASCIMENTO ---")

    nome_mae = input("Digite o nome da mae: ")
    identificacao_mae = input("Digite o numero de identificacao da mae: ")

    nome_bebe = input("Digite o nome do bebe: ")
    data = input("Digite a data do nascimento (DD/MM/AAAA): ")

    # Verificar se o nascimento aconteceu em outubro
    partes = data.split("/")

    if len(partes) != 3:

        print("Data invalida! Utilize DD/MM/AAAA.")
        return

    if partes[1] != "10":

        print("Este sistema so regista nascimentos de outubro.")
        return

    genero = input("Digite o genero do bebe (M/F): ").upper()

    if genero != "M" and genero != "F":

        print("Genero invalido!")
        return

    medico = input("Digite o nome do medico responsavel: ")

    #numero automaticamente
    numero = len(nascimentos) + 1
    codigo = "RN" + str(numero).zfill(5)

    # Guardar os dados do nascimento
    nascimento = {
        "codigo": codigo,
        "mae": nome_mae,
        "identificacao_mae": identificacao_mae,
        "bebe": nome_bebe,
        "data": data,
        "genero": genero,
        "medico": medico
    }

    nascimentos.append(nascimento)

    print("\nNascimento registado com sucesso!")
    print("Numero de identificacao do bebe:", codigo)


# consultar o bebe atraves da identificacao da mae
def consultar_bebe():

    print("\n--- CONSULTAR BEBE ---")

    identificacao = input("Digite o numero de identificacao da mae: ")

    encontrou = False

    for nascimento in nascimentos:

        if nascimento["identificacao_mae"] == identificacao:

            print("\nNumero do bebe:", nascimento["codigo"])
            print("Nome do bebe:", nascimento["bebe"])
            print("Data de nascimento:", nascimento["data"])
            print("Genero:", nascimento["genero"])
            print("Nome da mae:", nascimento["mae"])
            print("Medico responsavel:", nascimento["medico"])

            encontrou = True

    if encontrou == False:

        print("Nenhum registo encontrado para esta mae.")


# listar todos os nascimentos
def listar_nascimentos():

    print("\n--- LISTA DE NASCIMENTOS ---")

    if len(nascimentos) == 0:

        print("Ainda nao existem nascimentos registados.")

    else:

        for nascimento in nascimentos:

            print("Numero:", nascimento["codigo"])
            print("Bebe:", nascimento["bebe"])
            print("Data:", nascimento["data"])
            print("Genero:", nascimento["genero"])
            print("Mae:", nascimento["mae"])
            print("Medico:", nascimento["medico"])
            print("------------------------")


# apresentar as estatisticas
def mostrar_estatisticas():

    masculino = 0
    feminino = 0

    # Contar os bebes de cada genero
    for nascimento in nascimentos:

        if nascimento["genero"] == "M":

            masculino = masculino + 1

        elif nascimento["genero"] == "F":

            feminino = feminino + 1

    # Calcular o total de nascimentos
    total = masculino + feminino

    print("\n--- ESTATISTICAS DE OUTUBRO ---")

    print("Total de nascimentos:", total)
    print("Bebes masculinos:", masculino)
    print("Bebes femininos:", feminino)

    # Contar os nascimentos por medico
    print("\n--- NASCIMENTOS POR MEDICO ---")

    medicos = []

    for nascimento in nascimentos:

        nome_medico = nascimento["medico"]

        if nome_medico not in medicos:

            medicos.append(nome_medico)

    for medico in medicos:

        quantidade = 0

        for nascimento in nascimentos:

            if nascimento["medico"] == medico:

                quantidade = quantidade + 1

        print(medico, ":", quantidade, "nascimento(s)")


# MENU PRINCIPAL

opcao = ""

while opcao != "0":


    print("\n===== SISTEMA DE REGISTO DE NASCIMENTOS =====")
    print("1 - Registar nascimento")
    print("2 - Consultar bebe")
    print("3 - Listar nascimentos")
    print("4 - Mostrar estatisticas de outubro")
    print("0 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":

        registar_nascimento()

    elif opcao == "2":

        consultar_bebe()

    elif opcao == "3":

        listar_nascimentos()

    elif opcao == "4":

        mostrar_estatisticas()

    elif opcao == "0":

        print("Programa encerrado!")

    else:

        print("Opcao invalida!")
