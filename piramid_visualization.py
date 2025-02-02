import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Колір вузла (для візуалізації)
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """
    Рекурсивно додає вузли та ребра з дерева до графа, обчислюючи координати.
    """
    if node is not None:
        # Додаємо вузол до графа з унікальним id, збереженням кольору та мітки (значення)
        graph.add_node(node.id, color=node.color, label=node.val)
        
        # Якщо є лівий нащадок, додаємо ребро і обчислюємо позицію
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer  # зміщення по осі X для лівої гілки
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        
        # Якщо є правий нащадок, додаємо ребро і обчислюємо позицію
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer  # зміщення по осі X для правої гілки
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    """
    Створює граф за допомогою NetworkX та малює дерево за допомогою matplotlib.
    """
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}  # Початкова позиція кореня
    tree = add_edges(tree, tree_root, pos)
    
    # Підготовка списку кольорів і міток для вузлів
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def build_heap_tree(heap_list, color="skyblue"):
    """
    Побудова бінарного дерева (купового дерева) із заданого списку.
    
    :param heap_list: Список елементів, що представляє бінарну купу у порядку рівневого обходу.
    :param color: Колір вузлів для візуалізації.
    :return: Корінь побудованого дерева.
    """
    if not heap_list:
        return None
    
    # Створюємо вузли для кожного елемента списку
    nodes = [Node(val, color) for val in heap_list]
    n = len(nodes)
    
    # Для кожного вузла встановлюємо посилання на лівого та правого нащадків за правилами купи
    for i in range(n):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < n:
            nodes[i].left = nodes[left_index]
        if right_index < n:
            nodes[i].right = nodes[right_index]
    
    return nodes[0]  # Повертаємо корінь (елемент з індексом 0)

def main():
    # Приклад: бінарна купа, представлена списком (масивом)
    # Значення в списку можна вважати за елементи купи, впорядковані за правилами купи
    heap_list = [50, 30, 40, 10, 20, 35, 38, 5, 7, 15]
    
    # Будуємо дерево із купи
    heap_root = build_heap_tree(heap_list)
    
    # Візуалізуємо отримане дерево
    draw_tree(heap_root)

if __name__ == '__main__':
    main()