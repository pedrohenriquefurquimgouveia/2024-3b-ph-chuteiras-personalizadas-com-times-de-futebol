import os

chuteiras = []

def mostra_titulo():
    print(''' 
      P⃨H⃨ c⃨h⃨u⃨t⃨e⃨r⃨i⃨a⃨s⃨ p⃨e⃨r⃨s⃨o⃨n⃨a⃨l⃨i⃨z⃨a⃨d⃨a⃨s⃨ c⃨o⃨m⃨ t⃨i⃨m⃨e⃨ d⃨e⃨ f⃨u⃨t⃨e⃨b⃨o⃨l⃨

''')

def mostra_escolhas():
    print('1. cadastro de chuterias')
    print('2. listar chuteiras')
    print('3. ativar chuteiras')  
    print('4. sair da aplicação')

def escolha_opcao():
    try:
        opcao_escolhida = int(input('escolha de opção: '))
        print('Você escolheu a opção: ', opcao_escolhida)

        if  opcao_escolhida == 1: 
            print('cadastrar chuteiras')
        elif opcao_escolhida == 2: 
            print('listar chuterias')
        elif opcao_escolhida == 3: 
            print('ativar/desativar chuteiras')
        elif opcao_escolhida == 4:
            finalizar_programa
        else: 
            opcao_invalida()
    except:
        opcao_invalida()
        
        
def cadastrar_chuteiras():
    os.system('cls')
    print('Cadastrando chuteiras... ')
    nome_chuteira = input('Digite o nome da chuteira')
    chuteiras.append(nome_chuteira)
    print(f'O {nome_chuteira} foi adicionado(a) à lista de chuteiras')
    input('Digite qualquer tecla para voltar')
    main()
    
def mostrar_chuteiras():
    os.system('cls')
    print('Lista de chuteiras')
    
def finalizar_programa():
    os.system('clear') 
    print('finalizando programa')
    
def opcao_invalida():
    print('Esse caracter não é permitido') 
    input('digite qualquer tecla')
    main() 
    
def main():
    mostra_titulo()
    mostra_escolhas()
    escolha_opcao()  
      