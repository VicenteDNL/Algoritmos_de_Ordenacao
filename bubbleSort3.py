import psutil
import time

inicio = time.time()

def bubbleSort3(lista):
    trocas = 0
    compracoes = 0
    j=1
    troca=True
    while (j<=len(lista) and troca):
        troca=False
        for i in range(len(lista)-1):
            compracoes +=1
            lista[i]=int(lista[i])
            lista[i+1]=int(lista[i+1])
            if(lista[i]>lista[i+1]):
                trocas +=1
                troca=True
                aux=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=aux
        j+=1        
    return {'Total_trocas':trocas,'Total_comparações':compracoes}





arq = open('0-100000.txt', 'r')
lista=arq.read().split('\n')
arq.close()
print(bubbleSort3(lista))

print("CPU:",psutil.cpu_percent(),"%")                 
print(psutil.virtual_memory()._asdict())  
fim = time.time()
print("Tempo de execução:",fim - inicio)
