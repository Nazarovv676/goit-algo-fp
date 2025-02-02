class Node:
    """
    Клас для вузла однозв’язного списку.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head):
    """
    Функція для виведення списку.
    """
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

def reverse_list(head):
    """
    Функція для реверсування однозв’язного списку.
    Змінює посилання між вузлами так, що напрямок списку змінюється.
    """
    prev = None
    current = head
    while current:
        next_node = current.next  # зберігаємо наступний вузол
        current.next = prev       # змінюємо посилання: поточний вузол тепер вказує на попередній
        prev = current            # переходимо до наступного вузла
        current = next_node
    return prev  # нова голова списку

def merge_two_sorted_lists(l1, l2):
    """
    Функція для об'єднання двох відсортованих однозв’язних списків в один відсортований список.
    """
    dummy = Node(0)  # допоміжний вузол для спрощення злиття
    tail = dummy

    # Поки обидва списки не спустошено, вибираємо вузол з меншим значенням
    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # Додаємо залишок одного з списків (якщо є)
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    return dummy.next  # повертаємо об'єднаний список, пропускаючи dummy-вузол

def merge_sort(head):
    """
    Функція для сортування однозв’язного списку алгоритмом злиття.
    """
    # Базовий випадок: список порожній або містить один елемент
    if head is None or head.next is None:
        return head

    # Знаходимо середину списку (метод повзунів)
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Розділяємо список на дві частини
    mid = slow.next
    slow.next = None  # перериваємо зв'язок, утворюючи два окремих списки

    # Рекурсивно сортуємо обидві половини
    left = merge_sort(head)
    right = merge_sort(mid)

    # Об'єднуємо два відсортованих списки
    return merge_two_sorted_lists(left, right)

def create_linked_list(arr):
    """
    Функція для створення однозв’язного списку з Python-списку.
    """
    head = None
    tail = None
    for value in arr:
        new_node = Node(value)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    return head

# Приклад використання:
if __name__ == '__main__':
    # Створення списку з елементів
    arr = [4, 2, 5, 1, 3]
    head = create_linked_list(arr)
    print("Оригінальний список:")
    print_list(head)

    # Реверсування списку
    reversed_head = reverse_list(head)
    print("Реверсований список:")
    print_list(reversed_head)

    # Сортування списку за допомогою злиття
    sorted_head = merge_sort(reversed_head)
    print("Відсортований список:")
    print_list(sorted_head)

    # Створення двох відсортованих списків для демонстрації злиття
    list1 = create_linked_list([1, 3, 5, 7])
    list2 = create_linked_list([2, 4, 6, 8])
    print("Список 1:")
    print_list(list1)
    print("Список 2:")
    print_list(list2)

    # Об'єднання двох відсортованих списків в один відсортований список
    merged_head = merge_two_sorted_lists(list1, list2)
    print("Об'єднаний відсортований список:")
    print_list(merged_head)