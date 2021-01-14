for num in range(1, 101, 1):
    if num % 3 == 0:
        if num % 3 == 0 and num % 5 == 0:
            print('APPLESORANGES')
            continue
        print('APPLES')
    elif num % 5 == 0:
        if num % 3 == 0 and num % 5 == 0:
            print('APPLESORANGES')
            continue
        print('ORANGES')
    else:
        print(num)

