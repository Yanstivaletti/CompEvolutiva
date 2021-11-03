from copy import deepcopy
from statistics import mean
import random as rd
from time import sleep


# função que avalia a população
def fitness(populacao, latas, malha, robo):
  fit = []
  
  # para cada cromossomo chama a função objetivo
  for c in populacao:
    (_,qtdDeLatas,direcoes) = robo.funcObjetivo(latas, malha, c)
    
    # se sobrar 1 lata na malha então a nota do cromossomo é definida em seu número de passos * 2
    if qtdDeLatas == 1:
      nota = len(direcoes) * 2
    
    # se todas as latas foram recolhidas então a nota do cromossomo é o número de passos
    elif qtdDeLatas == 0:
      nota = len(direcoes)
    # se nem todas as latas foram recolhidas então a nota do cromossomo é a quantidade de latas que faltaram ser recolhidas
    # * o número de passos
    else:
      nota = qtdDeLatas * len(direcoes)
    
    fit.append(nota) # armazena a nota do cromossomo no vetor de fit
    
  return fit # retorna o vetor de fit dos cromossomos

# função para selecionar um cromossomo proporcionalmente pelo seu fit
def selecao(fit):
  fit = sorted(fit)
  
  prob = [x / sum(fit) for x in fit]
  
  rand = rd.uniform(0, max(prob))
  
  for i in range(len(prob)):
    if rand < prob[i]:
      return i
 
# função de crossover
def crossover(populacao, p1, p2, pc):
  
  if len(populacao[p1]) < len(populacao[p2]):
    aux = populacao[p1]
  else:
    aux = populacao[p2]
    
  c = rd.randrange(1, len(aux)-1)
  
  if rd.uniform(0,1) < pc:
    temp = populacao[p1][0:c]
    populacao[p1][0:c] = populacao[p2][0:c]
    populacao[p2][0:c] = temp

# função de mutação
def mutacao(populacao, pm):
  for i in range(len(populacao)):
    if rd.uniform(0,1) < pm:
      c = rd.randrange(0, len(populacao[i]))
      
      if populacao[i][c] == 'D':
        if rd.random() < 2/3:
          populacao[i][c] = 'E'
        else:
          if rd.random() < 1/2:
            populacao[i][c] = 'C'
          else:
            populacao[i][c] = 'B'
      
      if populacao[i][c] == 'E':
        if rd.random() < 2/3:
          populacao[i][c] = 'D'
        else:
          if rd.random() < 1/2:
            populacao[i][c] = 'C'
          else:
            populacao[i][c] = 'B'
      
      if populacao[i][c] == 'B':
        if rd.random() < 2/3:
          populacao[i][c] = 'C'
        else:
          if rd.random() < 1/2:
            populacao[i][c] = 'D'
          else:
            populacao[i][c] = 'E'
      
      if populacao[i][c] == 'C':
        if rd.random() < 2/3:
          populacao[i][c] = 'B'
        else:
          if rd.random() < 1/2:
            populacao[i][c] = 'D'
          else:
            populacao[i][c] = 'E'
          
def indiceDoMenor(lista):
  menor = None
  for i in range(len(lista)):
    if i == 0:
      menor = i
    if lista[menor] > lista[i]:
      menor = i
  return menor

# função que roda o AG
def rodaAG(populacao, numeroGeracoes, pc, pm, latas, malha, robo):

  fit = fitness(populacao, latas, malha, robo)
  fitOriginal = deepcopy(fit)
  print(f'\nFit original: {fit}')

  gen = 0
  print(f'\nGeração: 0, Fit mínimo: {min(fit)}, Média: {mean(fit)}')
  sleep(0.7)

  while gen < numeroGeracoes:
    
    pool = []
    
    for _ in range(len(populacao)):
      pool.append(selecao(fit))

    oldpop = deepcopy(populacao)
    oldfit = deepcopy(fit)

    for i in range(len(populacao)):
      populacao[i] = deepcopy(oldpop[pool[i]])

    for i in range(0,len(populacao),2):
      crossover(populacao, i, i+1, pc)

    for _ in populacao:
      mutacao(populacao, pm)
      
    fit = fitness(populacao, latas, malha, robo)
      
    print(f'\nFit antigo: {oldfit}')
    print(f'Fit atual: {fit}')
    
      
    for i in range(len(fit)):
      if oldfit[i] < fit[i]:
        populacao[i] = deepcopy(oldpop[i])
      
    fit = fitness(populacao, latas, malha, robo)
    print(fit)

    gen += 1
    print(f'Geração: {gen}, Fit mínimo: {min(fit)}, Média: {mean(fit)}')
    #sleep(0.7)

  fit = fitness(populacao, latas, malha, robo)
  print(f'\nFit original: {fitOriginal}')
  print(f'Fit depois do AG: {fit}')
  melhorFit = indiceDoMenor(fit)
  melhorFitOririnal = indiceDoMenor(fitOriginal)
  [_, qtdDeLatas, direcoes] = robo.funcObjetivo(latas, malha, populacao[melhorFit])
  resultado = [qtdDeLatas, direcoes, fit[melhorFit], fitOriginal[melhorFitOririnal]]
  return resultado
