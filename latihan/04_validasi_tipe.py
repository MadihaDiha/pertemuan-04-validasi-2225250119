try:
    benar = int(input("Jumlah jawaban benar (0-20): "))

    if benar < 0 or benar > 20:
        print("Jumlah harus antara 0 dan 20.")
    else:
        persentase = (benar / 20) * 100

        if persentase >= 75:
            status = "Tuntas"
        else:
            status = "Belum tuntas"

        print(f"Persentase: {persentase:.2f}%")
        print(f"Status: {status}")

except ValueError:
    print("Input harus berupa angka.")