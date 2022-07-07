#1
def cetakSiku(x):
    for i in range (1,x+1):
        print ('*'*i)

#2
def gambarlahPersegiEmpat(a,b):
    for i in range (a):
        if i==0 or i==a-1:
            print (b * '@')
        else:
            print ('@' + ' ' * (b-2) + '@')

#3a
def jumlahHurufVokal (huruf):
    vokal = 'aiueoAIUEO'
    a = 0
    hasil = 0
    for i in huruf:
        if i in vokal:
            a += len(i)
        else:
            a +=0
    hasil = 'Banyak huruf, ', len(huruf), 'dengan huruf vokal ', a
    return hasil

#3b
def jumlahHurufKonsonan (huruf):
    konsonan = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    b = 0
    hasil = 0
    for i in huruf:
        if i in konsonan:
            b +=len(i)
        else:
            b += 0
    hasil = 'Banyak huruf, ', len(huruf), 'dengan huruf vokal ', b
    return hasil

#4
def rerata(b):
    return sum(b)/len(b)

#5
from math import sqrt as sq
def apakahPrima(n):
    n = int(n)
    assert n>=0
    primaKecil = [2,3,5,7,9,11]
    bukanPrKecil = [0,1,4,6,8,9,10]
    if n in primaKecil:
        return True
    elif n in bukanPrKecil:
        return False
    else:
        for i in range(2,int(sq(n))+1):
            if n%i==0:
                return False
        return True

#6
def bilanganPrima(n):
    for i in range(2,n):
        prima = True
        for j in range (2,i):
            if(i%j==0):
                prima = False
        if (prima):
            print(i)

#7
def faktorPrima(x):
    bilanganList = []
    loop = 2
    while loop <= x:
        if x%loop == 0:
            x/=loop
            bilanganList.append(loop)
        else:
            loop +=1
    return bilanganList

#8
def apakahTerkandung(a,b):
    x = True
    for i in range(len(b)):
        if a in b:
            x = True
        else:
            x = False
    return x

#9
def kelipatan(x):
    for i in range(x):
        if(i<=0):
            pass
        elif(i%3==0 and i%5==0):
            print ('Python UMS')
        elif(i%3==0):
            print ('Python')
        elif(i%5==0):
            print ('UMS')
        else:
            print (i)

#10
from math import sqrt as akar
def selesaikanABC(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    D = float(b**2 - 4*a*c)
    if (D<0):
        hasil = "Determinannya negatif, persamaan tidak mempunyai akar real."
        return hasil
    else:
        x1 = (-b + akar(D))/(2*a)
        x2 = (-b - akae(D))/(2*a)
        hasil = (x1,x2)
        return hasil

#11
def apakahKabisat(tahun):
    hasil = False
    if(tahun%4==0 and tahun%100!=0 and tahun%400!=0):
        hasil = True
    elif(tahun%100==0 and tahun%400!=0):
        hasil = False
    elif(tahun%400==0):
        hasil = True
    else:
        hasil = False
    return hasil

#12
import random
def tebak():
    a = random.randrange(1,101,1)
    b = -1
    n = 0
    print ('Permainan Tebak Angka')
    print ('Saya Menyimpan Sebuah Angka Bulat Antara 1 Sampai 100.')
    while a != b:
        n = n + 1
        b = int (input('Masukkan tebakan ke- ' + str(n) + ':> '))
        if b < a:
            print ('Itu Terlalu Kecil, Coba Lagi')
        elif b > a:
            print ('Itu Terlalu Besar, Coba Lagi')
        else:
            print ('Ya, Anda Benar')
            break

#13
def katakan(bilangan):
    angka=['','Satu','Dua','Tiga','Empat','Lima','Enam',
           'Tujuh','Delapan','Sembilan','Sepuluh','Sebelas']
    Hasil =' '
    n = int(bilangan)
    if (n >= 0 and n <= 11):
        Hasil = Hasil + angka[n]
    elif (n < 20):
        Hasil = katakan(n % 10) + ' Belas'
    elif (n < 100):
        Hasil = katakan(n / 10) + ' Puluh' + katakan(n % 10)
    elif (n < 200):
        Hasil = ' Seratus' + katakan(n-100)
    elif (n < 1000):
        Hasil = katakan(n / 100) + ' Ratus' + katakan(n % 100)
    elif (n < 2000):
        Hasil = ' Seribu' + katakan(n-1000)
    elif (n < 10000):
        Hasil = katakan(n / 1000) + ' Ribu' + katakan(n % 1000)
    elif (n < 20000):
        Hasil = ' Sepuluh Ribu' + katakan(n-10000)
    elif (n < 100000):
        Hasil = katakan(n / 10000) + ' Puluh' + katakan(n % 10000)
    elif (n < 200000):
        Hasil = ' Seratus' + katakan(n-100000)
    elif (n < 1000000):
        Hasil = katakan(n / 100000) + ' Ratus' + katakan(n % 100000)
    elif (n < 2000000):
        Hasil = ' Satu Juta' + katakan(n-1000000)
    elif (n < 10000000):
        Hasil = katakan(n / 1000000) + ' Juta' + katakan(n % 1000000)
    elif (n < 10000000):
        Hasil = ' Satu Milyar' + katakan(n % 10000000)
    else:
        Hasil = 'Angka hanya sampai satu milyar'
    return Hasil

#14
def formatRupiah(bilangan):
    y = str(bilangan)
    if len(y) <= 3:
        return ('Rp ' + y)
    else:
        p = y[-3:]
        q = y[:-3]
        return formatRupiah(q) + '.' + p
        print ('Rp' + formatRupiah(q) + '.' + p)
