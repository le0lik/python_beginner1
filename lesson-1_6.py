a = float(input("Введите колисечтво километров в первый день:"))
b = float(input("Введите требуемое количество километров:"))

c = 1
while True:
    print(f"{c}-й день: {a}")

    if a >= b:
        break

    a += a / 10
    c += 1

print(f"На {c}-й день спортсмен достиг результата — не менее {b} км")
