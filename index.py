import time
def menu():
    print('\n')
    print('Iniciando menu Porto Repair...')
    time.sleep(1.3)
    print('\n')
    print('Bem vindo ao Porto Seguro Repair! Abaixo você encontra o nosso menu com as funções do nosso site! ')
    print(' Sobre Serviços(1)    Cadastro(2)    Agendamentos(3)    Sobre(4)    Contato(5)    Sair do Porto Repair(6)\n')

    while True:
        try:
            escolha = int(input('Escolha a opção que deseja: '))
            if 1 <= escolha <= 6:
                return escolha
            else:
                print('Opção inválida! Tente Novamente. ')
        except ValueError:
            print('Opção inválida! Tente um número inteiro. ')
            return escolha
     

    

def sobre_servicos():
    print('\n')
    print('Iniciando nossa aba Sobre Serviços...')
    time.sleep(1.3)
    print('\n')
    print('Você está na aba Serviços! Abaixo você pode ver os nossos serviços pra você!\n')
    print('1. Orçamento Online')
    print('2. Agendamento de Serviços')
    print('3. PortoRepair')
    print('4. Voltar para o menu')

    escolha_servicos = int(input('Escolha uma opção: '))
    while True:
        try:
            if escolha_servicos == 1:
                print('\n')
                print('''           Faça um orçamento certeiro online, realizado de forma automática em poucos minutos  
            utilizando a nossa nova tecnologia SeguroRepair, a nossa Inteligencia Artificial que
            irá fazer seu orçamento e entregar o preço total.
                    ''')
                time.sleep(2.6)
                sobre_servicos()
            elif escolha_servicos == 2:
                agendamento()
            elif escolha_servicos == 3:
                print('\n')
                print('''        Fale com a nossa nova Inteligencia Artificial PortoRepair, com ela você pode descobrir qual é o\n       problema que o seu automóvel está enfrentando e agendar um reparo com uma de nossas oficinas parceiras!''')
                time.sleep(2.6)
                sobre_servicos()
            elif escolha_servicos == 4:
                print("\n")
                print('Voltando para o menu...')
                index()
            else:
                print('Opção inválida! Digite um número de 1 a 4!')
                sobre_servicos()
        except ValueError:
            print('Digite um número inteiro!')
            sobre_servicos()
            
        return escolha_servicos  
    


def cadastro():
    print('\n')
    print('Iniciando nossa aba Cadastro...')
    time.sleep(1.3)
    print('\n')
    print('Você está na aba Cadastro! Abaixo você pode se cadastrar no nosso site!\n')
    print('1. Fazer Cadastro\n2. Atualizar Cadastro\n3. Voltar para o menu ')
    escolha_cadastro = int(input('Escolha uma opção: '))
    try:
        if escolha_cadastro == 1:
            fazer_cadastro()
        elif escolha_cadastro == 2:
            atualizar_cadastro()
        elif escolha_cadastro == 3:
            print('\n')
            print('Voltando para o menu...')
            index()
        else:
            print('Opção inválida! Digite um número de 1 a 3')
    except ValueError:
        print('Erro! Digite um número inteiro!')
        cadastro()
    return escolha_cadastro

            



def fazer_cadastro():
    print('\n')
    print('Iniciando o Cadastro...')
    time.sleep(1.3)
    print('\n')
    print('''       Digite os dados abaixo para fazer o cadastro:

    ''')

    nome = input('Digite seu nome completo: ')
    email = input('Digite seu email: ')
    endereco = input('Digite o seu endereço: ')
    profissao = input('Digite o seu emprego atual: ')
    carro = input('Digite o modelo do seu carro: ')
    vetor_cadastro = [nome,email,endereco,profissao,carro]
    
    print("\n")

    print(f'Nome: {vetor_cadastro[0]}\nE-mail: {vetor_cadastro[1]}\nEndereço: {vetor_cadastro[2]}\nProfissão: {vetor_cadastro[3]}\nCarro: {vetor_cadastro[4]}\nConfirma os dados?    1.Sim   2.Não ')

    confirmacao = int(input('Escolha uma opção: '))
    try:
        if confirmacao == 1:
            print('Cadastro realizado com sucesso!')
            print('Voltando para o menu...')
            index()
    
        elif confirmacao == 2:
            print('Cadastro não realizado!')
            cadastro()
        else:
            print('Opção inválida! Digite um número entre 1 e 2. Seus dados não foram salvos. Faça o cadastro novamente.')
            fazer_cadastro()
    except ValueError:
        print('Erro! Digite um número inteiro!')
        fazer_cadastro()

    return vetor_cadastro 

