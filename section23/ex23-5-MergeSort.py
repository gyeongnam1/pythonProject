'''
ex23-5-MergeSort.py

병합 정렬(Merge Sort)
    분할 정복 알고리즘의 일종으로, 리스트를 절반으로 나눈 후
    각각을 재귀적으로 합병 정렬하고, 다시 합치면서 정렬하는 알고리즘
'''


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2  # mid 값 4

    left = merge_sort(arr[:mid])  # mid 앞에 값까지 자르기 . left 값은 5,2,8,6. 그 안에서 또 merge_sort를 함
    ''' 재귀대명사니까 같은 함수가 이 자리에서 계속 반복
        if len(arr) <= 1:
                return arr
        mid = len(arr) //2

        left = merge_sort(arr[:mid])
                if len(arr) <= 1:
                    return arr
                mid = len(arr) //2

                left = merge_sort(arr[:mid]) 
                ...   
                길이가 1이 되면 return arr
    '''
    right = merge_sort(arr[mid:])  # right 값은 1,9,3,7

    return merge(left, right)


def merge(left, right):
    result = []

    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


# 실행 코드
arr = [5, 2, 8, 6, 1, 9, 3, 7]
sorted_arr = merge_sort(arr)
print(sorted_arr)