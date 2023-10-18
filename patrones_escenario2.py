import re
from itertools import product
import diccionarios_escenario2

diccionario_B = diccionarios_escenario2.get_b()
diccionario_U = diccionarios_escenario2.get_u()
diccionario_M = diccionarios_escenario2.get_m()
diccionario_L = diccionarios_escenario2.get_l()
diccionario_R = diccionarios_escenario2.get_r()
diccionario_F = diccionarios_escenario2.get_f()
diccionario_C = diccionarios_escenario2.get_c()
diccionario_T = diccionarios_escenario2.get_t()


def verificar_patron_escenario2(cadena, patron):
    busqueda = re.search(patron, cadena)
    if busqueda:
        return busqueda.groups()
    else:
        return None


def extraer_componentes_direccion_escenario2(cadena):
    componentes_direccion_escenario2 = {
        "Barrio": "",
        "Urbanizacion": "",
        "NombreUrbanizacion": "",
        "TipoPiso": "",
        "NumeroPiso": "",
        "Manzana": "",
        "TipoPredio": "",
        "Casa": "",
        "LoteParcela": "",
        "Sector": "",
        "Kilometro": "",
        "IdentificadorPredio": "",
        "UnhandledPattern": "",
        "UnhandledData": "",
        "InputPattern": "",
        "UserOverrideFlag": "",
        "LineaPatron": "",
        "DireccionEjemplo": ""
    }

    for M in diccionario_M.keys():
        patron_1 = r'^$'.format(re.escape(M))
        componentes_1 = verificar_patron_escenario2(cadena, patron_1)
        if componentes_1 is not None:
            componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_1[0])
            componentes_direccion_escenario2["InputPattern"] = 'M|^|+|^|'
            componentes_direccion_escenario2["LineaPatron"] = '5189'
            componentes_direccion_escenario2["DireccionEjemplo"] = 'MANZANA 27'
            return componentes_direccion_escenario2

    return None
