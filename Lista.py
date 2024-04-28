minha_lista = []

while True :
    print("Digite 1 para adicionar um elemento \n Digite 2 para exibir a lista \n Digite 3 para Sair")
    
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1 :
        elemento = input("Digite o elemento que deseja adicionar: ")
        minha_lista.append(elemento)
        print(f"'{elemento}' foi adicionado à lista.")
    elif escolha == 2:
        if len(minha_lista) == 0:
            print("A lista está vazia.")
        else :
            print("Elementos na lista : ")
            for item in minha_lista:
                print(item)
    elif escolha == 3 :
        print("Saindo do Programa")
        break
    else :
        print("Opção inválida. Por favor, escolha um opção válida.")