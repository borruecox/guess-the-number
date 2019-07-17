 # Este es el juego de adivinar el número.
import random

print('¡Hola! ¿Cómo te llamas?')
miNombre = input()

def Menu():
    print ("""************
Nivel de dificultad:
************
Menu
1) Noob 1 de 2
2) Normal 1 de 100
3) Dificil 1 de 1000
4) Imposible 1 de 1000000
5) Solo lo puede saber carla ya que es una diosa griega 1 de 10000000
6) Salir""")

def Juego():
    Menu()
    opc = int(input("Selecione Opcion\n"))
    if (opc==1):
        número = random.randint(1, 2)
        print('Bueno, ' + miNombre + ', estoy pensando en un número entre 1 y 2.')
        intentosRealizados = 0

        while intentosRealizados < 3:
            print('Intenta adivinar.') 
            estimación = input()
            estimación = int(estimación)

            intentosRealizados = intentosRealizados + 1

            if estimación < número:
                print('Tu estimación es muy baja.') 

            if estimación > número:
                print('Tu estimación es muy alta.')

            if estimación == número:
                break

        if estimación == número:
            intentosRealizados = str(intentosRealizados)
            print('Correcto, ' + miNombre + '. Has adivinado mi número en ' + intentosRealizados + ' intentos. Pero eso no quita que sigas en el nivel de los tontos :-)')

        if estimación != número:
            número = str(número)
            print('Tu eres mu tonto. El número que estaba pensando era ' + número)
        
    elif(opc==2):
        número = random.randint(1, 100)
        print('Bueno, ' + miNombre + ', estoy pensando en un número entre 1 y 100.')
        intentosRealizados = 0
        
        while intentosRealizados < 10:
            print('Intenta adivinar.') 
            estimación = input()
            estimación = int(estimación)

            intentosRealizados = intentosRealizados + 1

            if estimación < número:
                print('Tu estimación es muy baja.') 

            if estimación > número:
                print('Tu estimación es muy alta.')

            if estimación == número:
                break

        if estimación == número:
            intentosRealizados = str(intentosRealizados)
            print('¡Buen trabajo, ' + miNombre + '! ¡Has adivinado mi número en ' + intentosRealizados + ' intentos!')

        if estimación != número:
            número = str(número)
            print('Pues no. El número que estaba pensando era ' + número)        
    elif(opc==3):
        número = random.randint(1, 1000)
        print('Bueno, ' + miNombre + ', estoy pensando en un número entre 1 y 1000.')
        intentosRealizados = 0
        
        while intentosRealizados < 15:
            print('Intenta adivinar.') 
            estimación = input()
            estimación = int(estimación)

            intentosRealizados = intentosRealizados + 1

            if estimación < número:
                print('Tu estimación es muy baja.') 

            if estimación > número:
                print('Tu estimación es muy alta.')

            if estimación == número:
                break

        if estimación == número:
            intentosRealizados = str(intentosRealizados)
            print('¡Buen trabajo, ' + miNombre + '! ¡Has adivinado mi número en ' + intentosRealizados + ' intentos!')

        if estimación != número:
            número = str(número)
            print('Pues no. El número que estaba pensando era ' + número)        
    elif(opc==4):
        número = random.randint(1, 1000000)
        print('Bueno, ' + miNombre + ', estoy pensando en un número entre 1 y 1000000.')
        intentosRealizados = 0
        
        while intentosRealizados < 20:
            print('Intenta adivinar.') 
            estimación = input()
            estimación = int(estimación)

            intentosRealizados = intentosRealizados + 1

            if estimación < número:
                print('Tu estimación es muy baja.') 

            if estimación > número:
                print('Tu estimación es muy alta.')

            if estimación == número:
                break

        if estimación == número:
            intentosRealizados = str(intentosRealizados)
            print('¡Buen trabajo, ' + miNombre + '! ¡Has adivinado mi número en ' + intentosRealizados + ' intentos!')

        if estimación != número:
            número = str(número)
            print('Pues no. El número que estaba pensando era ' + número)        
    elif(opc==5):
        número = random.randint(1, 10000000)
        print('Bueno, ' + miNombre + ', estoy pensando en un número entre 1 y 10000000.')
        intentosRealizados = 0
        
        while intentosRealizados < 25:
            print('Intenta adivinar.') 
            estimación = input()
            estimación = int(estimación)

            intentosRealizados = intentosRealizados + 1

            if estimación < número:
                print('Tu estimación es muy baja.') 

            if estimación > número:
                print('Tu estimación es muy alta.')

            if estimación == número:
                break

        if estimación == número:
            intentosRealizados = str(intentosRealizados)
            print('¡Buen trabajo, ' + miNombre + '! ¡Has adivinado mi número en ' + intentosRealizados + ' intentos!')

        if estimación != número:
            número = str(número)
            print('Pues no. El número que estaba pensando era ' + número)        
Juego()
