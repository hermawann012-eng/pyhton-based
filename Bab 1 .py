
print ("Hello Users")


luas = 20
count = 0
target = 10000
tinggi = 40

satuan = "meter"
hh = luas * tinggi
gg = luas ** tinggi

hitung = hh / 2

hasil1 = print("Luas: \n", hh, satuan)

# kondisi if else
if (hh > 1000):
    print("Luas lebih dari 1000")
elif (hh < 1000):
    print("Luas kurang dari 1000")
elif (hh == 1000):
    print("Luas sama dengan 1000")
elif (gg > 1000):
    print("Pangkat luas lebih dari 1000")
elif (gg < 1000):
    print("Pangkat luas kurang dari 1000")

#kondisi dalam satu barus

kondisi = "Besar" if hh >= 200 else "Kecil"
print("Kondisi: ", kondisi, satuan)

# math case
match hitung:
    case 200 | 400 | 600:
        print ("saya makan")
    case 800:
        print("saya minum")

# kondisi while

while (tinggi < 100):
    print("hitunggg : ", count)
    count = count + 1
print("Beres", target)