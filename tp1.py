# comentario
def main():# comentario
    for num in range(1, 101):# comentario
        if (numberIsPrime(num)):# comentario
            print(num)

def numberIsPrime(num):
    return factoringNumber(num) == 1
   
def factoringNumber(num):
    timesFactored = 0
    while (num > 1):
        if (num % 2 == 0):
            num /= 2
        elif (num % 3 == 0):
            num /= 3
        elif (num % 5 == 0):
            num /= 5
        elif (num % 7 == 0):
            num /= 7
        else:
            num /= num
        timesFactored += 1
    return timesFactored  
        
main()
