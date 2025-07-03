def celsius_kam_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_kam_celsius(f):
    return (f - 32) * 5/9

def main():
    while True:
        print("\nКонвертор на температури:")
        print("1. Целзий → Фаренхайт")
        print("2. Фаренхайт → Целзий")
        print("3. Изход")

        izbor = input("Избери опция (1/2/3): ")

        if izbor == "1":
            try:
                c = float(input("Въведи температура в Целзий: "))
                f = celsius_kam_fahrenheit(c)
                print(f"{c}°C = {f:.2f}°F")
            except ValueError:
                print("⚠️ Невалидно число.")

        elif izbor == "2":
            try:
                f = float(input("Въведи температура във Фаренхайт: "))
                c = fahrenheit_kam_celsius(f)
                print(f"{f}°F = {c:.2f}°C")
            except ValueError:
                print("⚠️ Невалидно число.")

        elif izbor == "3":
            print("Изход. Довиждане!")
            break

        else:
            print("⚠️ Невалиден избор. Опитай отново.")

if __name__ == "__main__":
    main()
