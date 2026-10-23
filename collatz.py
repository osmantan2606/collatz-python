def collatz(number):
    if number % 2 == 0:
        result  = number // 2 # çift 
    else: 
        result = 3 * number + 1 # tek 
    print(result)
    return result 
while True: 
    try:  
        n = int(input("pozitif bir tam sayı girin"))
        if n > 0:
            break
        print("sayı 0'dan büyük olmalı" )
    except ValueError:  # metin ya da ondalıklı girilirse error verir
        print("hata:lütfen geçerli bir tam sayı girin") 
# sonuç 1 olana kadar diziyi devam ettirme 
# kaç adımda bulduğunu ekleme
adim = 0
while n !=1:  
    n =collatz(n)
    adim += 1
print("toplam adim",adim)         

