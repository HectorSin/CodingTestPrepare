while True:
    number = input()
    if number == '0':
        break

    checker = 'yes'
    for idx, i in enumerate(number):
        if i != number[-idx-1]:
            checker = 'no'

    print(checker)