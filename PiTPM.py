class Factorial():
    def __init__(self):
        pass

    def factorial(self,num):
        if num == 0:
            return 1
        else:
            result = 1
            for i in range(num):
                result *= (i+1)
            return result

def main():
    print("Enter a number:")
    number = int(input())
    fact = Factorial()
    result = fact.factorial(number)
    print(result)

if __name__ == '__main__':
    main()