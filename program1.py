print("Program menghitung laba dengan modal awal 100 juta")
print("")
print("Catatan")
print("Bulan pertama dan kedua = 0%")
print("Bulan ke 3 = 1%")
print("Bulan ke 5 = 5%")
print("Bulan ke 8 = 3%")
print("")
a = 100000000
for x in range(1,9):
    if (x>=1 and x<=2):
        b = a*0
        print("Laba bulan ke-",x," : ",b)
    if(x>=3 and x<=4):
        c = a*0.1
        print("Laba bulan ke-",x," : ",c)
    if(x>=5 and x<=6):
        d = a*0.5
        print("Laba bulan ke-",x," : ",d)
    if(x>=7 and x<=8):
        e = a*0.3
        print("Laba bulan ke-",x," : ",e)
total=b+b+c+c+d+d+d+e
print("Total : ",total)