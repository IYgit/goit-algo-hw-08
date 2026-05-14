import heapq


def min_cost_connect_cables(cables: list[int]) -> tuple[int, list[tuple[int, int, int]]]:
    """
    Знаходить мінімальні витрати на об'єднання кабелів у один.

    Алгоритм (жадібний + мін-купа):
      1. Помістити всі довжини кабелів у мін-купу.
      2. Поки в купі більше одного елемента:
         а. Витягти два найкоротші кабелі.
         б. З'єднати їх — витрати = сума довжин.
         в. Додати витрати до загальної суми.
         г. Покласти новий кабель назад у купу.
      3. Повернути загальні витрати.

    Складність: O(n log n)
    """
    if not cables:
        return 0, []
    if len(cables) == 1:
        return 0, []

    heap = cables[:]
    heapq.heapify(heap)

    total_cost = 0
    steps = []

    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        cost = first + second
        total_cost += cost
        steps.append((first, second, cost))
        heapq.heappush(heap, cost)

    return total_cost, steps


def print_result(cables: list[int]) -> None:
    """Виводить кабелі, порядок об'єднання та мінімальні витрати."""
    total, steps = min_cost_connect_cables(cables)
    print(f"Кабелі: {cables}")
    print("Порядок об'єднання:")
    for i, (a, b, cost) in enumerate(steps, 1):
        print(f"  Крок {i}: {a} + {b} = {cost}")
    print(f"Мінімальні загальні витрати: {total}")


if __name__ == "__main__":
    print_result([4, 3, 2, 6])
    print()
    print_result([1, 2, 3, 4, 5])
    print()
    print_result([10, 20, 30])

