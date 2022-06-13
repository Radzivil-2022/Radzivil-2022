def wanna_again():
    again = input()
    if again == "y":
        choose_number()
    if again == "n":
        print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
    if again != "y":
        if again != "n":
            print("Введите y или n")
            wanna_again()

def choose_number():

    print('Добро пожаловать в игру "Числовая угадайка"')
    print('Компьютер загадает число, а вам нужно его угадать')
    print("До какого числа компьютеру загадать число?")
    limit = int(input())
# защита от дурака pass
    def is_valid(n):
        if 1 <= n <= limit:
            return True
        return False


    import random
    num = random.randint(1, limit)
    print("Компьютер загадал число от 1 до", limit)
    print("Попробуйте его угадать")
    print("Введите ваше число")
    n = int(input())
    while is_valid(n) == False:
        print("А может быть все-таки введем целое число от 1 до", limit, "?")
        n = int(input())
    count = 0
    while n!=num:
        if n < num:
            print("Ваше число меньше загаданного, попробуйте ещё разок")
            n = int(input())
            count += 1
        if n > num:
            print("Ваше число больше загаданного, попробуйте ещё разок")
            n = int(input())
            count += 1
    if n == num:
        count += 1
    print("Вы угадали, поздравляем!")
    print("Вам понадобилось", count, "попыток")
    print("Хотите сыграть ещё раз? y/n")
    wanna_again()

choose_number()
