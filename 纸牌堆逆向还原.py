'''一副从1到n的牌，每次从牌堆顶取一张放桌子上，
再取一张放牌堆底，直到手机没牌，最后桌子上的牌是从1到n有序，
设计程序，输入n，输出牌堆的顺序数组
'''


def main(n):
    arr = []
    i = n
    while i >= 1:
        arr.append(i)
        temp = arr[0]
        del arr[0]
        arr.append(temp)
        i = i - 1
    temp = arr.pop()
    arr.insert(0, temp)
    arr.reverse()
    print(arr)
    return arr


def check(n):
    arr = []
    while len(n) > 1:
        arr.append(n[0])
        del n[0]
        temp = n[0]
        del n[0]
        n.append(temp)
        print(n)
        print(arr)
    arr = arr + n
    print(arr)


if __name__ == '__main__':
    main(100)
