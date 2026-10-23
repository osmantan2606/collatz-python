def collatz(number):
    if number % 2 == 0:
        result = number // 2  # çift
    else:
        result = 3 * number + 1  # tek
    print(result)
    return result


# Geçerli bir pozitif tam sayı alana kadar tekrar sor
while True:
    try:
        n = int(input("Pozitif bir tam sayı girin: "))
        if n > 0:
            break
        print("Sayı 0'dan büyük olmalı.")
    except ValueError:
        # Metin veya ondalıklı sayı girilirse int() hata verir
        print("Hata: Lütfen geçerli bir tam sayı girin.")

# Sonuç 1 olana kadar diziyi devam ettir ve adımları say
adim = 0
while n != 1:
    n = collatz(n)
    adim += 1
print("Toplam adım:", adim)
