'''
Created on Jun 30, 2024

@author: shadowmons
'''
 
def vectores():
     #Listas - Vectores
    vector = [1,2,3,4,5,6,7]
    print("Este es un vector ", vector)
    print(type(vector))
    dias = ['lunes','sabado','miercoles','domingo']
    print('vector de dias: ', dias)
    mixed=[1,'2','hola',True]
    print('Este es un vector de tipos mixtos: ', mixed)
    #Inspeccionar elementos de una lista, no una matriz
    print(dias[0][0:4])
    #el elemento 0 es lunes, y el string funciona, en cierta parte, como una lista
    #Los elementos de un String no se pueden modificar por asignacion de valor, pero en una lista si
    # texto[0] = 'f' (si texto es un string, no se puede)
    dias[0]='viernes'
    #Algunos metodos de listas son validos para string
    print(vector[:2]) 
    print(True in mixed)
    print(False in mixed)
    
def crud():
    #CRUD create, read, update, delete
    num = [1,2,3,4,5,6,7,10]
    print(num)
    num[-1]=8
    print(num)
    #agrega este elemento a la lista
    num.append(9)
    print(num)
    #inserta en el index indicado el elemento
    num.insert(0,0)
    print(num)
    num2 = num
    print(num2)
    num2 = [10,11,12,13]
    #concatena lista
    newlist = num + num2
    print(newlist)
    pos = newlist.index(8)
    newlist[pos]= 234
    print(newlist)
    #remove elimina un objeto determinado, tiene parametro de entrada
    newlist.remove(234)
    print(newlist)
    #pop elimina el ultimo elemento, si le paso el indice va a eliminar el element de la posicion
    newlist.pop()
    print(newlist)
    newlist.pop(-2)
    newlist.pop(0)
    print(newlist)
    #invierte lista y ordenar
    newlist.reverse()
    print(newlist)
    newlist.insert(4,23)
    newlist.insert(5,433)
    print(newlist)
    newlist.sort()
    print(newlist) 
    #ordenar con string
    abc = ['hola','aire','odio','luna','pera','gota']
    print(abc)
    abc.sort()
    print(abc)
    #No se puede ordenar un array de tipos mezclados con sort
    
def tuplas():
    #Tuplas se crean con parentesis
    numeros = (1,2,3,5)
    palabra = ('hola','amor','odio','paja')
    print(numeros)
    print(palabra)
    print(type(palabra))
    #acceder a tuplas por indice
    print(numeros[2])
    #las tuplas son inmutables, solo lectura
    #busqueda
    print(palabra.index('odio'))
    print(palabra.count('amor'))
    
    #puedo hacer transformaciones
    lista = list(palabra)
    print(type(lista))
    lista.append('neta')
    tupla = tuple(lista)
    print(tupla)
    print(type(tupla))
    
