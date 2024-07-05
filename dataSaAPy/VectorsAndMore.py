'''
Created on Jun 30, 2024

@author: shadowmons
'''
from gi._gi import new
 
def vectores():
    #Listas - Vectores
    print('Vectores/Listas \n',30*"*")
    #specifie vector with brackets
    vector = [1,2,3,4,5,6,7]
    print("Este es un vector ", vector)
    print(type(vector))
    dias = ['lunes','sabado','miercoles','domingo']
    print('vector de dias: ', dias)
    mixed=[1,'2','hola',True]
    print('Este es un vector de tipos mixtos: ', mixed)
    #Inspeccion of one element of the list, it works like in strings
    print(dias[0][0:4])
    #el elemento 0 es lunes, y el string funciona, en cierta parte, como una lista
    #Los elementos de un String no se pueden modificar por asignacion de valor, pero en una lista si
    # texto[0] = 'f' (si texto es un string, no se puede)
    dias[0]='viernes'
    #Algunos metodos de listas son validos para string
    print(vector[:2]) 
    print(True in mixed)
    print(False in mixed)
    #Nested List
    vector = [[1,2,3],[2,4,5],[4,2,5]]
    print(vector)
    
    
def crud():
    #CRUD create, read, update, delete
    print('CRUD create, read, update, delete\n',30*"*")
    num = [1,2,3,4,5,6,7,10]
    print(num)
    num[-1]=8
    print(num)
    #Add and element to the list
    num.append(9)
    print(num)
    #insert and element in the specified index
    num.insert(0,0)
    print(num)
    num2 = num
    print(num2)
    num2 = [10,11,12,13]
    #concatena lista
    newlist = num + num2
    print(newlist)
    pos = newlist.index(8)
    #If there are more elements like this, the index returned is the very first
    print(pos)
    newlist[pos]= 234
    print(newlist)
    #remove deletes and specific element of the array, it needs a value
    newlist.remove(234)
    print(newlist)
    #pop deletes the last elements, or you can specify the index
    newlist.pop()
    print(newlist)
    newlist.pop(-2)
    newlist.pop(0)
    print(newlist)
    #revert the order of the list
    newlist.reverse()
    print(newlist)
    newlist.insert(4,23)
    newlist.insert(5,433)
    print(newlist)
    #sorting the list.. like obvious not?
    newlist.sort()
    print(newlist) 
    #sorting with strings
    abc = ['hola','aire','odio','luna','pera','gota']
    print(abc)
    abc.sort()
    print(abc)
    #You cannot sort and array with mixed types
    newabc = abc.copy()
    #Return a shallow copy of the list. Equivalent to a[:].
    print(newabc)

    
def tuplas():
    #Tuples are created with parentheses
    print('Tuples',30*"*")
    numeros = (1,2,3,5)
    palabra = ('hola','amor','odio','paja')
    print(numeros)
    print(palabra)
    print(type(palabra))
    #tuples by index
    print(numeros[2])
    #Tuples are immutable, they're used to store data thta shouldn't be modified
    print(palabra.index('odio'))
    print(palabra.count('amor'))
    print(len(palabra))
    #joining tuples
    numeros += palabra
    print(numeros)
    #nested tuples, for more complex data structures
    numeros = ((2,4,5),(5,4,2))
    print(numeros)
    #Transformation can be done
    lista = list(palabra)
    print(type(lista))
    lista.append('neta')
    tupla = tuple(lista)
    print(tupla)
    print(type(tupla))
    #you can do a tuple of lists or a list of tuples
    
def sets():
    #are defined with braces
    #A set is an unordered collection with no duplicate elements
    print('Sets',30*"*")
    colors = {'red', 'blue', 'yellow','grey', 'orange','green'}
    print(colors)
    print('orange' in colors)
    print('brown' in colors)
    a = set('abracadabra')
    b = set('alacazam')
    print(a)
    print(b)
    #they are like set of char elements, we did the convertion os a string
    #(array of chars) to set
    print(type(a))
    #letters in a but not in b
    print(a-b)
    #letters in a or b or both
    print(a|b)
    #letters in both a and b
    print(a&b)
    #etters in a or b but not both
    print(a^b)
    
