def average(array):
    return sum(set(array))/len(set(array))

if __name__ == '__main__':
    n = int(raw_input())
    arr = list(map(int, raw_input().split()))
    result = average(arr)
    print(result)