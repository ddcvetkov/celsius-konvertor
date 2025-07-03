def celsius_kam_fahrenheit(c):
    return (c * 9/5) + 32

def main():
    print("Конвертор: Целзий към Фаренхайт")
    try:
        c = float(input("Въведи температура в Целзий: "))
        f = celsius_kam_fahrenheit(c)
        print(f"{c}°C = {f:.2f}°F")
    except ValueError:
        print("Моля, въведи валидно число.")

if __name__ == "__main__":
    main()
