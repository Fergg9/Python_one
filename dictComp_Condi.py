'''import random
countries = ['gt', 'nic', 'cr']

population = {country: random.randint(1, 100)
for country in countries}
print(population)

result2 = {country: population for (country, population) in population.items() if population > 50}
print(result2)

text = 'Hola, si soy una mierda'
unique = {c: text.count(c) for c in text if c in 'aeiou'}
print(unique)'''

def message_creator(text):
   # Escribe tu solución 👇

   respuestas = {'computadora' : "Con mi computadora puedo programar usando Python", 
                    'celular' : "En mi celular puedo aprender usando la app de Platzi",
                    'cable' : "¡Hay un cable en mi bota!"}

   if text in respuestas.keys(): 
      print(respuestas['cable'])
      return respuestas[text]
   else: 
      return 'Artículo no encontrado'

text = 'celular'
response = message_creator(text)
print(response)