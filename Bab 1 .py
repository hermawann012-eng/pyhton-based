luas = 20

tinggi = 40

satuan = "meter"
hh = luas * tinggi
gg = luas ** tinggi

hitung = hh / 2

hasil1 = print("Luas: ", hh, satuan)

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


match hitung:
    case 200 | 400 | 600:
        print ("saya makan")
    case 800:
        print("saya minum")