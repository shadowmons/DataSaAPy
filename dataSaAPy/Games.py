import random

class JuegoPPT:
    
    def __init__(self):
        print('')
    def ronda(self):
        
        opciones = ('piedra', 'papel','tijera')
        con = 1
        
        while True:
            print("*"*25)
            print('Ronda', con)
            print("*"*25)
            Opcion_user = input("Elija piedra, papel o tijera: ")
            Opcion_user.lower()
            
            #Opcion_user = random.choice(opciones)
            Opcion_comp = random.choice(opciones)
            if not Opcion_user in opciones:
                print('opcion no valida')
                continue
                
            con += 1
            print(f'La opcion del jugador es {Opcion_user} y la de la pc es {Opcion_comp}')
            salida = 'Error'
            
            if Opcion_comp == Opcion_user:
                salida= 'Empate'
            elif Opcion_comp == 'piedra':
                if Opcion_user == 'tijera':
                    salida = 'Perdiste'
                else:
                    salida = 'ganaste'
            elif Opcion_comp == 'tijera':     
                if Opcion_user == 'papel':
                    salida = 'Perdiste'
                else:
                    salida = 'ganaste'  
            else:
                if Opcion_user == 'piedra':
                    salida = 'Perdiste'
                else:
                    salida = 'ganaste'
                
            print(salida)

        
        