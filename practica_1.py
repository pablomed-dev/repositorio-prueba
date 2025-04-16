#Función que reciba una lista de números y devuelva otra lista con los números pares multiplicados por 2.
def lista_par_multiplicado(lista):
    new_list= []
    for x in lista :
        if x % 2 == 0 :
            new_list.append(x*2)
    return new_list
    

print(f"La lista es {lista_par_multiplicado([1,2,3,4,5,6])}")
