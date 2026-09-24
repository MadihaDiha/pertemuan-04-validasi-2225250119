a = float(input("Masukkan sudut A: "))
b = float(input("Masukkan sudut B: "))
c = float(input("Masukkan sudut C: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Sudut harus lebih dari 0.")
elif abs(a + b + c - 180) > 1e-9:
    print("Jumlah ketiga sudut harus 180 derajat.")
else:
    sudut_terbesar = max(a, b, c)

    if sudut_terbesar > 90:
        print("Segitiga tumpul")
    elif sudut_terbesar == 90:
        print("Segitiga siku-siku")
    else:
        print("Segitiga lancip")