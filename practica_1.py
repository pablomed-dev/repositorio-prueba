#Función que reciba una lista de números y devuelva otra lista con los números pares multiplicados por 2.
# def lista_par_multiplicado(lista):
#     new_list= []
#     for x in lista :
#         if x % 2 == 0 :
#             new_list.append(x*2)
#     return new_list
    

# print(f"La lista es {lista_par_multiplicado([1,2,3,4,5,6])}")

def lista_par_multiplicado(lista):
    return [x*2 for x in lista if x % 2 ==0]

print(f"La nueva lista es {lista_par_multiplicado([1,2,3,4,5,6,7,8])}")