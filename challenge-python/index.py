def menu():
    print('\n')
    print('Bem vindo ao Porto Seguro Repair! Abaixo você encontra o nosso menu com as funções do nosso site! ')
    print('Serviços(1)    Cadastro(2)    Agendamento(3)    Sobre(4)    Contato(5)\n')

    while True:
        try:
            escolha = int(input('Escolha a opção que deseja: '))
            if 1 <= escolha <= 5:
                return escolha
            else:
                print('Opção inválida! Tente Novamente. ')
        except ValueError:
            print('Opção inválida! Tente um número inteiro. ')
     

    

def servicos():

    print('\n')
    print('Você está na aba Serviços! Abaixo você pode ver os nossos serviços pra você!\n')
    print('1. Orçamento Online')
    print('2. Agendamento de Serviços')
    print('3. PortoRepair')
    print('4. Voltar para o menu')

    escolha_servicos = int(input('Escolha uma opção: '))
    if escolha_servicos == 4:
        menu()
    return escolha_servicos
    


def cadastro():

    print('\n')
    print('Você está na aba Cadastro! Abaixo você pode se cadastrar no nosso site!\n')
    print('1. Fazer Cadastro\n2. Atualizar Cadastro\n3. Ver cadastro\n4. Voltar para o menu ')
    escolha_cadastro = int(input('Escolha uma opção: '))

    if escolha_cadastro == 1:
        fazer_cadastro()

    def fazer_cadastro():

        print('\n')
        
        nome = input('Digite seu nome completo: ')
        email = input('Digite seu email: ')
        endereco = input('Digite o seu endereço: ')
        profissao = input('Digite o seu emprego atual: ')
        carro = input('Digite o carro que será prestado o serviço: ')
        vetor_cadastro = [nome,email,endereco,profissao,carro]


        print(f'Nome: {vetor_cadastro[0]}\nEmail: {vetor_cadastro[1]}\nEndereço: {vetor_cadastro[2]}\nProfissão: {vetor_cadastro[3]}\nCarro: {vetor_cadastro[4]}\nConfirma os dados?    1.Sim   2.Não ')

        mostrar_cadastro = f'Nome: {vetor_cadastro[0]}\nEmail: {vetor_cadastro[1]}\nEndereço: {vetor_cadastro[2]}\nProfissão: {vetor_cadastro[3]}\nCarro: {vetor_cadastro[4]}'
        confirmacao = int(input('Escolha uma opção: '))

        if confirmacao == 1:
            print('Cadastro realizado com sucesso!')
            print('Voltando para o menu...')
            return vetor_cadastro    
        elif confirmacao == 2:
            print('Cadastro não realizado!')
            return cadastro()

def agendamento():

    print('\n')
    print('Você está na aba Agendamento! Abaixo você pode agendar uma manutenção ou revisão no nosso site!\n')
    print('1. Agendamento de Revisão\n2. Agendamento de Manutenção\n3. Voltar para o menu')
    escolha_agendamento = int(input('Escolha uma opção: '))
    if escolha_agendamento == 1:
        input('Digite a data para agendamento: ')

def sobre():

    print('\n')
    print('Você está na aba Sobre! Abaixo você pode ler um pouco sobre a história da Porto!\n')
    print(f"""A Porto (anteriormente Porto Seguro Seguros) é uma holding brasileira fundada em 1945. A atuação da empresa se baseia em três verticais de negócios: Porto Seguro, Porto Saúde e Porto Bank. Além de 11,7 milhões de clientes únicos, 13 mil funcionários, 12 mil prestadores de serviço e 36 mil corretores independentes, a empresa conta ainda com 101 sucursais e escritórios regionais em todo o Brasil. Ao todo, 27 empresas fazem parte do universo Porto Seguro, entre elas: Azul Seguros, Itaú Seguros de Auto e Residência, Porto Seguro Saúde, Porto Seguro Serviços e Porto Seguro Uruguai. Em 2022, a Companhia apresentou R$ 28,0 bilhões de receita e lucro líquido de R$ 1,13 bilhão.
        """)


    
    

def index():
    while True:
        escolha = menu()
        escolha_servicos = servicos()
        escolha_cadastro = cadastro()

        if escolha == 1:
            servicos()
            if escolha_servicos == 4:
                return menu()
        elif escolha == 2:
            cadastro()
            if escolha_cadastro == 4:
                return menu()
        else:
            menu()
        break

if __name__ == '__main__':
    index()