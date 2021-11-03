# esse arquivo apenas inicializa as função para gerar e preencher a malha,
# inicializar o robô e gerar a população inicial

import malha as ma
import robo as ro

def preencheMalha(tamanhoMalha):
  malha = ma.criaMalha(tamanhoMalha)
  latas = ma.preencheMalha(malha)
  
  return (malha, latas)

def inicializaRobo():
  return ro.Robo()

def geraPopulacao(robo, latas, malha):
  cromossomo1 = robo.coletaLatas(latas, malha)
  cromossomo2 = robo.coletaLatas2(latas, malha)
  cromossomo3 = robo.coletaLatas3(latas, malha)
  cromossomo4 = robo.coletaLatas4(latas, malha)
  
  return [cromossomo1, cromossomo2, cromossomo3, cromossomo4]