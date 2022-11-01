if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr1=set(list(arr))
    arr1=sorted(arr1)
    print(arr1[-2])
