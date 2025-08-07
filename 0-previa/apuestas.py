import random
import numpy as np

def dinero_final(capital_inicial, porc_a_cara):
  capital_actual = capital_inicial
  for _ in range(1000):
    tirada = random.randint(0,1)
    if tirada == 1:
      capital_actual = 3 * capital_actual * porc_a_cara
    else:
      capital_actual = 1.2 * capital_actual * (1 - porc_a_cara)
  return capital_actual

dict_ganancias = {}
capital_inicial = 1_000_000
max = 0
for porcentaje in np.linspace(0,1,11):
  final =  dinero_final(capital_inicial, porcentaje)
  dict_ganancias[porcentaje] = final
  if final > max:
    max = final
    mejor_porc = porcentaje
print(dict_ganancias)
print(mejor_porc, max)