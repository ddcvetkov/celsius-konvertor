import random

def poznai_chisloto():
    tajno_chislo = random.randint(1, 100)
    opiti = 0

    print("🎯 Игра: Познай числото (от 1 до 100)")

    while True:
        vhod = input("Въведи число: ")

        if not vhod.isdigit():
            print("⚠️ Моля, въведи цяло число.")
            continue

        poznaeto = int(vhod)
        opiti += 1

        if poznaeto < tajno_chislo:
            print("🔼 По-голямо е!")
        elif poznaeto > tajno_chislo:
            print("🔽 По-малко е!")
        else:
            print(f"✅ Браво! Позна числото {tajno_chislo} за {opiti} опита.")
            break

if __name__ == "__main__":
    poznai_chisloto()
