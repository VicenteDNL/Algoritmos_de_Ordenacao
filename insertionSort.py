import psutil
import time

inicio = time.time()

def insertionSort(lista):
    trocas = 0
    compracoes = 0
    for i in range(1,len(lista)):
        eleito=int(lista[i])
        j=i-1
        compracoes +=1
        while j>=0 and int(lista[j])>eleito:
            trocas +=1
            lista[j+1]=int(lista[j])
            j-=1
        lista[j+1]=eleito
    return {'Total_trocas':trocas,'Total_comparações':compracoes}




arq = open('0-100000.txt', 'r')
lista=arq.read().split('\n')
arq.close()
print(insertionSort(lista))

print("CPU:",psutil.cpu_percent(),"%")                 
print(psutil.virtual_memory()._asdict())  
fim = time.time()
print("Tempo de execução:",fim - inicio)
