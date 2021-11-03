import SSGA
import inicializaFuncoes
from time import sleep

tamanhoDaMalha = int(input(f'\nDigite quantas linhas e quantas colunas a malha deve ter: '))
numeroGeracoes = int(input('Digite o número de gerações desejado: '))
pc = float(input('Digite a taxa de crossover desejada (ex: 0.4, 0.7, etc): '))
pm = float(input('Digite a taxa de mutação desejada (ex: 0.4, 0.7, etc): '))

(malha, latas) = inicializaFuncoes.preencheMalha(tamanhoDaMalha)
print(f'\nMalha com as latas: {malha}')
sleep(1.2)
print(f'\nPosições das latas: {latas}')

sleep(1.2)

robo = inicializaFuncoes.inicializaRobo()
populacao = inicializaFuncoes.geraPopulacao(robo, latas, malha)
resultados = SSGA.rodaAG(populacao, numeroGeracoes, pc, pm, latas, malha, robo)

print(f'\nQuantidade de latas restantes na malha: {resultados[0]}')
print(f'\nDireções do robô: {resultados[1]}')
print(f'Número de passos para pegar todas as latas antes do AG: {resultados[3]}')
print(f'Número de passos para pegar todas as latas depois do AG: {resultados[2]}\n')