def atualizar_cadastro():
    print('\n')
    print('Iniciando a Atualização de Cadastro...')
    time.sleep(1.3)
    print('\n')
    print('''Qual dado do seu cadastro você deseja atualizar?
1. Nome
2. E-mail
3. Endereço
4. Profissão
5. Carro
6. Voltar para a aba Cadastro ''')    
    escolha_atualizar = int(input('Escolha uma opção:  '))
    try:
        if escolha_atualizar == 1:
            nome = input('Digite seu nome completo: ')
            print('Nome Atualizado!')
            print(f'O Seu nome é: {nome}.')
            cadastro()
        elif escolha_atualizar == 2:
            email = input('Digite seu E-mail: ')
            print('E-mail Atualizado!')
            print(f'O seu E-mail é: {email}.')
            cadastro()
        elif escolha_atualizar == 3:
            endereco = input('Digite seu endereço: ')
            print('Endereço Atualizado!')
            print(f'O seu endereço é: {endereco}.')
            cadastro()
        elif escolha_atualizar == 4:
            profissao = input('Digite sua profissão: ')
            print('Profissão Atualizada!')
            print(f'A sua profissão é: {profissao}.')
            cadastro()
        elif escolha_atualizar == 5:
            carro = input('Digite o modelo do seu carro: ')
            print('Carro Atualizado!')
            print(f'O seu carro é: {carro}.')
            cadastro()
        elif escolha_atualizar == 6:
            print('\n')
            print('Voltando para a aba Cadastro...')
            cadastro()
        else:
            print('Opção inválida! Escolha um número de 1 a 6.')
            atualizar_cadastro()
    except ValueError:
            print('Erro! Digite um número inteiro!')
            atualizar_cadastro()
    cadastro_atualizado = [nome, email,endereco,profissao,carro]
    return cadastro_atualizado

        


def agendamento():
    print('\n')
    print('Iniciando a nossa aba Agendamentos...')
    time.sleep(1.3)
    print('\n')
    print('Você está na aba Agendamento! Abaixo você pode agendar uma manutenção ou revisão no nosso site!\n')
    print('1. Agendamento de Revisão\n2. Agendamento de Manutenção\n3. Voltar para o menu')
    escolha_agendamento = int(input('Escolha uma opção: '))
    try:
        if escolha_agendamento == 1:
            print('Digite a data para a revisão do seu veículo! Apenas com números.')
            dia = input('Digite o dia:  ')
            mes = input('Digite o mês:  ')
            ano = input('Digite o ano:  ')
            data = [dia,mes,ano]
            print(f'Excelente! A data para a revisão do seu veículo está agendada para: {data[0]}/{data[1]}/{data[2]}')
        elif escolha_agendamento == 2:
            print('Digite a data para a manutanção do seu veículo! Apenas com números.')
            dia = input('Digite o dia:  ')
            mes = input('Digite o mês:  ')
            ano = input('Digite o ano:  ')
            data = [dia,mes,ano]
            print(f'Excelente! A data para a manutenção do seu veículo está agendada para: {data[0]}/{data[1]}/{data[2]}')
        elif escolha_agendamento == 3:
            print('\n')
            print('Voltando para o menu...')
            index()
        else:
            print('Opção inválida! Digite um número de 1 a 3.')
            agendamento()
    except ValueError:
        print('Erro! Digite um número inteiro!')
    return data





def sobre():
    print('Iniciando a nossa aba Sobre...')
    time.sleep(1.3)
    print('\n')
    print('Você está na aba Sobre! Abaixo você pode ler um pouco sobre a história da Porto!\n')
    print(f"""              A Porto (anteriormente Porto Seguro Seguros) é uma holding brasileira fundada em 1945.
           A atuação da empresa se baseia em três verticais de negócios: Porto Seguro, Porto Saúde e Porto Bank.
           Além de 11,7 milhões de clientes únicos, 13 mil funcionários, 12 mil prestadores de serviço
           e 36 mil corretores independentes, a empresa conta ainda com 101 sucursais e escritórios regionais
           em todo o Brasil. Ao todo, 27 empresas fazem parte do universo Porto Seguro, entre elas: Azul Seguros,
           Itaú Seguros de Auto e Residência, Porto Seguro Saúde, Porto Seguro Serviços e Porto Seguro Uruguai.
           Em 2022, a Companhia apresentou R$ 28,0 bilhões de receita e lucro líquido de R$ 1,13 bilhão.""")
    time.sleep(5)
    print("\n")
    print('Voltando para o menu...')
    
    


def contato():
    print('\n')
    print('Iniciando a nossa aba Contato...')
    time.sleep(1.3)
    print('\n')
    print('Você está na aba Contato! Abaixo está nossos meios de contato para suporte e avaliação.')
    print('\n')

    print('''                   E-mail: portorepair.ia@gmail.com
                    Telefone: 333 76786
                    WhatsApp: (11) 3003 9303
         ''')
    time.sleep(3.5)
    print("\n")
    print('Voltando para o menu...')


    
    

def index():
    while True:
        try:
            escolha = menu()
            if escolha == 1:
                sobre_servicos()
            elif escolha == 2:
                cadastro()
            elif escolha == 3:
                agendamento()
            elif escolha == 4:
                sobre()
            elif escolha == 5:
                contato()
            elif escolha == 6:
                print('Obrigado por utilizar nosso sistema! A Porto Repair estará sempre aqui para te ajudar!')
                print('Fechando o Porto Repair...')
                time.sleep(1.6)
                break
            else: 
                print('Opção inválida! Digite um número de 1 a 5!')
        except ValueError:
                print('Erro! Digite um número inteiro!')
                index()


       
if __name__ == '__main__':
    index()
