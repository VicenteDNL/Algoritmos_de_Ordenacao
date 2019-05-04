import psutil
import time

inicio = time.time()

def selectionSort(lista):
    trocas = 0
    compracoes = 0
    for i in range(len(lista)-1):
        eleito=int(lista[i])
        menor=int(lista[i+1])
        pos=i+1
        for j in range (i+1,len(lista)):
            if (int(lista[j])<menor):
                menor=int(lista[j])
                pos=j
        compracoes +=1
        if (menor<eleito):
            trocas +=1
            lista[i]=int(lista[pos])
            lista[pos]=eleito
    return {'Total_trocas':trocas,'Total_comparações':compracoes}




arq = open('0-100.txt', 'r')
lista=arq.read().split('\n')
arq.close()
print(selectionSort(lista))

print("CPU:",psutil.cpu_percent(),"%")                 
print(psutil.virtual_memory()._asdict())  
fim = time.time()
print("Tempo de execução:",fim - inicio)
