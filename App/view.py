"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar X videos con más views")
    print("3- Consultar el video que más días fue trending para un país")
    print("4- Consultar el video que más días fue trending para una categoría")
    print("5- Consultar X videos con más likes en un país con un tag específico")
    print("0- Salir")

def initCatalog(typelist):
    return controller.initCatalog(typelist)
    
def initcategory():
    return controller.initcategory()

def loadData(catalog):
    controller.loadData(catalog)


def loadCategory_id(category):
    controller.loadCategory_id(category)

def printResults(ord_videos, sample=10):
    size = lt.size(ord_videos)

    if size > sample:
        print("Los primeros ", sample, " libros ordenados son: ")
        i = 1
        while i <= sample:
            video = lt.getElement(ord_videos, i)
            print("Titulo :"+ video['title'] + ' Titulo del Canal: '+ video['channel_title'] +
            ' Trending_date: ' + video['trending_date']+ ' Pais: '+ video['country'] +
            ' views: '+ video['views'] + ' Likes: ' + video['likes'] + ' Dislikes: ' + video['dislikes'])
            i += 1
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print('Tipo de lista que desea crear')
        print('1- Array list')
        print('2- Single linked list')
        typelist = input('Seleccione el tipo de lista para continuar\n')
        print("Cargando información de los archivos ....")
        catalog = None
        if int(typelist[0]) == 1:
            catalog = initCatalog('ARRAY_LIST')
            
        elif int(typelist[0]) == 2:
            catalog = initCatalog('SINGLE_LIKED')

        loadData(catalog)
        category = initcategory()
        loadCategory_id(category)
        video = lt.firstElement(catalog)
        print(type(catalog))
        print("Titulo :"+ video['title'] + ' Titulo del Canal: '+ video['channel_title'] +
            ' Trending_date: ' + video['trending_date']+ ' Pais: '+ video['country'] +
            ' views: '+ video['views'] + ' Likes: ' + video['likes'] + ' Dislikes: ' + video['dislikes'])
        print('Videos cargados: ' + str(lt.size(catalog)))
        print('Catalagos cargados: ' + str(len(category)))
        

    elif int(inputs[0]) == 2:
        size = int(input("Inserte el número de videos: "))
        print('Metodo de ordenamiento que desea utilizar')
        print('1- shellsort')
        print('2- selectionsort')
        print('3- insertionsort')
        print('4- mergesort')
        print('5- quicksort')
        typesort = input('Seleccione el metodo de ordenamiento para continuar\n')
        result = None
        if size <= lt.size(catalog):
            if int(typesort[0]) == 1:
                result = controller.shellSortVideos(catalog, (size))
                print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                            str(result[0]))
                printResults(result[1])
                
            elif int(typesort[0]) == 2:
                result = controller.selectionSortVideos(catalog, (size))
                print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                            str(result[0]))
                printResults(result[1])
            
            elif int(typesort[0]) == 3:
                result = controller.insertionSortVideos(catalog, int(size))
                print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                            str(result[0]))
                printResults(result[1])
            elif int(typesort[0]) == 4:
                result = controller.mergeSortVideos(catalog, int(size))
                print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                            str(result[0]))
                printResults(result[1])
            elif int(typesort[0]) == 5:
                result = controller.quickSortVideos(catalog, int(size))
                print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                            str(result[0]))
                printResults(result[1])
        #pais = str(input("Inserte un país: "))
        #categ = str(input("Inserte una categoría: "))





    elif int(inputs[0]) == 3:
        pais = str(input("Inserte una categoría: "))
        
    elif int(inputs[0]) == 4:
        videos = int(input("Inserte el número de videos: "))
        pais = str(input("Inserte un país: "))
        tag = str(input("Inserte un tag específico: "))

    else:
        sys.exit(0)
sys.exit(0)
