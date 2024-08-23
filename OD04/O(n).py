# O(n) - линейная сложность алгоритма
def line_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return None

arr = [10, 20, 30, 40, 50]
print(line_search(arr, 30))
print(line_search(arr, 60))