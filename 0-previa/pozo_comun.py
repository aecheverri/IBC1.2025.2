import random
import numpy as np

def dinero_final(capital_inicial, porc_a_cara):
  capital_actual = capital_inicial
  tirada = random.randint(0,1)
  if tirada == 1:
    capital_actual = 3 * capital_actual * porc_a_cara
  else:
    capital_actual = 1.2 * capital_actual * (1 - porc_a_cara)
  return capital_actual


capitales_iniciales = np.full(101,1)
pozo = 0
print(capitales_iniciales)
for jugada in range(1000):
  pozo = 0
  for capital in capitales_iniciales:
    pozo +=  dinero_final(capital, 0.5)
  capitales_iniciales = np.full(len(capitales_iniciales), pozo / len(capitales_iniciales) )
  print(f'Jugada {jugada + 1}')
  print(capitales_iniciales)