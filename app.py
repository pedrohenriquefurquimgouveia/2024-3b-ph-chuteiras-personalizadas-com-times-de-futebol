print(''' 
      P⃨H⃨ c⃨h⃨u⃨t⃨e⃨r⃨i⃨a⃨s⃨ p⃨e⃨r⃨s⃨o⃨n⃨a⃨l⃨i⃨z⃨a⃨d⃨a⃨s⃨ c⃨o⃨m⃨ t⃨i⃨m⃨e⃨ d⃨e⃨ f⃨u⃨t⃨e⃨b⃨o⃨l⃨

''')

print('1. cadastro de chuterias')
print('2. listar chuteiras')
print('3. ativar chuteiras')  
print('4. sair da aplicação')

opcao_escolhidas = input('escolha de opção: ')
print('Você escolheu a opção:', opcao_escolhidas)

if opcao_escolhidas == 1: 
    print('cadastrar chuteiras')
elif opcao_escolhidas == 2: 
    print('listar chuterias')
elif opcao_escolhidas == 3: 
    print('ativar chuteiras')
else: 
    print('saindo aplicaçaõ')