﻿"""
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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog(typelist):
    catalog = model.newCatalog(typelist)
    return catalog

def initcategory():
    catalog = model.newcategory()
    return catalog
# Funciones para la carga de datos
def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadvideo(catalog)


def loadvideo(catalog):
    videofile = cf.data_dir + 'videos/videos-large.csv'
    input_file = csv.DictReader(open(videofile, encoding='utf-8'))
    for video in input_file:
        model.loadData(catalog, video)


def loadCategory_id(category):
    categoryfile = cf.data_dir + 'videos/category-id.csv'
    input_file = csv.DictReader(open(categoryfile, encoding="utf-8"),  delimiter='\t')
    print
    for category_id in input_file:
        model.loadCategory_id(category, category_id)

# Funciones de ordenamiento
def selectionSortVideos(catalog, size):

    return model.selectionSortVideos(catalog, size)

def shellSortVideos(catalog, size):

    return model.shellSortVideos(catalog, size)

def insertionSortVideos(catalog, size):

    return model.insertionSortVideos(catalog, size)

# Funciones de consulta sobre el catálogo
'''def country_categoryVideos(catalog, category, pais, category_id)
    for video in catalog:
        if video['country'] == pais:'''

