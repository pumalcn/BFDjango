def mutate_string(string, position, character):
    res = string[:position] + character + string[position+1:]
    return res

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new