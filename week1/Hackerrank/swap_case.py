def swap_case(s):
    res = ''
    for i in s:
        n = ord(i)
        if n >= 65 and n <= 90:
            res += i.lower()
        elif n >= 97 and n <= 122:
            res += i.upper()
        else:
            res += i
    return res


if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print
    result