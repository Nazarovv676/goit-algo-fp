import turtle
import math

def pythagoras_tree(t, size, level, branch_angle):
    """
    Рекурсивна функція для малювання фракталу "дерево Піфагора".
    
    :param t: екземпляр turtle.Turtle для малювання
    :param size: довжина сторони поточного квадрата
    :param level: рівень рекурсії (якщо level == 0, малювання завершується)
    :param branch_angle: кут повороту для лівої гілки (в градусах)
    """
    if level == 0:
        return

    # Збереження поточної позиції та кута (голови) turtle
    start = t.position()
    heading = t.heading()

    # Намалювати квадрат зі стороною size
    for _ in range(4):
        t.forward(size)
        t.left(90)

    # Обчислення векторів напрямку "вперед" та "вліво"
    theta = math.radians(heading)
    forward = (math.cos(theta), math.sin(theta))
    # Вектор, що повертається на 90 градусів вліво від напрямку руху
    left = (-math.sin(theta), math.cos(theta))

    # Обчислення координат верхнього лівого та верхнього правого кутів квадрата
    # top_left = початкова позиція + вектор "вліво" на довжину size
    top_left = (start[0] + size * left[0], start[1] + size * left[1])
    # top_right = top_left + вектор "вперед" на довжину size
    top_right = (top_left[0] + size * forward[0], top_left[1] + size * forward[1])

    # Обчислення розмірів для нових квадратів-гілок
    # Ліва гілка: сторона зменшується на cos(branch_angle)
    left_size = size * math.cos(math.radians(branch_angle))
    # Права гілка: сторона зменшується на sin(branch_angle)
    right_size = size * math.sin(math.radians(branch_angle))

    # Малювання лівої гілки
    t.penup()
    t.setposition(top_left)               # переходимо до верхнього лівого кута
    t.setheading(heading + branch_angle)    # обертаємо turtle на branch_angle вліво
    t.pendown()
    pythagoras_tree(t, left_size, level - 1, branch_angle)

    # Малювання правої гілки
    t.penup()
    t.setposition(top_right)              # переходимо до верхнього правого кута
    t.setheading(heading - (90 - branch_angle))  # обертаємо turtle на -(90 - branch_angle)
    t.pendown()
    pythagoras_tree(t, right_size, level - 1, branch_angle)

def main():
    # Налаштування вікна та turtle
    t = turtle.Turtle()
    t.speed(0)         # максимально швидке малювання
    t.hideturtle()     # приховуємо черепаху для чистоти малюнка

    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Фрактал 'Дерево Піфагора'")

    # Запит рівня рекурсії у користувача
    recursion_depth = int(screen.numinput("Рівень рекурсії", 
                                            "Введіть рівень рекурсії (наприклад, 5):", 
                                            default=5, minval=0, maxval=15))
    # Запит кута відхилення гілки
    branch_angle = float(screen.numinput("Кут гілки", 
                                           "Введіть кут гілки (в градусах, наприклад, 45):", 
                                           default=45, minval=0, maxval=90))

    # Початкова позиція та параметри
    initial_size = 100
    t.penup()
    # Розташовуємо дерево так, щоб його нижня частина була внизу екрану;
    # оскільки функція малює квадрат, початкова точка буде його нижнім лівим кутом.
    t.setposition(-initial_size/2, -250)
    t.setheading(0)    # turtle дивиться праворуч
    t.pendown()

    # Викликаємо рекурсивну функцію для малювання фракталу
    pythagoras_tree(t, initial_size, recursion_depth, branch_angle)

    turtle.done()

if __name__ == '__main__':
    main()