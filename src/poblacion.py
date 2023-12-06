# -*- coding: utf-8 -*-

""" 
Poblacion mundial
@author: Toñi Reina
REVISOR: José Antonio Troyano, Daniel Mateos, Mariano González, Fermín Cruz
ÚLTIMA MODIFICACIÓN: 10/10/2022
"""

import csv
from matplotlib import pyplot as plt
from collections import namedtuple

RegistroPoblacion = namedtuple("RegistroPoblacion", "pais, codigo, ano, censo")

############################################################################################
def lee_poblaciones(ruta_fichero:str)->list[RegistroPoblacion]:
    """
    Lee el fichero de entrada y devuelve una lista de tuplas poblaciones

    @param fichero: nombre del fichero de entrada
    @type fichero: str

    @return: lista de tuplas con la información del fichero
    @rtype: RegistroPoblacion
    """
    pass
    res= list()
    with open (ruta_fichero, 'rt', encoding='utf-8') as f:
        lector= csv.reader(f) #, delimiter=',') no hace falta por defeto es ,
#        next(lector) salta primera linea!!
        for pais, codigo, ano, censo in lector:
            my_list=RegistroPoblacion(pais, codigo, int(ano), int(censo))
            res.append(my_list)
    return res

def calcula_paises(poblaciones):
    """
    Calcula la lista de países distintos presentes en una lista de de tuplas de tipo RegistroPoblacion.

    @param poblaciones: lista de tuplas con información de poblaciones
    @type poblaciones: list(RegistroPoblacion)

    @return: lista de paises, ordenada alfabéticamente, sin duplicados
    @rtype: list(str)
    """
    pass
    res= list()
    for i in poblaciones:
        res.append(i.pais)
    res=set(res)
    res=sorted(res)
    return res

def filtra_por_pais(poblaciones, pais_o_codigo):
    """
    Devuelve el año y el censo de las tuplas correspondientes a un determinado pais

    @param poblaciones: lista de tuplas con información de poblaciones
    @type poblaciones: list(RegistroPoblacion)
    @param pais_o_codigo: nombre o código del país del que se seleccionarán los registros
    @type pais_o_codigo: str

    @return: lista de tuplas (año, censo) seleccionadas
    @rtype: list(tuple(int, int))
    """
    pass
    res = list()
    for i in poblaciones:
        if i.pais == pais_o_codigo or i.codigo == pais_o_codigo:
            tupla=(i.ano, i.censo)
            res.append(tupla)
            #res.append((i.ano, i.censo)) eso tambien sirve pero ojo! cuidado con dos parantesis
    return res

##############################################################################################

##############################################################################################
def filtra_por_paises_y_anyo(poblaciones:list(), anyo:int, paises:list())->list():
    """
    Devuelve el país y el censo de las tuplas correspondientes a un conjunto de paises de un año concreto.

    @param poblaciones: lista de tuplas con información de poblaciones
    @type poblaciones: list(RegistroPoblacion)
    @param año: año del que se seleccionarán los registros
    @type año: int
    @param paises: conjunto de nombres de países de los que se seleccionarán los registros
    @type paises: set(str)

    @return: lista de tuplas (pais, censo) seleccionadas
    @rtype: list(tuple(str,int))
    """
    pass
    res = list()
    for i in poblaciones:
        for p in paises:
            if i.ano == anyo and i.pais == p:
                tupla=(i.pais , i.censo)
                res.append(tupla)
    return res

##############################################################################################

###############################################################################################
def muestra_evolucion_poblacion(poblaciones, pais_o_codigo):
    """
    Genera una curva con la evolución de la población de un país. El país puede
    darse como su nombre completo o por su código.

    @param poblaciones: lista de tuplas con información de poblaciones
    @type poblaciones: list(RegistroPoblacion)
    @param pais_o_codigo: nombre o código del país del que se generará la gráfica
    @type pais_o_codigo: str
    """
    # TODO Complete la función para asignar los valores correctos
    #  a las variables titulo, lista_años y lista_habitantes
    titulo = "Evolucion de la poblacion de Spain"
    etiqueta_eje_x="Anos"
    etiqueta_eje_xy="Num. Habitantes"
    filtra_por_pais(poblaciones, pais_o_codigo)
    filtrados= filtra_por_pais(poblaciones, pais_o_codigo)
    filtrados.sort()
    lista_anos=list()
    lista_habitantes=list()
    for ano, censo in filtrados:
        lista_anos.append(ano)
        lista_habitantes.append(censo)
#        if i.pais == pais_o_codigo or i.codigo == pais_o_codigo:
#            poblaciones_ano=poblaciones_ano.append((i.ano))
#            poblaciones_censo=poblaciones_censo.append((i.censo))
#    lista_años = [poblaciones_ano]
#    lista_habitantes = [poblaciones_censo]
    # Estas instrucciones dibujan la gráfica
    plt.title(titulo)
    plt.xlabel(etiqueta_eje_x)
    plt.ylabel(etiqueta_eje_xy)
    plt.plot(lista_anos, lista_habitantes)
    plt.show()


###############################################################################################

###############################################################################################
def muestra_comparativa_paises_anyo(poblaciones, ano, paises):
    """
    Genera una gráfica de barras en la que se muestra la comparativa de
    la población de varios países en un año concreto

    @param poblaciones: lista de tuplas con información de poblaciones
    @type poblaciones: list(RegistroPoblacion)
    @param año: del que se generará la gráfica
    @type año: int
    @param paises: nombres de los países para los que se generará la gráfica
    @type paises: list(str)
    """
    # TODO Complete la función para asignar los valores correctos
    #  a las variables titulo, lista_paises y lista_habitantes
    titulo = "Poblacion en el ano 2016"
    filtra_por_paises_y_anyo(poblaciones, ano, paises)
    filtrados = filtra_por_paises_y_anyo(poblaciones, ano, paises)
    filtrados.sort()
    lista_paises = []
    lista_habitantes = []
    for pais, censo in filtrados:
        lista_paises.append(pais)
        lista_habitantes.append(censo)

    # Estas instrucciones dibujan la gráfica
    plt.title(titulo)
    indice = range(len(lista_paises))
    plt.bar(indice, lista_habitantes)
    plt.xticks(indice, lista_paises, fontsize=8)
    plt.show()