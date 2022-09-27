#Multiprocessing Prime Calculator
from multiprocessing import Pool
import time




def Prime(initialNumber):
    start_t = time.perf_counter()
    number = initialNumber
    if number > 1:
        for i in range(2, int(number/2)+1):
            if number % i == 0:
                break
        else:
            end_t = time.perf_counter()
            total_duration = end_t - start_t
            return number, float("{:.2f}".format(total_duration))



def main():
    
    print("Digite um intervalo entre dois números \nEx:1-100")
    inputString = input()
    try:
        min = int(inputString.split('-')[0])
        max = int(inputString.split('-')[1])
    except:
        print("Número inválido")
        return

    if(min > max):
        temp = min
        min = max
        max = temp
    
    process = [min+n for n in range(max)]
    print(process[0], process[-1], len(process))

    result = []

    start_t = time.perf_counter()

    with Pool() as pool:
        resultInt = pool.map(Prime, process)
        for i in resultInt:
            if(i != None):
                result.append(i)

    end_t = time.perf_counter()
    total_duration = end_t - start_t

    print(result)
    print(len(result), " números primos foram encontrados")
    print(f"main levou {total_duration:.2f}s para terminar")



if __name__ == "__main__":
    main()