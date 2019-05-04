import psutil
import time

inicio = time.time()

def bubbleSort1(lista):
    trocas = 0
    compracoes = 0
    for j in range(len(lista)):
        for i in range(len(lista)-1):
            compracoes +=1
            lista[i]=int(lista[i])
            lista[i+1]=int(lista[i+1])
            if (lista[i]>lista[i+1]):
                trocas +=1
                aux = lista[i]
                lista[i]= lista[i+1]
                lista[i+1]= aux         
    return {'Total_trocas':trocas,'Total_comparações':compracoes}





arq = open('0-100000.txt', 'r')
lista=arq.read().split('\n')
arq.close()
print(bubbleSort1(lista))

print("CPU:",psutil.cpu_percent(),"%")                 
print(psutil.virtual_memory()._asdict())  
fim = time.time()
print("Tempo de execução:",fim - inicio)
