biblioteca = [
    {"titulo": "1984", "autor": "George Orwell", "disponibilidade": True},
    {"titulo": "Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry", "disponibilidade": True},
    {"titulo": "Dom Quixote", "autor": "Miguel de Cervantes", "disponibilidade": True},
    {"titulo": "Hamlet", "autor": "William Shakespeare", "disponibilidade": False},
    {"titulo": "Harry Potter e a Pedra Filosofa", "autor": "J. K. Rowling", "disponibilidade": True},
]

def adicionar_livro(): 
        titulo = input("Digite o nome do livro a ser adicionado: ")  
        autor = input("Digite o autor desse livro: ")

        biblioteca.append({"titulo": titulo, "autor": autor, "disponibilidade": True})
        print(f"Livro {titulo} adicionado com sucesso!")

def emprestar_livro():
    titulo_emprestar = input("Digite o nome do livro que será emprestado: ")  
    encontrado = False

    for livro in biblioteca:
        if livro["titulo"] == titulo_emprestar:
            encontrado = True

            if livro["disponibilidade"]:
                livro["disponibilidade"] = False
                print(f"Livro {titulo_emprestar} emprestado com sucesso!") 
            else:
                print("Já emprestado!")
            break

    if not encontrado:
        print("Título não encontrado!")

def devolver_livro():
    titulo_devolver = input("Digite o nome do livro que será devolvido: ")  
    encontrado = False

    for livro in biblioteca:
        if livro["titulo"] == titulo_devolver: 
            encontrado = True

            if not livro["disponibilidade"]:
                livro["disponibilidade"] = True
                print(f"Livro {titulo_devolver} devolvido com sucesso!")
            else:
                print("Título já disponível!")
            break

    if not encontrado:
        print("Título não encontrado!")

def ver_livros():
    for livro in biblioteca:
        status = "Disponível" if livro["disponibilidade"] else "Emprestado"
        print(f"Livro: {livro['titulo']} - Autor: {livro['autor']} - Status: {status}")   

def ver_disponiveis():
    disponiveis = [livro for livro in biblioteca if livro["disponibilidade"]]

    if disponiveis:
        for livro in disponiveis:
                print(f"{livro['titulo']} - {livro['autor']}")
    else:
        print("Nenhum livro disponível no momento!")

def busca_titulo():
    busca = input("Digite o nome do livro: ")
    encontrado = False

    for livro in biblioteca:
        if busca.lower() == livro["titulo"].lower():
            print(f"Livro: {livro['titulo']} - {livro['autor']}")
            encontrado = True

    if not encontrado:
        print("Livro não encontrado!")

def livro_autor():
    busca = input("Digite o nome do autor: ")
    encontrado = False

    for livro in biblioteca:
        if busca.lower() == livro["autor"].lower():
            print(f"Livro: {livro['titulo']} - {livro['autor']}")
            encontrado = True
        
    if not encontrado:
        print("Livro não encontrado!")  

def estatistica():
    cont_d = 0
    cont_i = 0
    quant = len(biblioteca)  
    for livro in biblioteca:
        if livro["disponibilidade"]:
            cont_d += 1
        else:
            cont_i += 1

    print("=== ESTATÍSTICAS ===")  
    print(f"Total de livros: {quant}")
    print(f"Disponiveis: {cont_d}")  
    print(f"Indisponiveis: {cont_i}")       

def menu():
    while True:
        print("\n=== MENU SISTEMA BIBLIOTECA ===")
        print("1. Adicionar livro")
        print("2. Emprestar livro")
        print("3. Devolver livro")
        print("4. Ver todos os livros")
        print("5. Ver apenas disponíveis")
        print("6. Buscar livros por título")
        print("7. Livros por autor")
        print("8. Estatística")
        print("9. Sair")
        opcao = str(input("Selecione uma das opções acima: "))

        if opcao == "1":
          adicionar_livro()

        elif opcao == "2":
            emprestar_livro()
        
        elif opcao == "3":
            devolver_livro()
        
        elif opcao == "4":
            ver_livros()

        elif opcao == "5":
            ver_disponiveis()
        
        elif opcao == "6":
            busca_titulo()

        elif opcao == "7":
            livro_autor()

        elif opcao == "8":
            estatistica()

        elif opcao == "9":
            print("Saindo...")
            break
        else:
            print("Opção inválida!!")

def main():
     menu()

if __name__ == "__main__":
    main()     