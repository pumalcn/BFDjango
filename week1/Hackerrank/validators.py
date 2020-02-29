if __name__ == '__main__':
    s = raw_input()
    ok1, ok2, ok3, ok4, ok5 = [False] * 5
    for i in s:
        if i.isalpha():
            ok2 = True
        if i.isdigit():
            ok3 = True
        if i.islower():
            ok4 = True
        if i.isupper():
            ok5 = True
    ok1 = ok3 or ok2
    res = [ok1, ok2, ok3, ok4, ok5]

    for i in res:
        print(i)

