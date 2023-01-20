user_option = input('Piedra, papel o tijera: ')
user_option = user_option.lower()
pc_option = 'papel'

if user_option == pc_option:
    print('empate')
elif user_option == 'tijera':
    if pc_option == 'papel':
        print('tijera le gana a papel')
        print('Usuario gana')
    else: 
        print('piedra le gana a tijera')
        print('la pc gano')
        
elif user_option == 'piedra':
    if pc_option == 'tijera':
        print('piedra le gana a tijera')
    else:
        print('Papel le gana a piedra')    
        print('la pc gano')   
    
elif user_option == 'papel':
    if pc_option == 'piedra':
        print('papel le gana  a piedra')
        print('Gano el usuario')
    else:
        print('tijera le gana a papel')
        print('Pc gano')    
                     