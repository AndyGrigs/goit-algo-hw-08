import heapq

def merge_k_lists(lists):
    # Створимо мінімальну купу
    min_heap = []
     # Додаємо перші елементи всіх списків до купи разом з їх індексами
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(min_heap, (lists[1][0], i, 0))
    
    res = []
     # Поки купа не порожня
    while min_heap:
        # Виймаємо найменший елемент з купи
        cost, i, j = heapq.heappop(min_heap)
        res.append(cost)
        # Якщо є наступний елемент у цьому списку, додаємо його до купи
        if j + 1 < len(lists[i]):
            heapq.heappush(min_heap, (lists[i][j + 1], i, j + 1))
    return res

# Приклад використання:
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)