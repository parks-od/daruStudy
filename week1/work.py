def divCal(numbers):
    for number in numbers:
        if number%2==0: print(f"{number}는 짝수입니다.")
        else : print(f"{number}는 홀수입니다.")
    print("--------------------------")
def lengthCal(numbers):
    for number in numbers:
        print(f"{number}는 {len(str(number))}자릿수입니다.")

if __name__ == '__main__':
    numbers = [273, 103, 5, 32, 65, 9, 72,800, 99]
    divCal(numbers)
    lengthCal(numbers)