def diccionario():       
    #Diccionary, are defined with braces, and is a pair of key and value
    print('Dictionary',30*"*")
    mydic = {'name':'pajaro metalico',
             'marca': 'la hora',
             'modelo':'de revista'
             }
    print(type(mydic))
    print(mydic)
    print(mydic['modelo'])
    print(mydic.get('modelos'))
    print(mydic.get('modelo'))
    #lThe main difference between the above methods is that the first can throw 
    #exception, but the get method can handled them
    print('marca' in mydic)
    print('color' in mydic)
    #this could be use to prevent exceptions
    #adding elements
    mydic['color']= 'de tus ojos'
    print(mydic)
    
    persona = {
        'name':'Victor',
        'last_name':'Gil',
        'langs':['java','python'],
        'age':28}
    
    print(persona)
    #modify dictionary
    persona['name']='Angel'
    persona['age']=30
    #works as a list
    persona['langs'].append('C')
    print(persona)
    #delete
    del persona['last_name']
    #is mandatory to pass the key in pop method for dict
    persona.pop('age')
    print(persona)
    #items (dreturn an array of tuples, each tuple is a pair of key and value)
    print('items: ', persona.items())
    #keys list with keys
    print('keys> ', persona.keys())
    #values rlist with value
    print('values> ', persona.values())
    #check this out, a list of tuples
    lista= list(persona.items())
    print(lista)
    
    
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
    print('Variables, String y otras cosas \n',30*"*")
    #Variables
    nombre = "Victor"
    edad = input('what is your age?')
    try:
        edad = int(edad)
    except ValueError:
        print("Wrong data type")
    #you do not have to specify the datatype
    print(12 + 35)
    print(12 - 35)
    print(12 * 35)
    
    #String
    string = "string"
    print(type(string) )
    lastName= "Gil"
    longName = nombre + " " + lastName
    print(longName)
    sentence = "This is a sentence, or is not? "
    print(sentence)
    # si quiero usar un apostrofe o una comilla doble
    #usa la contraria para abrir y cerrar   
    sentence="One wise man once said : '... what did i say?'"
    print(sentence)
    #Formato 
    template = "the name is: " + nombre + " and tha family ashamed is: "   + lastName
    print(template)
    template = "the name is:  {} and tha family ashamed is: {}".format(nombre, lastName)
    print(template)
    template = f"and this si the other form to print the name {nombre} and the other thing: {lastName}"
    print(template *4)
    
    #numbers
    numero = 23
    print(numero)
    print(type(numero))
    flotante = 2.45
    print(flotante)
    print(type(flotante))
    grandee = 454500000000000000000.01
    print(grandee)
    print(type(grandee))
    
    #booleans
    boleano = True
    print(boleano)
    print(type(boleano))
    print(not boleano)
    
    #print in different formats
    print("the chosen number is: " + str(numero))
    print(f"the same number, other format {numero}")
    #you can convert types, always as they make sense
    numero2 = "43"
    numero2 = int(numero2)
    
    # + - * / r
    #rest is %, division entera es //, el de elevado es **
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
    
    #float hadling
    #format in string
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
    print(y)
    print("*" * 34)
    tolerancia = 0.000001
    print(abs(x-y) < tolerancia)
    
    #logic operators    
    print('evaluando AND', True and False)
    print('evaluando OR', True or False)
    print('evaluando not', not True or False)
    print('evaluando nand', not(True and False))
    #Condicionales
    if True:
        print('always print')
        
    if False:
        print("never is goint to be printed")
    else:
        print("this is the one printed")
    #Formato if (se verifica que sea true) :
    if (True or False) and 100>50:
        print('yeah you got it, this is going to be printed')
        
    mascota = 'perro'
    if mascota == 'perro':
        print('asi se HACE PERRO')
    elif mascota == 'gato':
        print('asi se HACE GATO')
    elif mascota == 'pez':
        print('glu glu')
    else:
        print('lo que sea') 
        
    #random number
    from random import random
    numeroR = format(random() * 3, ".3g")
    print(numeroR)
    
    #Modifying strings
    texto = 'Lets see how Good this is'
    print('vamos' in texto)
    print(len(texto))
    print(texto.upper())
    print(texto.lower())
    print(texto.count('e'))
    print(texto.swapcase())
    print(texto.startswith('error'))
    print(texto.endswith('is'))
    print(texto.replace('is', 'really is'))
    
    texto2 = 'this is the second try'
    print(texto2.capitalize())
    print(texto2.title())
    print(texto2.isdigit())
    print('45'.isdigit())
    print('45.5'.isdigit())
    print('554'.isdecimal())
    print("%"*15)
    #indexing y slicing
    text = "Okey this si the interesting part"
    print(text[6])
    #the first index is 0, like arrays/list
    print(text[len(text)-1])
    print(text[-1])
    print(text[len(text)-1] == text[-1])
    #with negative numbers the count is backwards
    
    #slicing
    print(text[0:10])
    print(text[:10])
    #If we dont specify the first index, is 0 by default
    print(text[-6:len(text)])
    print(text[5:])
    #the same for the last index
    print(text[:])#Is valid, and it has their applications, good to have it in mind
    #this define: from where to where we are going to print, and the jumps, (1 by default)
    #If the last digit is 2, it print every other character in the secuence
    print(text[10:16:1])
    print(text[10:16:2])
    print(text[10:16:3])
    escrito = "Do you want to understand what did I write?"
    print(escrito[::2])
    escrito = "DDoo yyoou  wwanntt ttoo uunndeerrsttaanndd wwhhatt  ddiid II  wrriitee?"
    print(escrito[::2])
