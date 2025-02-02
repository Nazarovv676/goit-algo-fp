import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# =============================================================================
# Клас вузла та функції для побудови й візуалізації дерева (базова частина)
# =============================================================================
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Початковий колір вузла (буде змінено під час обходу)
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """
    Рекурсивно додає вузли та ребра до графа для візуалізації.
    Обчислює координати вузлів для красивого розташування.
    """
    if node is not None:
        # Додаємо вузол з його унікальним id, збереженням кольору та мітки (значення)
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / (2 ** layer)
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / (2 ** layer)
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, title="Binary Tree"):
    """
    Побудова графа (використовуючи NetworkX) та візуалізація дерева за допомогою matplotlib.
    """
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    
    # Отримуємо список кольорів та міток для вузлів
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    
    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def build_heap_tree(heap_list, color="skyblue"):
    """
    Будує бінарне дерево (як для бінарної купи) із заданого списку.
    Для вузла з індексом i:
      - Лівий нащадок має індекс 2*i + 1
      - Правий нащадок має індекс 2*i + 2
    """
    if not heap_list:
        return None
    nodes = [Node(val, color) for val in heap_list]
    n = len(nodes)
    for i in range(n):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < n:
            nodes[i].left = nodes[left_index]
        if right_index < n:
            nodes[i].right = nodes[right_index]
    return nodes[0]

def count_nodes(root):
    """
    Рахує кількість вузлів у дереві, використовуючи ітеративний обхід (BFS).
    """
    if not root:
        return 0
    count = 0
    queue = deque([root])
    while queue:
        node = queue.popleft()
        count += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return count

# =============================================================================
# Функція для генерації кольору за порядком обходу (градієнт від темного до світлого)
# =============================================================================
def get_gradient_color(order, total, start_color=(10, 50, 100), end_color=(230, 240, 255)):
    """
    Обчислює колір у форматі hex (16-система) за допомогою лінійної інтерполяції між
    start_color (темний відтінок) та end_color (світлий відтінок).
    
    :param order: Поточний номер відвідування вузла (0-індексований).
    :param total: Загальна кількість вузлів, що будуть відвідані.
    :param start_color: Початковий (темний) колір у вигляді кортежу (R, G, B).
    :param end_color: Кінцевий (світлий) колір у вигляді кортежу (R, G, B).
    :return: Рядок з кольором у hex-форматі, наприклад, "#1296F0".
    """
    if total <= 1:
        ratio = 1
    else:
        ratio = order / (total - 1)
    r = int(start_color[0] + ratio * (end_color[0] - start_color[0]))
    g = int(start_color[1] + ratio * (end_color[1] - start_color[1]))
    b = int(start_color[2] + ratio * (end_color[2] - start_color[2]))
    return f"#{r:02X}{g:02X}{b:02X}"

# =============================================================================
# Ітеративні алгоритми обходу: DFS (в глибину) та BFS (в ширину)
# (НЕ використовується рекурсія)
# =============================================================================
def iterative_dfs(root):
    """
    Ітеративний обхід дерева в глибину (DFS) з використанням стека.
    Під час обходу вузлам присвоюється колір згідно з порядком відвідування.
    """
    if root is None:
        return
    total = count_nodes(root)
    stack = [root]
    order = 0
    while stack:
        node = stack.pop()  # вилучаємо вузол з вершини стека
        # Призначаємо вузлу унікальний колір згідно з його порядком
        node.color = get_gradient_color(order, total)
        order += 1
        # Для префіксного обходу в глибину спочатку додаємо правий, потім лівий вузол
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def iterative_bfs(root):
    """
    Ітеративний обхід дерева в ширину (BFS) з використанням черги.
    Під час обходу вузлам присвоюється колір згідно з порядком відвідування.
    """
    if root is None:
        return
    total = count_nodes(root)
    queue = deque([root])
    order = 0
    while queue:
        node = queue.popleft()  # вилучаємо вузол з початку черги
        node.color = get_gradient_color(order, total)
        order += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# =============================================================================
# Основна функція
# =============================================================================
def main():
    # Приклад: побудова бінарного дерева із списку (представлення купи)
    heap_list = [50, 30, 40, 10, 20, 35, 38, 5, 7, 15]
    
    # Для демонстрації створюємо дві копії дерева:
    # одна для обходу в глибину (DFS), інша — для обходу в ширину (BFS)
    tree_dfs = build_heap_tree(heap_list, color="gray")
    tree_bfs = build_heap_tree(heap_list, color="gray")
    
    # Ітеративний обхід в глибину (DFS)
    iterative_dfs(tree_dfs)
    draw_tree(tree_dfs, title="Ітеративний обхід в глибину (DFS)")
    
    # Ітеративний обхід в ширину (BFS)
    iterative_bfs(tree_bfs)
    draw_tree(tree_bfs, title="Ітеративний обхід в ширину (BFS)")

if __name__ == '__main__':
    main()