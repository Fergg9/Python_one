centroamerica_set = {'Gt', 'Hon', 'Nic', 'Cr', 'Pnm', 'Eslv', 'Can'}
concacaf_set = {'Gt', 'Hon', 'Nic', 'Cr', 'Pnm', 'Eslv', 'Usa', 'Can', 'Mx'}

union = centroamerica_set | concacaf_set
print(union)

intersection = centroamerica_set & concacaf_set
print(intersection)

difference = centroamerica_set - concacaf_set
#resta un set a otro
print(f' diferencia {difference}')

assymetric_difference = centroamerica_set ^ concacaf_set
#La diferencia simetrica entre dos conjutnos consta de restar todos los elementos de ambos exceptuando el elemento en común.
print(assymetric_difference)