def diccionario():       
    #Diccionarios
    mydic = {'name':'pajaro metalico',
             'marca': 'la hora',
             'modelo':'de revista'
             }
    print(type(mydic))
    print(mydic)
    print(mydic['modelo'])
    print(mydic.get('modelo'))
    #la diferencia entre ambos metodos de arriba es que el primero
    #puede dar error y el get puede manejar errores (result none)
    print('marca' in mydic)
    print('color' in mydic)
    #otra forma de prevenir errores
    #para agregar un elemento al dic
    mydic['color']= 'de tus ojos'
    print(mydic)
    
    persona = {
        'name':'Victor',
        'last_name':'Gil',
        'langs':['java','python'],
        'age':27}
    
    print(persona)
    #modificar el diccionario
    persona['name']='Angel'
    persona['age']=30
    persona['langs'].append('C')
    print(persona)
    #eliminar
    del persona['last_name']
    #en diccionarios obligatioriamente se debe pasar el valor a pop
    persona.pop('age')
    print(persona)
    
    #items (devuelve un array de tuplas, pares clave valor)
    print('items: ', persona.items())
    
    #keys retorna una lista con las claves
    print('keys> ', persona.keys())
    
    #values retorna una lista con los valores
    print('values> ', persona.values())
    
    # lista de eso = list(persona.items())
    """
    Agregar un nuevo elemento al diccionario con la llave "twitter" y el valor "@nicobytes".
    Actualizar el valor del elemento con la llave "name" con el valor "Felipe".
    Eliminar el elemento del diccionario con la llave "age".
    Imprimir una lista con las llaves del diccionario.
    Imprimir una lista con los valores del diccionario.
    """
    
    def ciclos():
        #ciclos
        #mientras la condicion sea True siempre se va a ejecutar
        """
        if False:
            while True:
                print("Esto sera infinito")
                """
                
        con = 0
                
        while con < 10:
            print(con)
            con+=1
            
        con = 0
        
        #usar el break para joder un ciclo
        while con < 20:
            print(con)
            con +=3
            if con>15:
                print('Te jodiste')
                break
            
        #usar el continue
        #hace que todo lo que resta en un ciclo no se ejecute
        #hablando de lineas de codigo
        con = 0
        while con < 20:
            con +=1
            if con<15:
                continue 
            print(con)
            print("cono mira como funciona")
            
        #Ciclo For
        print("##"*23)
        
        for i in range(5):
            print(i)
            
        lista = [23,43,54,65,76]
        for i in lista:
            print(i)
            
        tupla = (1,4,7,"fr",'rfr')
        for i in tupla:
            print(i)
            
        dic = {'name':'jose',
               'age': 23,
               'hei':194}
        
        for i in dic:
            #itera las keys
            print(i, dic[i])
        
        #lo mismo que arriba pero mejor
        for i, j in dic.items():
            print(i,j)
            
        #prueba con lista de diccionarios
        personas = [
            {
                'name':'jose',
               'age': 23,
               'hei':194
                },
            {
                'name':'juan',
               'age': 24,
               'hei':184
                },
            {
                'name':'vict',
               'age': 34,
               'hei':179
                }
            ]
        for i in personas:
            print(i)
            print('nombre', i['name'])
            
        matriz = [
            [1,2,3], [4,5,6], [7,8,9]]
        print(matriz[0][1])
        
        for i in matriz:
            print(i)
            for j in i:
                print(j)
                
    def miscelaneos():
        #Variables
        nombre = "Victor"
        #nombre = input("Cual es tu nombre?: ")
        #print("tu puto nombre es", nombre)
        #Edad = input('Y cual es tu mmgva edad?')
        #print("El gallo tiene", Edad)
        # Las variables aqui no tienen que ser declaradas, osea los tipos de variables, interesante
        print("A ver", nombre)
        print(12 + 35)
        print(12 - 35)
        print(12 * 35)
        # adadadadasd
        
        #String
        
        string = "cadena"
        print(type(string) )
        
        apellido = "Gil"
        nombre_completo = nombre + " " + apellido
        
        palabra = "Su madre como uso apostrofe I'm "
        print(palabra)
        # si quiero usar un apostrofe o una comilla doble
        #usa la contraria para abrir y cerrar
        
        #Formato 
        
        template = "hola mmgvo el nomnbre es " + nombre + " y el pendejo es "   + apellido
        print(template)
        template = "hola mmgvo el nomnbre es {} y el pendejo es {}".format(nombre, apellido)
        print(template)
        
        template = f"a ver mmgvo {nombre} tu apellido es {apellido}"
        print(template *4)
        
        #int
        
        numero = 23
        print(numero)
        print(type(numero))
        
        flotante = 2.45
        print(flotante)
        print(type(flotante))
        grandee = 454500000000000000000.01
        print(grandee)
        
        
        #booleanos
        
        boleano = True
        print(boleano)
        print(type(boleano))
        
        print(not boleano)
        
        #transformacion para concatenar diferentes tipos de tu sabes
        print("el numero que escogiste es" + str(numero))
        print(f"Mi edad es {numero}")
        
        numero2 = "43"
        numero2 = int(numero2)
        
        # + - * / residuo es %, division entera es //, el de elevado es **
        #parentesis, exponente, multi, dipli, ad, rest
        
        print(344//56)
        print(344%56)
        print(2**3)
        
        #comparacion <  >  >=   <=  == estrictamente de igualdad  != de diferencia
        print(33>5)
        print(234<23)
        print(2432>=4)
        print(232<=232)
        print(2342!=34)
        print("ff" == "ff")
        print("ff" == "fF")
        print('2' == 2)
        
        
        #comparando float que normalmente es un dolor de huevos
        #usar string para el formato
        x = 3.3
        y = 1.1 + 2.2584
        print(x)
        print(y)
        print(x==y)
        
        ys = format(y, ".2g")
        print(ys)
        ys = format(y, ".3g")
        print(ys)
        ys = format(y, ".4g")
        print(ys)
        
        y = 1.1 + 2.2
        
        print("*" * 34)
        
        tolerancia = 0.000001
        
        print(abs(x-y) < tolerancia)
        
        #operadores logicos and or y esa paja
        #pana ya te sabes eso, de pana que si se te olvido te sale sendo lepe
        
        print('evaluando AND', True and False)
        print('evaluando OR', True or False)
        print('evaluando not', not True or False)
        print('evaluando nand', not(True and False))
        
        #Condicionales
        
        if True:
            print('asi se hace esta mierda')
            
        if False:
            print("esto no debe imprimirse mmgvo")
        else:
            print("aqui si debe entrar jajajajaajuuuuuuu")
        
        #Formato if (se verifica que sea true) :
        if (True or False) and 100>50:
            print('rememorando mmgvo')
            
        mascota = 'perro'
        
        if mascota == 'perro':
            print('asi se HACE PERRO')
        elif mascota == 'gato':
            print('asi se HACE GATO')
        elif mascota == 'pez':
            print('que mal gusto mmgvo')
        else:
            print('lo que sea') 
        from random import random
            
        
        #numero_computer = int (format(random * 3, ".1g"))
        
        
        texto = 'Vamos a ver si esto esta tan Bueno Como Parece'
        
        print('vamos' in texto)
        print(len(texto))
        print(texto.upper())
        print(texto.lower())
        print(texto.count('e'))
        print(texto.swapcase())
        print(texto.startswith('error'))
        print(texto.endswith('Parece'))
        print(texto.replace('Parece', 'Suena'))
        
        texto2 = 'esto es una prueba'
        print(texto2.capitalize())
        print(texto2.title())
        print(texto2.isdigit())
        print('45'.isdigit())
        print('45.5'.isdigit())
        print('554'.isdecimal())
        print("%"*15)
        #indexing y slicing
        text = "Ella sabe Python"
        print(text[6])
        #la longitud se puede desbordar porque los indices empiezan en 0
        print(text[len(text)-1])
        print(text[-1])
        print(text[len(text)-1] == text[-1])
        #si hago con numeros negativos hace el conteo desde el final del string hacia el inicio
        
        #slicing
        print(text[0:10])
        print(text[:10])
        #si no se especifica el primer indice toma 0 como defecto
        print(text[-6:len(text)])
        print(text[5:])
        #lo mismo ocurre con el final
        print(text[:])#es valido, pero estupido
        print(text[10:16:1])
        print(text[10:16:2])
        print(text[10:16:3])
        #define los saltos
        escrito = "Vamos a ver si se puede entender lo que escribi"
        print(escrito[::2])
