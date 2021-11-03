from copy import deepcopy

class Robo:

  # inicializa o robô com a posição (0,0)
  def __init__(self):
    self.linha = 0
    self.coluna = 0
        
  # essa função faz com que o robô colete todas as latas da malha e retorne um vetor de direções pelo qual ele passou
  def coletaLatas(self, latas, malha):
    # vetor que irá armazenar as direções que o robô tomou na malha, com as seguintes
    # possibilidades Direita (D), Esquerda (E), Cima (C) e Baixo (B)
    direcoes = []
    malha2 = deepcopy(malha)
    posicaoAnterior = (0, 0) # variável que armazena a posição anterior do robô
    qtdDeLatas = len(latas) # variável que armazena a quantidade de latas
    
    # percorre todo o vetor das posições das latas
    for lata in latas:
      
      # enquanto dura até o robô encontrar a lata da iteração
      while True:
        
        if qtdDeLatas == 0: # se encontrou todas as latas então retorna as direções
          self.linha = 0
          self.coluna = 0
          return direcoes
        
        if (lata[0], lata[1]) == (self.linha, self.coluna): # robô encontrou a lata
          malha2[self.linha][self.coluna] = 1 # atualiza a posição da malha tirando a lata
          qtdDeLatas -= 1 # decrementa 1 lata
          break
        
        # verifica se a lata está à direita do robô, se o robô não está em uma
        # das paredes e se o robô dando um movimento à direita não anula seu último movimento
        # se todas as verificações forem verdadeiras então o robô andará para a direita
        if (self.coluna <= lata[1]) and (self.coluna != (len(malha2) - 1)) and (
        (self.linha, self.coluna+1) != posicaoAnterior):
          posicaoAnterior = (self.linha, self.coluna) # a posição anterior será a posição atual do robô
          direcoes.append('D') # o movimento à direita é colocado no vetor de direções
          self.coluna += 1 # aqui o robô efetivamente caminha na malha à direita
        
        # verifica se a lata está à esquerda do robô, se o robô não está em uma
        # das paredes e se o robô dando um movimento à esquerda não anula seu último movimento
        # se todas as verificações forem verdadeiras então o robô andará para a esquerda
        elif (self.coluna >= lata[1]) and (self.coluna != 0) and (
        (self.linha, self.coluna-1) != posicaoAnterior):
          posicaoAnterior = (self.linha, self.coluna)
          direcoes.append('E') # o movimento à esquerda é colocado no vetor de direções
          self.coluna -= 1 # aqui o robô efetivamente caminha na malha à esquerda
        
        # verifica se a lata está em uma linha abaixo do robô, se o robô não está em uma
        # das paredes e se o robô dando um movimento para baixo não anula seu último movimento
        # se todas as verificações forem verdadeiras então o robô se movimentará para baixo
        elif (self.linha <= lata[0]) and (self.linha != (len(malha2) - 1)) and (
        (self.linha+1, self.coluna) != posicaoAnterior):
          posicaoAnterior = (self.linha, self.coluna)
          direcoes.append('B') # o movimento para baixo é colocado no vetor de direções
          self.linha += 1 # aqui o robô efetivamente caminha na malha para baixo
        
        # verifica se a lata está em uma linha acima do robô, se o robô não está em uma
        # das paredes e se o robô dando um movimento para cima não anula seu último movimento
        # se todas as verificações forem verdadeiras então o robô se movimentará para cima  
        elif (self.linha >= lata[0]) and (self.linha != 0) and (
        (self.linha-1, self.coluna) != posicaoAnterior):
          posicaoAnterior = (self.linha, self.coluna)
          direcoes.append('C') # o movimento para cima é colocado no vetor de direções
          self.linha -= 1 # aqui o robô efetivamente caminha na malha para cima
    
    # seta o robô para a posição (0,0)   
    self.linha = 0
    self.coluna = 0
    return direcoes
  
  # as funções coletaLatas2, coletaLatas3 e coletaLatas4 são basicamente iguais a
  # função coletaLatas, a diferença está em quais direções o robô caminhará primeiro
  
  def coletaLatas2(self, latas, malha):
    direcoes = []
    malha2 = deepcopy(malha)
    posicaoAnterior = (0, 0)
    qtdDeLatas = len(latas)
    
    for lata in latas:
      while True:
        
        if qtdDeLatas == 0:
          self.linha = 0
          self.coluna = 0
          return direcoes
        
        if (lata[0], lata[1]) == (self.linha, self.coluna):
          malha2[self.linha][self.coluna] = 1
          qtdDeLatas -= 1
          break
          
        if (self.linha <= lata[0]) and (self.linha != (len(malha2) - 1)) and (
        (self.linha+1, self.coluna) != posicaoAnterior):
          posicaoAnterior = (self.linha, self.coluna)
          direcoes.append('B')
          self.linha += 1
          
        elif (self.linha >= lata[0]) and (self.linha != 0) and (
        (self.linha-1, self.coluna) != posicaoAnterior):
          posicaoAnterior = (self.linha, self.coluna)
          direcoes.append('C')
          self.linha -= 1
          
        elif (self.coluna <= lata[1]) and (self.coluna != (len(malha2) - 1)) and (
        (self.linha, self.coluna+1) != posicaoAnterior):
          posicaoAnterior = (self.linha, self.coluna)
          direcoes.append('D')
          self.coluna += 1
          
        elif (self.coluna >= lata[1]) and (self.coluna != 0) and (
        (self.linha, self.coluna-1) != posicaoAnterior):
          posicaoAnterior = (self.linha, self.coluna)
          direcoes.append('E')
          self.coluna -= 1
        
    self.linha = 0
    self.coluna = 0
    return direcoes
  
  def coletaLatas3(self, latas, malha):
    direcoes = []
    malha2 = deepcopy(malha)
    posicaoAnterior = (0, 0)
    qtdDeLatas = len(latas)
    
    for lata in latas:
      while True:
        
        if qtdDeLatas == 0:
          self.linha = 0
          self.coluna = 0
          return direcoes
        
        if (lata[0], lata[1]) == (self.linha, self.coluna):
          malha2[self.linha][self.coluna] = 1
          qtdDeLatas -= 1
          break
        
        if (self.linha >= lata[0]) and (self.linha != 0) and (
        (self.linha-1, self.coluna) != posicaoAnterior):
          posicaoAnterior = (self.linha, self.coluna)
          direcoes.append('C')
          self.linha -= 1
          
        elif (self.coluna <= lata[1]) and (self.coluna != (len(malha2) - 1)) and (
        (self.linha, self.coluna+1) != posicaoAnterior):
          posicaoAnterior = (self.linha, self.coluna)
          direcoes.append('D')
          self.coluna += 1
          
        elif (self.coluna >= lata[1]) and (self.coluna != 0) and (
        (self.linha, self.coluna-1) != posicaoAnterior):
          posicaoAnterior = (self.linha, self.coluna)
          direcoes.append('E')
          self.coluna -= 1
        
        elif (self.linha <= lata[0]) and (self.linha != (len(malha2) - 1)) and (
        (self.linha+1, self.coluna) != posicaoAnterior):
          posicaoAnterior = (self.linha, self.coluna)
          direcoes.append('B')
          self.linha += 1
        
    self.linha = 0
    self.coluna = 0
    return direcoes
  
  def coletaLatas4(self, latas, malha):
    direcoes = []
    malha2 = deepcopy(malha)
    posicaoAnterior = (0, 0)
    qtdDeLatas = len(latas)
    
    for lata in latas:
      while True:
        
        if qtdDeLatas == 0:
          self.linha = 0
          self.coluna = 0
          return direcoes
        
        if (lata[0], lata[1]) == (self.linha, self.coluna):
          malha2[self.linha][self.coluna] = 1
          qtdDeLatas -= 1
          break
          
        if (self.coluna >= lata[1]) and (self.coluna != 0) and (
        (self.linha, self.coluna-1) != posicaoAnterior):
          posicaoAnterior = (self.linha, self.coluna)
          direcoes.append('E')
          self.coluna -= 1
          
        elif (self.linha <= lata[0]) and (self.linha != (len(malha2) - 1)) and (
        (self.linha+1, self.coluna) != posicaoAnterior):
          posicaoAnterior = (self.linha, self.coluna)
          direcoes.append('B')
          self.linha += 1
          
        elif (self.coluna <= lata[1]) and (self.coluna != (len(malha2) - 1)) and (
        (self.linha, self.coluna+1) != posicaoAnterior):
          posicaoAnterior = (self.linha, self.coluna)
          direcoes.append('D')
          self.coluna += 1
          
        elif (self.linha >= lata[0]) and (self.linha != 0) and (
        (self.linha-1, self.coluna) != posicaoAnterior):
          posicaoAnterior = (self.linha, self.coluna)
          direcoes.append('C')
          self.linha -= 1
        
    self.linha = 0
    self.coluna = 0
    return direcoes
  
  # a função objetivo recebe um vetor de direções e movimenta o robô na malha
  # coletando as latas por onde ele passar
  def funcObjetivo(self, latas, malha, direcoes):
    # seta o robô para a posição (0,0)
    self.linha = 0
    self.coluna = 0
    malha2 = deepcopy(malha)
    qtdDeLatas = len(latas)
    posicaoAnterior = (0, 0)
    direcoes2 = [] # vetor que armazena as direções por onde o robô passou
    
    # percorre todo o vetor das direções
    for direcao in direcoes:
      
      # se recolheu todas as latas então a função é finalizada
      if qtdDeLatas == 0:
        return (malha2, qtdDeLatas, direcoes2)
      
      # verifica se a direção lida é direita, se o robô não está em uma
      # das paredes e se o robô dando um movimento à direita não anula seu último movimento
      # se todas as verificações forem verdadeiras então o robô andará para a direita 
      if direcao == 'D' and (self.coluna != (len(malha2) - 1)) and (
        (self.linha, self.coluna+1) != posicaoAnterior):
        posicaoAnterior = (self.linha, self.coluna)
        self.coluna += 1
        direcoes2.append('D')
      
      # verifica se a direção lida é esquerda, se o robô não está em uma
      # das paredes e se o robô dando um movimento à esquerda não anula seu último movimento
      # se todas as verificações forem verdadeiras então o robô andará para a esquerda
      if direcao == 'E' and (self.coluna != 0) and (
        (self.linha, self.coluna-1) != posicaoAnterior):
        posicaoAnterior = (self.linha, self.coluna)
        self.coluna -= 1
        direcoes2.append('E')
      
      # verifica se a direção lida é baixo, se o robô não está em uma
      # das paredes e se o robô dando um movimento para baixo não anula seu último movimento
      # se todas as verificações forem verdadeiras então o robô se movimentará para baixo
      if direcao == 'B' and (self.linha != (len(malha2) - 1)) and (
        (self.linha+1, self.coluna) != posicaoAnterior):
        posicaoAnterior = (self.linha, self.coluna)
        self.linha += 1
        direcoes2.append('B')
      
      # verifica se a direção lida é cima, se o robô não está em uma
      # das paredes e se o robô dando um movimento para cima não anula seu último movimento
      # se todas as verificações forem verdadeiras então o robô se movimentará para cima  
      if direcao == 'C' and (self.linha != 0) and (
        (self.linha-1, self.coluna) != posicaoAnterior):
        posicaoAnterior = (self.linha, self.coluna)
        self.linha -= 1
        direcoes2.append('C')      
      
      # verifica se há uma lata na atual posição do robô, se estive ele irá coletá-la
      if malha2[self.linha][self.coluna] == 'lata':
        malha2[self.linha][self.coluna] = 1
        qtdDeLatas -= 1
    
    return (malha2, qtdDeLatas, direcoes2) # retorna a malha, a quantidade de latas restantes na malha e o vetor de direções que o robô caminhou
    