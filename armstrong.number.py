def check_armstrong(num):
    text = str(num)
    n = len(text)
    t = 0
    for digit in text:
        p = int(digit) ** n
        t = t+p
    if t == num:
        print("armstrong number")
    else:
        print("not armstrong number")
num=int(input('enter a number='))
check_armstrong(num)
