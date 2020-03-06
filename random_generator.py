#!/usr/bin/env python3.6

#english:
#####################################################################################
# simple pseudo random number generator function
#####################################################################################
#this function generates a pseudo random inside a given range, a seed needs to be provided
#in the example current time is used to generate the seed, if the same number is used the generated random will be the same so as somewhat random seed should be used, using time is the usual method
#the resulting number is a floating point integer, use round() if a integer is necessary

def Random_gen( min, max, seed):
 number = ((134775813 * seed + 2147483587) % 134456) #this is the random generation calculation the constants where chosen from common examples
 return (number / 134456) * (max - min) + min #this is the calculation that adjust the generated number into the given range
#return round((number / 134456) * (max - min) + min, 0) #using round to get an integer

#single line lambda pseudo random number generator
#lambda_gen1 = lambda min, max, seed: (((134775813 * seed + 2147483587) % 134456) / 134456) * (max - min) + min
#and with round
#lambda_gen2 = lambda min, max, seed: round((((((134775813 * seed + 2147483587) % 134456) / 134456) * (max - min) + min) / 134456) * (max - min) + min, 0)

#example
import time

min, max = -3, 15
number = Random_gen(min, max,  int(round(time.time() * 1000)))
for i in range(0, 10):
 print(number)
 number = Random_gen(min, max, number)

#####################################################################################
#this fuction implements a linear congruential generator (LCG), the basic equation is
#xn+1 = ( a * Xn + c ) mod m
#number = ( multiplier * seed + increment ) % modulus

#----------------------------------------------------------------------------------------------------------------------------------------------

#portugues:
#####################################################################################
#funcao simples para a geracao de numeros pseudo aleatorios
#####################################################################################
#esta funcao gera numeros pseudo aleatorios dentro de um intervalo, uma seed precisa ser passada, se a mesma seed(semente) for usada o numero gerado sera o sempre mesmo
#no exemplo o tempo atual e usado para gerar a seed
#o numero resultante desta funcao e um inteiro de ponto flutuante, ou seja um float, use round() se precisar de um inteiro

def Random_gerador( menor, maior, seed):
 numero = ((134775813 * seed + 2147483587) % 134456) #este e o calculo que gera o numero aleatorio, as constantes usadas sao valores comuns a outros geradores
 return (numero / 134456) * (maior - menor) + menor #este e o calculo que ajusta o numero gerado para o intervalo definido
#return (((134775813 * seed + 2147483587) % 134456) / 134456) * (max - min) + min #este e um exemplo de como fazer toda a funcao ter uma unica linha
#return round((number / 134456) * (max - min) + min, 0) #este e um exemplo do uso do round() para remover a parte decimal

#função lambda para geração de numeros pseudo aleatorios em uma unica linha
#l1 = lambda menor, maior, seed: (((134775813 * seed + 2147483587) % 134456) / 134456) * (maior - menor) + menor
#e usando round
#l2 = lambda menor, maior, seed: round((((((134775813 * seed + 2147483587) % 134456) / 134456) * (maior - menor) + menor) / 134456) * (maior - menor) + menor, 0)

#exemplo
import time

menor, maior = -3, 15
numero = Random_gerador(menor, maior,  int(round(time.time() * 1000)))
for i in range(0, 10):
 print(numero)
 numero = Random_gerador(menor, maior, numero)

#####################################################################################
#esta função implementa um gerador congruencial linear (inglês: Linear Congruential Generator) de sigla LCG, a equacao basica e:
#xn+1 = ( a * Xn + c ) mod m
#numero = ( multiplicador * seed + incremento ) % modulo
