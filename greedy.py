def greedy_algorithm(items, budget):
    """
    Жадібний алгоритм для вибору страв, максимізуючи співвідношення калорій до вартості.
    
    :param items: Словник, де ключ — назва страви, а значення — словник з "cost" і "calories".
                  Наприклад:
                  {
                      "pizza": {"cost": 50, "calories": 300},
                      ...
                  }
    :param budget: Обмеження бюджету (ціле число).
    :return: Кортеж (chosen_items, total_calories, total_cost)
             chosen_items - список вибраних страв,
             total_calories - загальна калорійність обраних страв,
             total_cost - загальна вартість обраних страв.
    """
    # Створюємо список елементів із співвідношенням калорій/вартість
    items_ratio = []
    for name, data in items.items():
        cost = data["cost"]
        calories = data["calories"]
        ratio = calories / cost  # співвідношення калорій до вартості
        items_ratio.append((name, cost, calories, ratio))
    
    # Сортуємо за спаданням співвідношення (чим більше, тим краща страва)
    items_ratio.sort(key=lambda x: x[3], reverse=True)
    
    chosen_items = []
    total_calories = 0
    total_cost = 0
    
    # Проходимо по відсортованих стравах та додаємо, якщо бюджет дозволяє
    for name, cost, calories, ratio in items_ratio:
        if total_cost + cost <= budget:
            chosen_items.append(name)
            total_cost += cost
            total_calories += calories
    
    return chosen_items, total_calories, total_cost

def dynamic_programming(items, budget):
    """
    Алгоритм динамічного програмування для задачі 0/1 рюкзака.
    Задача: вибрати набір страв так, щоб сумарна вартість не перевищувала budget,
           а загальна калорійність була максимальною.
    
    :param items: Словник, де ключ — назва страви, а значення — словник з "cost" і "calories".
    :param budget: Обмеження бюджету.
    :return: Кортеж (chosen_items, total_calories, total_cost)
             chosen_items - список вибраних страв (оптимальний набір),
             total_calories - загальна калорійність,
             total_cost - загальна вартість обраних страв.
    """
    # Перетворимо словник в список для зручності перебору: (назва, cost, calories)
    items_list = [(name, data["cost"], data["calories"]) for name, data in items.items()]
    n = len(items_list)
    
    # Створюємо таблицю dp розміром (n+1) x (budget+1)
    # dp[i][w] — максимальна калорійність, яку можна отримати, використовуючи перші i страв при бюджеті w.
    dp = [[0]*(budget+1) for _ in range(n+1)]
    
    # Заповнюємо таблицю dp
    for i in range(1, n+1):
        name, cost, calories = items_list[i-1]
        for w in range(1, budget+1):
            if cost <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - cost] + calories)
            else:
                dp[i][w] = dp[i-1][w]
    
    # Реконструюємо набір вибраних страв
    w = budget
    chosen_items = []
    total_cost = 0
    for i in range(n, 0, -1):
        # Якщо поточне значення dp[i][w] відрізняється від dp[i-1][w],
        # це означає, що i-ий елемент був включений.
        if dp[i][w] != dp[i-1][w]:
            name, cost, calories = items_list[i-1]
            chosen_items.append(name)
            total_cost += cost
            w -= cost  # зменшуємо бюджет на вартість вибраної страви
    
    chosen_items.reverse()  # відновлюємо порядок вибору
    total_calories = dp[n][budget]
    
    return chosen_items, total_calories, total_cost

def main():
    # Вихідні дані про страви: кожна страва має вартість і калорійність
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    
    # Запит бюджету у користувача
    try:
        budget = int(input("Введіть бюджет: "))
    except ValueError:
        print("Будь ласка, введіть ціле число для бюджету.")
        return
    
    print("\n--- Жадібний алгоритм ---")
    greedy_result = greedy_algorithm(items, budget)
    print("Вибрані страви:", greedy_result[0])
    print("Загальна калорійність:", greedy_result[1])
    print("Загальна вартість:", greedy_result[2])
    
    print("\n--- Динамічне програмування ---")
    dp_result = dynamic_programming(items, budget)
    print("Вибрані страви:", dp_result[0])
    print("Загальна калорійність:", dp_result[1])
    print("Загальна вартість:", dp_result[2])

if __name__ == '__main__':
    main()