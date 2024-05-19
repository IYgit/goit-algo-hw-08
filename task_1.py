import heapq

def connect_cables(cables):
    heapq.heapify(cables)
    total_cost = 0
    
    while len(cables) > 1:
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)
        
        new_cable = cable1 + cable2
        total_cost += new_cable
        
        heapq.heappush(cables, new_cable)
    
    return total_cost

# TEST
cables = [4, 3, 2, 6]
min_cost = connect_cables(cables)
print("Мінімальні витрати на об'єднання кабелів:", min_cost)
