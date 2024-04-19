def menu():
  """Exibe o menu e retorna a opção escolhida pelo usuário."""
  print("\n--- Menu Principal ---")
  print("1. Calcular média")
  print("2. Verificar par/ímpar")
  print("3. Sair")

  while True:
    try:
      opcao = int(input("Digite a opção desejada: "))
      if 1 <= opcao <= 3:
        return opcao
      else:
        print("Opção inválida. Tente novamente.")
    except ValueError:
      print("Entrada inválida. Digite um número inteiro.")

def calcular_media():
  # Função para calcular a média de números
  while True:
    try:
      # Solicita ao usuário a quantidade de números
      quantidade_numeros = int(input("Digite a quantidade de números para calcular a média: "))
      if quantidade_numeros > 0:
        break  # Sai do loop se a quantidade for válida
      else:
        print("Quantidade inválida. Digite um número maior que zero.")
    except ValueError:
      print("Entrada inválida. Digite um número inteiro.")

  # Inicializa a variável para somar os números
  soma = 0

  # Itera sobre a quantidade de números informada
  for i in range(quantidade_numeros):
    try:
      # Solicita ao usuário cada número
      numero = float(input(f"Digite o {i+1}º número: "))
      soma += numero  # Adiciona o número à soma
    except ValueError:
      print("Entrada inválida. Digite um número.")

  # Calcula e retorna a média
  if soma != 0:
    media = soma / quantidade_numeros
    print(f"A média dos números é: {media}")
  else:
    print("Não foi possível calcular a média. Nenhum número válido foi informado.")


def verificar_par_impar():
  # Função para verificar se um número é par ou ímpar
  """
  Verifica se um número é par ou ímpar.

  Argumento:
    numero (float): O número a ser verificado.

  Retorno:
    str: A mensagem informando se o número é par ou ímpar.
  """
  while True:
    try:
      # Solicita ao usuário o número
      numero = float(input("Digite um número: "))
      break  # Sai do loop após obter o número
    except ValueError:
      print("Entrada inválida. Digite um número.")

  # Verifica se o número é par ou ímpar e retorna a mensagem
  if numero % 2 == 0:
    print( f"O número {numero} é par.")
  else:
    print(f"O número {numero} é ímpar.")

def main():
  while True:
    opcao = menu()

    if opcao == 1:
      calcular_media()
    elif opcao == 2:
      verificar_par_impar()
    else:
      print("Saindo do programa...")
      break

if __name__ == "__main__":
  main()










