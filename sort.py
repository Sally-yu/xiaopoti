def maopao(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if(arr[j]) > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def xuanze(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def charu(a):
    for i in range(1, len(a)):
        while i > 0 and a[i] < a[i - 1]:
            a[i], a[i - 1] = a[i - 1], a[i]
            i -= 1
    return a


# def bubble(a):
#     for i in range(len(a)):
#         for j in range(len(a) - 1 - i):
#             if a[j] < a[j + 1]:
#                 a[j], a[j + 1] = a[j + 1], a[j]
#     return a


# def select(a):
#     for i in range(len(a)):
#         for j in range(i + 1, len(a)):
#             if a[j] > a[i]:
#                 a[i], a[j] = a[j], a[i]
#     return a


# def insert(a):
#     for i in range(1, len(a)):
#         while i > 0 and a[i] > a[i - 1]:
#             a[i - 1], a[i] = a[i], a[i - 1]
#             i -= 1
#     return a


def main():
    a = [i for i in range(10000)]
    b = [34, 5, 5, 3, 43, 5, 3, 223, 24, 234, 5667, 6748, 8965, 5, 675, 453]
    a = charu(b)
    print(a)


if __name__ == '__main__':
    main()
