import streamlit as st
import estandarizador_escenario2

#def estandarizar_direccion(cadena):
#    componentes = estandarizador_escenario2.estandarizar_direccion(cadena)
#    return estandarizador_escenario2.get_diccionario(componentes)

def main():
    st.title("Aplicación de Estandarización de Direcciones")
    
    # Solicitar la cadena al usuario
    cadena = st.text_input("Ingrese una dirección:")

# def get_diccionario(diccionario: dict):
#    dictionary_depurado: dict = {}
#    if diccionario is not None:
#        for i in diccionario.keys():
#            if diccionario[i] != "":
#                dictionary_depurado[i] = diccionario[i]
#        return dictionary_depurado
#    else:
#        return dictionary_depurado


# lista_direcciones = ["MANZANA 4 "]

# for i in lista_direcciones:
#    componentes = estandarizador_escenario2.estandarizar_direccion(i)
#    print(i)
#    print(get_diccionario(componentes))
#    print("-------------------------------------------")
