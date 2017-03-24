# -*- coding: utf-8 -*-
import math


#1: Media de tres numeros
def media_Num(valorX, valorY, valorZ):
        media = (float(valorX) + float(valorY) +float(valorZ))/3
        print "La media es:", media
        print"*************************************************************"
        menuOpc()
        
#2: Volumen de una esfera
def vol_Esf(radio):
        vol = (1.33 * 3.1416) * (float(radio)**3)
        print "El volumen de la esfera es:", vol
        print"*************************************************************"
        menuOpc()
        
#3: 10 numeros impares inciando con en 13
def impar_N(impar):
        while impar <= 32: 
                 print "Numero Impar:", str(impar) 
                 impar += 2
        print"*************************************************************"
        menuOpc()

#4: obtener el maximo de 3 numeros
def mayor_N(x, y, z):
        if x >= y and x >= z:
                print "Numero Mayor", x
        elif y >= x and y >= z:
                print "Numero Mayor", y
        elif z >= x and z >= y:
                print "Numero Mayor", z
        print"*************************************************************"
        menuOpc()
                
#5: Rotar una lista
def rotar(lista):
        cont=1
        while cont<len(lista):
                lista.append(lista[0])
                lista.remove(lista[0])
                cont +=1
                print lista
        print"*************************************************************"
        menuOpc()
#rotar(input('vector'))



#6: Realiza un programa que permita generar un intervalo 
#de la suma de los cubos de los primeros n números.
#Ejemplo suma = 1 + 8 + 27 + n
def intervaloSuma(x):      
        vacio=[(conta**3) for conta in range(1,x+1)]        
        print vacio
        return sum(vacio)
        print"*************************************************************"
        menuOpc()


#7: Realiza un programa que permita generar un 
#intervalo de los cuadrados de n números mayores a 100.
def intervaloMayor(x):
        #for conta in range(1,x+1):
            #   if (conta**2)>100:
            #       return [(conta**2) for conta in range(1,x+1)]
        vacio=[(conta**2) for conta in range(1,x+1)]        
        num=1
        while num<len(vacio):
                if vacio[num]>100:
                        print vacio[num]
                num+=1
        print"*************************************************************"
        menuOpc()

#8: Realiza un programa que permita generar un intervalo 
#de n numeros entre 20 y 60
def intervaloN (x):
        cont=1
        while cont<=x:
                if cont>=20 and cont<=60:
                        print cont
                cont+=1
        print"*************************************************************"
        menuOpc()
#9: Realiza un programa que solicite dos argumentos de 
#tipo Double para calcular la hipotenusa de un 
#triangulo rectángulo y retorne un valor de tipo Double.        
def hipoT (x, y):
        print "Resultado:", math.sqrt(x**2 + y**2)
        print"*************************************************************"
        menuOpc()

#10: Crear un programa que por medio de recursión calcule 
#la suma de los cuadrados de n números.
def recursive (dato, variable=0):
        if(dato>=0):
                variable+=dato**2
                return recursive(dato-1,variable)
        else:
                print variable
                print"*************************************************************"
                menuOpc()
                

def menuOpc():
        print "\n1: Media de tres numeros\n2: Volumen de una esfera\n3: 10 Numeros impares inciando con en 13\n4: Obtener el maximo de 3 numeros\n5: Rotar una lista\n6: Generar un intervalo de la suma de los cubos de los primeros n numeros\n7: Programa que permite generar un intervalo de los cuadrados de n numeros mayores a 100\n8: Programa que permite generar un intervalo de n numeros entre 20 y 60\n9: Programa que solicita dos argumentos de tipo Double para calcular la hipotenusa\n10: Programa que por medio de recursion calcule la suma de los cuadrados de n numeros. "
        opc = int(input('Opcion: '))

        if opc == 1:
                 print"*************************************************************"
                 print "Media de tres numeros"
                 media_Num(float(input ('Valor 1: ')), float(input('Valor 2: ')), float(input('Valor 3: ')))
        elif opc == 2:
                print"*************************************************************"
                print "Volumen de una esfera"
                vol_Esf(input('ValorRadio: '))
        elif opc == 3:
                print"*************************************************************"
                print "10 numeros impares inciando con en 13"
                impar_N(input('Numero: '))
        elif opc == 4:
                print"*************************************************************"
                print "Obtener el maximo de 3 numeros"
                mayor_N(input('Valor 1: '), input('Valor 2: '), input('Valor 3: '))
        elif opc == 5:
                print"*************************************************************"
                print "Rotar una lista"
                rotar(input('Lista []: '))
        elif opc == 6:
                print"*************************************************************"
                print "Permite generar un intervalo de la suma de los cubos de los primeros n números. Ejemplo suma = 1 + 8 + 27 + n"
                intervaloSuma(input('Valor: '))
        elif opc == 7:
                print"*************************************************************"
                print "Permita generar un intervalo de los cuadrados de n números mayores a 100"
                intervaloMayor(input('ValorMayor: '))

        elif opc == 8:
                print"*************************************************************"
                print "Permite generar un intervalo de n numeros entre 20 y 60"
                intervaloN (int(input('ValorN: ')))
        elif opc == 9:
                print"*************************************************************"
                print "Programa que solicite dos argumentos de tipo Double para calcular la hipotenusa de un triangulo rectangulo y retorne un valor de tipo Double."
                hipoT (input('Lado A: '), input('Lado B: '))
        elif opc == 10:
                print"*************************************************************"
                print "Programa que por medio de recursión calcule la suma de los cuadrados de n números."
                recursive (input('Dato: '), variable=0)
        
        
menuOpc()
