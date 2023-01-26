def message_creator(text):
   # Escribe tu solución 👇

   respuestas = {'computadora' : "Con mi computadora puedo programar usando Python", 
                    'celular' : "En mi celular puedo aprender usando la app de Platzi",
                    'cable' : "¡Hay un cable en mi bota!"}

   if text in respuestas.keys(): 
      return respuestas[text]
   else: 
      return 'Artículo no encontrado'

text = 'celular'
response = message_creator(text)
print(response)

def sum_in_range(min, max):
    print(min, max)
    sum = 0
    for x in range(min, max):
      sum += x
    print(f'la suma entre el rango {min, max} es: {sum}')  

sum_in_range(1, 900) 
