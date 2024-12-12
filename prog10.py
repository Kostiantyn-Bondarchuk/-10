import random
import string
import logging

# Налаштування логування
logging.basicConfig(
    filename="fuzz_test.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)


def fuzz_input_generator(max_length=100):
    """Генерує випадковий вхідний рядок."""
    length = random.randint(1, max_length)
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation + "\n\t", k=length))


def test_function(input_string):
    """Цільова функція для тестування."""
    # Зразкова функція для прикладу (замінити на власну функцію)
    return len(input_string) if "error" not in input_string.lower() else int(input_string)


def fuzz_test(target_function, iterations=1000):
    """Виконує fuzz-тестування заданої функції."""
    for i in range(iterations):
        try:
            # Генерація випадкових вхідних даних
            fuzz_input = fuzz_input_generator()

            # Виклик цільової функції
            result = target_function(fuzz_input)

            # Запис результатів у журнал (при бажанні)
            logging.info(f"Тест #{i + 1}: Вхідні дані: {repr(fuzz_input)}, Результат: {result}")
        except Exception as e:
            # Логування помилок
            logging.error(f"Тест #{i + 1}: Вхідні дані: {repr(fuzz_input)}, Помилка: {e}")
            print(f"Помилка на тесті #{i + 1}. Деталі записані у журнал.")


if __name__ == "__main__":
    iterations = int(input("Введіть кількість ітерацій для fuzz-тестування: ") or 1000)
    fuzz_test(test_function, iterations)
