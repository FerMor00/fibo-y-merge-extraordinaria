from multiprocessing import Pool
import time
import random
import sys
import multiprocessing

    
    
def Fibo():
    MAX = 22000000
  
    f = [0] * MAX
      
    def fib(n) : 
        if (n == 0) : 
            return 0
        if (n == 1 or n == 2) : 
            f[n] = 1
            return (f[n]) 
      
        if (f[n]) : 
            return f[n] 
      
        if( n & 1) : 
            k = (n + 1) // 2
        else :  
            k = n // 2
      
        
        if((n & 1) ) : 
            f[n] = (fib(k) * fib(k) + fib(k-1) * fib(k-1)) 
        else : 
            f[n] = (2*fib(k-1) + fib(k))*fib(k) 
      
        return f[n] 
      
      
    n = 21806
    start = time.time()
    print(fib(n)) 
    elapsed = time.time() - start
    print('Fibo: %f sec' % (elapsed))
    print('Fernando Moreno 21806962')


def MergeSort():
    N = 21806962
    print('Generated random list of: ', N)
    if len(sys.argv) > 1:  
        N = int(sys.argv[1])

    #backup list.
    lystbck = [random.random() for x in range(N)]

    #Sequential .
    #lyst = list(lystbck)
    #start = time.time()             
    #lyst = mergesort(lyst)
    #elapsed = time.time() - start

    #if not isSorted(lyst):
     #   print('Sequential mergesort did not sort. oops.')
    
    #print('Sequential mergesort: %f sec' % (elapsed))
   # time.sleep(3)


    #parallel mergesort. 
    lyst = list(lystbck)
    start = time.time()
    n = multiprocessing.cpu_count()
    lyst = mergeSortParallel(lyst, n)
    elapsed = time.time() - start

    if not isSorted(lyst):
        print('mergeSortParallel did not sort. oops.')

    print('Parallel mergesort: %f sec' % (elapsed))

    #time.sleep(3)
    

def merge(left, right):
    ret = []
    li = ri = 0
    while li < len(left) and ri < len(right):
        if left[li] <= right[ri]:
            ret.append(left[li])
            li += 1
        else:
            ret.append(right[ri])
            ri += 1
    if li == len(left):
        ret.extend(right[ri:])
    else:
        ret.extend(left[li:])
    return ret

def mergesort(lyst):
    if len(lyst) <= 1:
        return lyst
    ind = len(lyst)//2
    return merge(mergesort(lyst[:ind]), mergesort(lyst[ind:]))

def mergeWrap(AandB):
    a,b = AandB
    return merge(a,b)

def mergeSortParallel(lyst, n):
    numproc = n
    print('numero de procesadores: ',numproc)
    
    endpoints = [int(x) for x in linspace(0, len(lyst), numproc+1)]
    args = [lyst[endpoints[i]:endpoints[i+1]] for i in range(numproc)]
    pool = Pool(processes = numproc)
    sortedsublists = pool.map(mergesort, args)
    
    while len(sortedsublists) > 1:
        
        args = [(sortedsublists[i], sortedsublists[i+1]) \
				for i in range(0, len(sortedsublists) - 1, 2)]
        sortedsublists = pool.map(mergeWrap, args)
        
    return sortedsublists[0]
    

    
def linspace(a,b,nsteps):
    ssize = float(b-a)/(nsteps-1)
    return [a + i*ssize for i in range(nsteps)]


def isSorted(lyst):
    for i in range(1, len(lyst)):
        if lyst[i] < lyst[i-1]:
            return False
    return True
  
def main():
    user= 'fer'
    password = 'coco'
    acceso = False
    opcion = 1
    while not acceso:
        usuario = input('Introduzca su email: ')
        contrasena = input('Introduzca su contraseña: ')
        if (usuario != user)or(contrasena != password):
            print('Usuario o contraseña incorrecto')
        else:
            print('Usuario y contraseña correcto')
            acceso = True
            
    while opcion != 3:
        print('1. Fibo')
        print('2. MergeSort')
        print('3. Salir')

        opcion = int(input('Introduzca la opcion: '))
        if opcion == 1:
            Fibo()

        elif opcion == 2:
            MergeSort()

        elif opcion == 3:
            print('Hasta luego')
        else:
            print('la opcion introducida no es valida')

            
if __name__ == '__main__':
   main()
