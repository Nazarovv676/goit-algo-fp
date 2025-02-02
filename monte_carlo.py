import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_trials):
    """
    Імітує кидки двох кубиків num_trials разів.
    
    :param num_trials: Кількість кидків кубиків.
    :return: Словник, де ключ – сума (від 2 до 12), а значення – кількість разів, коли ця сума випала.
    """
    # Ініціалізуємо словник для підрахунку сум від 2 до 12
    frequencies = {sum_val: 0 for sum_val in range(2, 13)}
    
    for _ in range(num_trials):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        s = die1 + die2
        frequencies[s] += 1
        
    return frequencies

def main():
    # Кількість кидків кубиків (чим більше, тим точніше симуляція)
    num_trials = 1_000_000
    
    # Отримуємо частоти появи кожної суми за допомогою методу Монте-Карло
    frequencies = simulate_dice_rolls(num_trials)
    
    # Обчислюємо імовірності для кожної суми
    monte_probabilities = {s: freq / num_trials for s, freq in frequencies.items()}
    
    # Аналітичні ймовірності для двох кубиків (загальна кількість варіантів = 36)
    analytic_probabilities = {
        2: 1/36,
        3: 2/36,
        4: 3/36,
        5: 4/36,
        6: 5/36,
        7: 6/36,
        8: 5/36,
        9: 4/36,
        10: 3/36,
        11: 2/36,
        12: 1/36
    }
    
    # Вивід таблиці результатів
    print("Сума\tЧастота\tМонте-Карло ймовірність\tАналітична ймовірність")
    for s in range(2, 13):
        freq = frequencies[s]
        monte_prob = monte_probabilities[s]
        analytic_prob = analytic_probabilities[s]
        print(f"{s}\t{freq}\t{monte_prob:.4f}\t\t\t{analytic_prob:.4f}")
    
    # Підготовка даних для побудови графіку
    sums = list(range(2, 13))
    monte_probs = [monte_probabilities[s] for s in sums]
    analytic_probs = [analytic_probabilities[s] for s in sums]
    
    # Побудова графіку: стовпчиковий для Монте-Карло та лінійний для аналітичних значень
    plt.figure(figsize=(10, 6))
    plt.bar(sums, monte_probs, width=0.5, alpha=0.7, label="Монте-Карло")
    plt.plot(sums, analytic_probs, color="red", marker="o", linestyle="-", linewidth=2, markersize=8, label="Аналітичні")
    
    plt.xlabel("Сума на кубиках")
    plt.ylabel("Ймовірність")
    plt.title("Ймовірності сум при киданні двох кубиків")
    plt.xticks(sums)
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()