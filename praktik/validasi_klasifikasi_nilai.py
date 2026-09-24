try:
    ujian = float(input("Nilai ujian: "))
    tugas = float(input("Nilai tugas: "))
    kehadiran = float(input("Persentase kehadiran: "))

    if not (0 <= ujian <= 100):
        print("Nilai ujian harus antara 0 dan 100.")
    elif not (0 <= tugas <= 100):
        print("Nilai tugas harus antara 0 dan 100.")
    elif not (0 <= kehadiran <= 100):
        print("Persentase kehadiran harus antara 0 dan 100.")
    else:
        akhir = 0.6 * ujian + 0.4 * tugas

        if akhir >= 85:
            predikat = "A"
        elif akhir >= 70:
            predikat = "B"
        elif akhir >= 60:
            predikat = "C"
        elif akhir >= 50:
            predikat = "D"
        else:
            predikat = "E"

        if kehadiran < 80:
            status = "Tidak memenuhi syarat kehadiran"
        elif predikat in ["A", "B", "C"]:
            status = "Lulus"
        else:
            status = "Belum lulus"

        print(f"Nilai akhir: {akhir:.2f}")
        print(f"Predikat: {predikat}")
        print(f"Status: {status}")

except ValueError:
    print("Input harus berupa angka.")