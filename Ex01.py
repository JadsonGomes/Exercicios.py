# Resolução 01

#CRIAR 2 LISTAS (1° COM 5 NOMES) E MAIS (2° COM 5 VALORES EM REAIS)
lista_clientes=[]
lista_valores=[]

#USAR OS LAÇOS DE REPETIÇÃO PARA O PREENCHIMENTO DA MESMA FORMA QUE SAIRÁ NO MEN
print('*'*20,'MENU PRINCIPAL','*'*20)
print('PARA ENCERRAR O PROGRAMA DIGITE (Sair)')

while True:
  nome=input('Nome>> ')
  if nome.lower() == 'sair':
    break
  saldo=float(input('Saldo>> '))
  lista_clientes.append(nome)
  lista_valores.append(saldo)
  print('-'*60)

#SAIDA COM A LISTA DE CLIENTES CADASTRADOS
print('LISTA DE CLIENTES - BANCO NACIONAL')
print('|  NOME  |  SALDO  |  CONTA  |')
for conta, (nome, saldo) in enumerate(zip(lista_clientes, lista_valores), start=1):
  print('nome{}saldo{}  #{}   '.format(nome,saldo,conta)) #Comentário de teste