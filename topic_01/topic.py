# --- ЗАВДАННЯ 1: Обернути рядок ---
original_str = "abcdefg123"
# Використовуємо зріз (slicing) з кроком -1 для розвороту
reversed_str = original_str[::-1]

print(f"1. Оригінал: {original_str}")
print(f"   Результат: {reversed_str}")
print("-" * 30)

# --- ЗАВДАННЯ 2: Тестування функцій рядків ---
print("2. Тестування методів рядків:")

# Для strip() створимо рядок із пробілами
text_spaces = "   abcdefg123   "
print(f"   strip(): '{text_spaces.strip()}' (видаляє пробіли з країв)")

# Для інших методів візьмемо тестовий рядок
text_test = "hello python world"

print(f"   capitalize(): '{text_test.capitalize()}' (перша літера велика, інші малі)")
print(f"   title():      '{text_test.title()}' (перші літери кожного слова великі)")
print(f"   upper():      '{text_test.upper()}' (всі літери великі)")
print(f"   lower():      '{text_test.upper().lower()}' (всі літери малі)")
print("-" * 30)

# --- ЗАВДАННЯ 3: Функція пошуку дискримінанту ---
def calc_discriminant(a, b, c):
    """
    Функція обчислює дискримінант квадратного рівняння
    за формулою: D = b^2 - 4ac
    """
    D = b**2 - 4*a*c
    return D

# Приклад використання: 2x^2 + 5x - 3 = 0
# a = 2, b = 5, c = -3
a, b, c = 2, 5, -3
disc = calc_discriminant(a, b, c)

print(f"3. Дискримінант для a={a}, b={b}, c={c}:")
print(f"   D = {disc}")