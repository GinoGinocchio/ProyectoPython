
#Se abre el archivo en caso no haya ningun dato

from logging import exception
import sys

#Titulo del programa
print("Bienvenidos al Registro de Notas\n")

#Menu de acciones del programa
def Menu():  
    #Se usa un try except para que el programa no crashee ante algun error
    try:
        #Lista de opciones del menu
        print("1.Registrar")
        print("2.Mostrar")
        print("3.Salir\n")
        #Se inicializa el num en 0 para poder manejarlo como si fuera un do while
        num=0
        #Se realiza el while de manera que solo realice las opciones mencionadas en el menu
        while(num < 1 or num > 3):
            num = int(input("Inserte una opcion: "))
        #Se enlazan las opciones con los metodos correspondientes
        if(num==1):
            print("\n")
            #Metodo registrar notas de un alumno
            Registrar()
        if(num==2):
            print("\n")
            #Metodo mostrar registros
            Mostrar()
        if(num==3):
            #Metodo para salir del programa
            sys.exit()
    #Excepcion que imprime en pantalla un error en caso exista y devuelve el menu
    except Exception as ex:
        print(ex)
        Menu()
    

    
def Registrar():

    try:
        #Metodo para abrir el archivo para poder insertar datos, para esto se usa el 'a' del append
        f = open ( 'Registros.txt','a')
        #Se recibe el nombre del alumno y se almacena en un string
        nombre = input ("Ingrese el nombre del alumno: ")
        alumno="Alumno: " + nombre+"\n\n"
        #Se inserta en el archivo de texto
        f.write(alumno)
        #Se insertan los campos correspondientes al archivo
        Campos = "\t\t\tN1\tN2\tN3\tProm\n\n"
        f.write(Campos)
        #Se realiza un for para la insercion de notas de los 3 cursos usados para este ejemplo
        for i in range(0,3):
            #Se verifican las opciones de acuerdo al curso que pertenezca
            if i == 0:
                #Curso de algoritmica y se inserta al archivo
                algo = "Notas de algoritmica\t"
                print("Notas de algoritmica\n")
                f.write(algo)
            elif i == 1:
                #Curso de estadistica y se inserta al archivo
                Estadistica = "Notas de Estadistica\t"
                print("Notas de Estadistica\n")
                f.write(Estadistica) 
            else:
                #Curso de calculo y se inserta al archivo
                Calculo = "Notas de Calculo\t"
                print("Notas de Calculo\n")
                f.write(Calculo)
            #Se crea un vector vacio de dimension 4 para las notas y el promedio de notas
            nota = [None] * 4
            #Se crea un for para la insercion de las 3 primeras notas
            for n in range(0,3):
                #Se inicializa la nota con -1 para poder tratarlo como un do while
                nota[n]=-1
                #Se inicializa el while de manera que solo permita notas de 0 a 20
                while (nota[n] < 0 or nota[n]>20):
                    notitas = "Ingrese la nota "+ str(n+1) + ": "
                    nota[n] = int(input(notitas))
                #Se convierte la nota en un string para poder ser almacenado en el archivo de texto
                nota_wh=str(nota[n])+"\t"
                #Se almacena la nota en el archivo de texto
                f.write(nota_wh) 
            #Se saca el promedio de las 3 primeras notas para la 4 nota
            nota[3]=int((nota[0]+nota[1]+nota[2])/3)
            #Se convierte el promedio en un string para poder insertarlo en el archivo
            nota_wh=str(nota[3])+"\n\n"
            #Se inserta el promedio en el archivo
            f.write(nota_wh)                         
            print("\n")
        f.write("\n")
        #Se cierra el archivo con el registro ya hecho
        f.close()
        Menu()
    #Se usa un except para capturar los errores en caso de existir uno
    except Exception as ex:
        print(ex)
    
    
def Mostrar():
    #Se abre el archivo de texto, se usa una 'r' de 'read'
    f = open ('Registros.txt','r')
    #Se le otorga a una variable el valor del archivo
    mensaje = f.read()
    #Finalmente se muestra el archivo en un print
    print(mensaje)
    #Se cierra el archivo
    f.close()
    Menu()

#Se inicializa el Menu que vendria a ser el Main de la aplicacion
Menu()
 