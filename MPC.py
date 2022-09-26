#Multiprocessing Prime Calculator
from multiprocessing import Pool
from time import time




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
    
    #process = []

    nb2 = 1
    max = 50000
    process = [nb2+n for n in range(max)]
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

    print(result, len(result))
    print(f"main took {total_duration:.2f}s total")



if __name__ == "__main__":
    main()