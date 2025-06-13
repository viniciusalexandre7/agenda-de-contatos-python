"Dividir as funcionalidades do código, Classes apenas retornam os metodos (são como os motores), Fazer inputs e prints com funções fora das classes"
import os

class Contato:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    def __str__(self):

        return f"Nome: {self.nome}\nNúmero: {self.numero}"

class Agenda:
    def __init__(self):

        #Cria uma lista vazia da Agenda    
        self.contatos = []

    #retona true caso tenha algum contato ou false caso não tenha um contato
    def adicionar_contato(self, contato):
        if contato:
            self.contatos.append(contato)
            return True
        return False
        
    def encontrar_por_atributo(self, atributo, valor_busca):
        
        #Exceção para caso os valores sejam vazios
        if not atributo or not valor_busca:
            raise ValueError("Atributo ou Valor buscado não podem ser vazio!")

        #atributo irá ser nome ou numero
        #valor_busca é o valor que irá ser buscado
        #para usar o return só fazer ("nome", "nome dessejado") ou ("numero", "numero desejado")


        encontrados = [contato for contato in self.contatos
        if hasattr(contato, atributo) and getattr(contato, atributo, "default").lower() == valor_busca.lower() ]

        #hasattr(obj, atributo) Verifica se um objeto tem um determinado atributo.
        #getattr Obtém o valor de um atributo de um objeto. Se o atributo não existir, pode retornar um valor padrão (evitando erro).



        return encontrados

    
    def deletar_contato(self, contato_deletar):

        if contato_deletar in self.contatos:
            self.contatos.remove(contato_deletar)
            return True
        return False

        

def executar_adicao(agenda_obj):
    nome = input("Digite o nome do contato: ")
    numero = input("Digite o numero do contato: ")
    contato = Contato(nome, numero)

    if agenda_obj.adicionar_contato(contato):
        print(f"Contato {nome} adicionado com sucesso!")
    else:
        print("Erro ao adicionar contato")


def executar_listagem(agenda_obj):

    if not agenda_obj.contatos:
        print("Agenda está vazia! Não há contatos para listar")
    else:
        lista_contatos = agenda_obj.contatos
        print(f"Você tem {len(lista_contatos)} contatos na sua lista!")
        for i, contato in enumerate(lista_contatos, start=1):
            print(f"\n---Contato {i}---")
            print(contato)
            print("---------------")


def executar_busca(agenda_obj):
    if not agenda_obj.contatos:
        print("Agenda está vazia!")
        return None

    print("Como você deseja encontrar o contato:")
    print("1- Buscar pelo nome")
    print("2- Buscar pelo número")

    escolha_opcao = input("Escolha sua Opção: ").strip()

    if escolha_opcao == '1':
        atributo = 'nome'
        valor_busca = input("Digite o nome do contato: ").strip()
    elif escolha_opcao == '2':
        atributo = 'numero'
        valor_busca = input("Digite o numero do contato: ").strip()
    else:
        print("Opção Ínvalida")
        return None

    contatos_encontrados = agenda_obj.encontrar_por_atributo(atributo, valor_busca)

    if not contatos_encontrados:
        print(f"Nenhum contato encontrado com {atributo}: '{valor_busca}'")
        return None

    print(f"Foram encontrados {len(contatos_encontrados)} contatos com o {atributo}: '{valor_busca}'")

    for i, contato in enumerate(contatos_encontrados, start=1):
        print(f"\n---Contato {i}---")
        print(contato)
        print("---------------")

    return contatos_encontrados

def editar_contatos(agenda_obj):
    contatos_encontrados = executar_busca(agenda_obj)

    if contatos_encontrados is None:
        print("Nenhum contato encontrado, operação cancelada.")
        return

    try:
        escolha_indice = 1 if len(contatos_encontrados) == 1 else int(input(f"Digite o índice do contato que deseja editar (1-{len(contatos_encontrados)}): "))

        if not (1 <= escolha_indice <= len(contatos_encontrados)):
            print("Número Fora do Intervalo")
            return

        contato_a_editar = contatos_encontrados[escolha_indice-1]

        print("---CASO NÃO DESEJA ALTERAR ALGUM ITEM, APENAS DEIXE EM BRANCO---\n")

        print(f"Nome Atual: {contato_a_editar.nome}")
        novo_nome = input("Digite o novo nome do contato: ").strip()
        if novo_nome:
            contato_a_editar.nome = novo_nome

        print(f"Número Atual: {contato_a_editar.numero}")
        novo_numero = input("Digite o novo numero do contato: ").strip()
        if novo_numero:
            contato_a_editar.numero = novo_numero
        
        print("\nDados atualizados com sucesso!")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")



def executar_deletacao(agenda_obj):
    contatos_encontrados = executar_busca(agenda_obj)

    if contatos_encontrados is None:
        print("Nenhum contato encontrado, operação cancelada.")
        return

    try:
        if len(contatos_encontrados) == 1:
            escolha_indice = 1
        else:
            escolha_indice = int(input(f"Digite o indice do contato que deseja deletar (1-{len(contatos_encontrados)}): "))

        if not (1 <= escolha_indice <= len(contatos_encontrados)):
            print("Número Fora do Intervalo")
            return

        contato_a_deletar = contatos_encontrados[escolha_indice-1]

        confirmar = input(f"Tem certeza que deseja deletar '{contato_a_deletar.nome}'? (s/n): ").lower().strip()

        if confirmar == "s":
            if agenda_obj.deletar_contato(contato_a_deletar):
                print("Contato deletado com sucesso!")
            else:
                print("Erro: O contato não foi encontrado na agenda para deleção.")
        else:
            print("Operação cancelada.")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")


def main():
    agenda = Agenda()

    while True:
        print("\n==== Menu da Agenda ====")
        print("1 - Adicionar contato")
        print("2 - Buscar contato")
        print("3 - Editar contato")
        print("4 - Remover contato")
        print("5 - Listar contatos")
        print("0 - Sair")

        try:
            escolha = int(input("Escolha uma opção: "))
        except ValueError:
            print("Operação ínvalida")
            return

        if escolha == 1:
            os.system("cls")
            print("---ADICIONAR CONTATOS---")
            executar_adicao(agenda)
        elif escolha == 2:
            os.system("cls")
            print("---BUSCAR CONTATOS---")
            executar_busca(agenda)
        elif escolha == 3:
            os.system("cls")
            print("---EDITAR CONTATOS---")
            editar_contatos(agenda)
        elif escolha == 4:
            os.system("cls")
            print("---DELETAR CONTATOS---")
            executar_deletacao(agenda)

        elif escolha == 5:
            os.system("cls")
            executar_listagem(agenda)

        elif escolha == 0:
            print("Saindo da agenda...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()