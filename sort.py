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


def shellSort(nums):
    lens = len(nums)
    gap = 1  
    while gap < lens // 3:
        gap = gap * 3 + 1  # 动态定义间隔序列
    while gap > 0:
        for i in range(gap, lens):
            curNum, preIndex = nums[i], i - gap  # curNum 保存当前待插入的数
            while preIndex >= 0 and curNum < nums[preIndex]:
                nums[preIndex + gap] = nums[preIndex] # 将比 curNum 大的元素向后移动
                preIndex -= gap
            nums[preIndex + gap] = curNum  # 待插入的数的正确位置
        gap //= 3  # 下一个动态间隔
    print(nums)


def mergeSort(nums):
    # 归并过程
    def merge(left, right):
        result = []  # 保存归并后的结果
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result = result + left[i:] + right[j:] # 剩余的元素直接添加到末尾
        return result
    # 递归过程
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    return(left, right)


def quickSort(nums):  # 这种写法的平均空间复杂度为 O(nlogn)
    if len(nums) <=1:
        return nums
    p=nums[0]
    left=[nums[i] for i in range(1,len(nums)) if nums[i] < p]
    right=[nums[i] for i in range(1,len(nums)) if nums[i] >= p ]
    return quickSort(left) +[p] +quickSort(right)


def countSort(a):
    bucket=[0] * (max(a)+1)
    for num in a:
        bucket[num] += 1
    b = []
    for i in range(len(bucket)):
        while bucket[i] > 0:
            b.append(i)
            bucket[i]-=1
    return b

def main():
    a = [1,23,4,563,3,5,23,43,54,28]
    print(countSort(a))


if __name__ == '__main__':
    main()
