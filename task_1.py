import heapq

def min_cost_to_connect_cables(cables):
    # Ініціалізуємо чергу пріоритетів
    heapq.heapify(cables)
    total_cost = 0
    
    # Об'єднуємо кабелі доти, доки в черзі не залишиться тільки один кабель
    while len(cables) > 1:
        # Беремо два кабелі з найменшою довжиною
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)
        
        # Об'єднуємо їх та обчислюємо витрати
        new_cable = cable1 + cable2
        total_cost += new_cable
        
        # Додаємо новий кабель до черги
        heapq.heappush(cables, new_cable)
    
    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
min_cost = min_cost_to_connect_cables(cables)
print("Мінімальні витрати на об'єднання кабелів:", min_cost)
