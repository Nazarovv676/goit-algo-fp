import heapq

def dijkstra(graph, start):
    """
    Алгоритм Дейкстри для пошуку найкоротших шляхів у зваженому графі.
    
    :param graph: Словник, що представляє граф, де ключ — вершина, 
                  а значення — список кортежів (сусідня_вершина, вага_ребра).
    :param start: Початкова вершина.
    :return: Кортеж (distances, previous), де:
             - distances — словник, що містить найкоротшу відстань від start до кожної вершини;
             - previous — словник для відновлення шляху: для кожної вершини зберігається попередня вершина на шляху.
    """
    # Ініціалізуємо відстані: для всіх вершин – безкінечність, для стартової – 0.
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # Словник для збереження попередників (для відновлення шляху).
    previous = {vertex: None for vertex in graph}

    # Ініціалізуємо бінарну купу (пріоритетну чергу) з кортежем (відстань, вершина)
    heap = [(0, start)]
    
    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        # Якщо знайдена відстань більша за вже збережену, то пропускаємо (застаріла інформація)
        if current_distance > distances[current_vertex]:
            continue

        # Перебираємо сусідів поточної вершини
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # Якщо знайшли коротший шлях до сусіда, оновлюємо інформацію
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(heap, (distance, neighbor))
    
    return distances, previous

def print_path(previous, start, target):
    """
    Рекурсивна функція для виведення шляху від start до target,
    використовуючи інформацію про попередників (previous).
    """
    if target == start:
        print(start, end='')
    elif previous[target] is None:
        print(f"Немає шляху від {start} до {target}", end='')
    else:
        print_path(previous, start, previous[target])
        print(" -> " + str(target), end='')

def main():
    # Створюємо зважений граф. Кожна вершина має список суміжних вершин
    # у вигляді кортежів (сусід, вага ребра).
    graph = {
        'A': [('B', 5), ('C', 1)],
        'B': [('A', 5), ('C', 2), ('D', 1)],
        'C': [('A', 1), ('B', 2), ('D', 4), ('E', 8)],
        'D': [('B', 1), ('C', 4), ('E', 3), ('F', 6)],
        'E': [('C', 8), ('D', 3)],
        'F': [('D', 6)]
    }

    # Вкажемо початкову вершину для алгоритму Дейкстри.
    start_vertex = 'A'
    distances, previous = dijkstra(graph, start_vertex)

    # Виведемо найкоротші відстані від початкової вершини до всіх інших
    print("Найкоротші відстані від вершини", start_vertex)
    for vertex in graph:
        print(f"Відстань до вершини {vertex}: {distances[vertex]}")

    # Виведемо відновлені шляхи від початкової вершини до кожної з вершин
    print("\nШляхи від вершини", start_vertex)
    for vertex in graph:
        print(f"Шлях до {vertex}: ", end='')
        if distances[vertex] == float('inf'):
            print("Немає шляху")
        else:
            print_path(previous, start_vertex, vertex)
            print()

if __name__ == '__main__':
    main()