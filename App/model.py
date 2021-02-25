"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import selectionsort as sel
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import quicksort as qui 
from DISClib.Algorithms.Sorting import mergesort as mer
import time
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalog(typelist):
    catalog = lt.newList(typelist)

    return catalog

def newcategory():
        category = {}
        return category
# Funciones para agregar informacion al catalogo
def loadData(catalog,video):
        lt.addLast(catalog, video)

def loadCategory_id(category, category_id):
        category[category_id['id']] = category_id['name']

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpVideosByViews(video1, video2):
    return (float(video1['views']) > float(video2['views']))


def selectionSortVideos(catalog, size):
        sub_list = lt.subList(catalog, 1, size)
        sub_list = sub_list.copy()
        start_time = time.process_time()
        selectionSortList = sel.sort(sub_list, cmpVideosByViews)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return (elapsed_time_mseg, selectionSortList)


def shellSortVideos(catalog, size):
        sub_list = lt.subList(catalog, 1, size)
        sub_list = sub_list.copy()
        start_time = time.process_time()
        shellSortList = sa.sort(sub_list, cmpVideosByViews)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return (elapsed_time_mseg, shellSortList)

def insertionSortVideos(catalog, size):
        sub_list = lt.subList(catalog, 1, size)
        sub_list = sub_list.copy()
        start_time = time.process_time()
        insertionSortList = ins.sort(sub_list, cmpVideosByViews)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return (elapsed_time_mseg, insertionSortList)
        
def quickSortVideos(catalog, size):
        sub_list = lt-subList(catalog, 1, size)
        sub_list = sub_list.copy()
        start_time = time.process_time()
        quickSortList = qui.sort(sub_list, cmpVideosByViews)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return (elapsed_time_mseg, quickSortList)

def mergeSortVideos(catalog, size):
        sub_list = lt-subList(catalog, 1, size)
        sub_list = sub_list.copy()
        start_time = time.process_time()
        mergeSortList = mer.sort(sub_list, cmpVideosByViews)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return (elapsed_time_mseg, mergeSortList)
# Funciones de ordenamiento