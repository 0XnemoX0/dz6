# task6_corect_code.py

result = []

def divider(a, b):
    if a < b:
        raise ValueError("a менше ніж b")
    if b > 100:
        raise IndexError("b більше 100")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}  # без []

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except Exception as e:
        print(f"Виникла помилка: {type(e).__name__} — {e}")

print("\nРезультат роботи програми:")
print(result)
