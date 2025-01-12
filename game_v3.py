import random

def binary_search_guess(predict_number, low=1, high=1000):
    """Функция для угадывания числа с использованием бинарного поиска."""
    count = 0

    while low <= high:
        count += 1
        # Находим середину диапазона
        guess = (low + high) // 2
        

        # Проверяем угадали ли число
        if guess == predict_number:            
            break
        elif guess < predict_number:
            low = guess + 1  # Число больше текущей догадки
        else:
            high = guess - 1  # Число меньше текущей догадки

        
    return count


def evaluate_algorithm(low=1, high=1000):

    total_attempts = 0
    num_tests = high - low + 1

    for number in range(low, high + 1):
        total_attempts += binary_search_guess(number, low, high)

    return total_attempts / num_tests


# Пример вызова функции и оценки алгоритма
if __name__ == "__main__":
    predict_number = random.randint(1, 1000)
    attempts = binary_search_guess(predict_number)
    print(f"Число {predict_number} угадано за {attempts} попыток.")

    average_attempts = evaluate_algorithm()
    print(f"Среднее количество попыток: {average_attempts:.2f}")
