def maximizar(As, D):
    arrRespuesta=[]
    acumulado=0
    mayor=0
    
    #Estructura voraz
    #etapas: cada tupla de la lista As
    #criterio voraz por etapa: el peso de cada tupa sumando al acumulado es menor que el total??
    #   si: agregar a la lista de respuesta y sumar peso al acumulado
    #   no: cerrar el ciclo de etapas
    for i in range(len(As)):
        if(As[i][1]+acumulado<=D):
            agregarOrdenado(arrRespuesta, As[i])
            acumulado=acumulado+As[i][1]
            if(As[i][1]>mayor):
                mayor=As[i][1]
        else:
            if(As[i][1]<mayor):
                acumulado=quitarMayor(mayor,arrRespuesta,acumulado)
                mayor=buscarMayor(arrRespuesta)
                agregarOrdenado(arrRespuesta, As[i])
                acumulado=acumulado+As[i][1]
                
                if(As[i][1]>mayor):
                    mayor=As[i][1]
                
    return arrRespuesta

def quitarMayor(mayor,arr,acumulado):
    for i in range(len(arr)):
        if(arr[i][1]==mayor):
            acumulado=acumulado-arr[i][1]
            arr.pop(i)
            break
    return acumulado
            
def buscarMayor(arr): 
    mayor=0
    for i in range(len(arr)):
        if(arr[i][1]>mayor):
            mayor=arr[i][1]
    return mayor

def agregarOrdenado(arr, elemento):
    for i in range(len(arr)):
        if(elemento[1]<arr[i][1]):
            arr.insert(i,elemento)
            return
    arr.append(elemento)
