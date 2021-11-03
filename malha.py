import random as rd

rd.seed(42)  # comando para definir uma seed para os números aleatórios

# função que cria a malha como uma matriz quadrada de tamanho n
def criaMalha(n):
  malha = []

  for _ in range(n):
    linha = []
    for _ in range(n):
      linha.append(0)
    malha.append(linha)

  malha[0][0] = 'robo'

  return malha


# função que gera aleatoriamente as latas na malha, cerca de 20% da malha é preenchida com latas
# retorna um vetor com as posições das latas na malha
def preencheMalha(malha):
  latas = []
  for _ in range(int(0.2 * len(malha) ** 2)):
    while True:
      x = rd.randint(0,len(malha)-1)
      y = rd.randint(0,len(malha)-1)
      if (x + y != 0) and (malha[x][y] != 'robo') and (malha[x][y] != 'lata'):
        malha[x][y] = 'lata'
        latas.append([x,y])
        break
  latas = sorted(latas, key=lambda k: [k[0], k[1]])
  
  return latas
