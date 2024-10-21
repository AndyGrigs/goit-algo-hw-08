import heapq

def min_cost_connect(cables):
    heapq.heapify(cables)   

    cost = 0
    while len(cables) > 1:
        cost += heapq.heappop(cables) + heapq.heappop(cables)
        heapq.heappush(cables, cost)
    return cost

cables = [4, 3, 2, 6]

print("Мініьфльні кошти для з'єднання кабелів" ,min_cost_connect(cables))