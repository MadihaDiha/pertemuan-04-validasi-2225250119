# Pertemuan 04 — Seleksi Multi-Kondisi dan Validasi Input dalam Python

**Nama:** Madiha
**NIM:** 2225250119
**Program Studi:** S1 Pendidikan Matematika
**Mata Kuliah:** Algoritma dan Pemrograman

## Deskripsi

Project ini merupakan tugas pada mata kuliah **Algoritma dan Pemrograman** yang membahas penggunaan seleksi multi-kondisi dengan `if-elif-else` serta validasi input dalam Python.

Materi yang dipraktikkan meliputi:

* Seleksi multi-kondisi menggunakan `if`, `elif`, dan `else`.
* Validasi nilai berdasarkan rentang tertentu.
* Validasi tipe input menggunakan `try-except`.
* Klasifikasi bilangan.
* Klasifikasi sudut dan segitiga.
* Klasifikasi nilai akhir dan status kelulusan.

## Struktur Project

```text
pertemuan-04-validasi-NIM/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_predikat_nilai.py
│   ├── 02_kategori_bilangan.py
│   ├── 03_validasi_rentang.py
│   ├── 04_validasi_tipe.py
│   └── 05_klasifikasi_segitiga_sudut.py
└── praktik/
    └── validasi_klasifikasi_nilai.py
```

## Daftar Latihan

### 1. Predikat Nilai

File:
`latihan/01_predikat_nilai.py`

Program menerima nilai akhir dan menentukan predikat:

| Rentang Nilai | Predikat |
| ------------- | -------- |
| ≥ 85          | A        |
| ≥ 70          | B        |
| ≥ 60          | C        |
| ≥ 50          | D        |
| < 50          | E        |

### 2. Kategori Bilangan

File:
`latihan/02_kategori_bilangan.py`

Program mengelompokkan bilangan bulat menjadi:

* Bilangan negatif
* Nol
* Bilangan positif genap
* Bilangan positif ganjil

### 3. Validasi Rentang

File:
`latihan/03_validasi_rentang.py`

Program memeriksa apakah sudut berada pada rentang **lebih dari 0° dan kurang dari 180°**. Jika valid, sudut diklasifikasikan menjadi:

* Sudut lancip
* Sudut siku-siku
* Sudut tumpul

### 4. Validasi Tipe Input

File:
`latihan/04_validasi_tipe.py`

Program menerima jumlah jawaban benar dari 20 soal. Input divalidasi agar:

* Berupa angka.
* Berada pada rentang 0–20.

Kemudian program menghitung persentase dan menentukan status:

* **Tuntas** jika persentase ≥ 75%.
* **Belum tuntas** jika persentase < 75%.

### 5. Klasifikasi Segitiga Berdasarkan Sudut

File:
`latihan/05_klasifikasi_segitiga_sudut.py`

Program menerima tiga sudut dan memeriksa:

* Setiap sudut harus lebih dari 0°.
* Jumlah ketiga sudut harus 180°.

Jika valid, segitiga diklasifikasikan menjadi:

* Segitiga lancip
* Segitiga siku-siku
* Segitiga tumpul

## Praktik

File:
`praktik/validasi_klasifikasi_nilai.py`

Program menerima:

* Nilai ujian
* Nilai tugas
* Persentase kehadiran

Nilai akhir dihitung dengan rumus:

```text
Nilai akhir = 60% × nilai ujian + 40% × nilai tugas
```

Program kemudian menentukan predikat A–E dan status kelulusan berdasarkan nilai akhir serta persentase kehadiran.

Jika kehadiran kurang dari **80%**, statusnya adalah:

```text
Tidak memenuhi syarat kehadiran
```

## Cara Menjalankan Program

Pastikan Python sudah terpasang pada komputer.

Buka terminal di VS Code, kemudian jalankan salah satu file dengan perintah:

```bash
python latihan/01_predikat_nilai.py
```

Contoh untuk file praktik:

```bash
python praktik/validasi_klasifikasi_nilai.py
```

## Kesimpulan

Melalui project ini, mahasiswa mempraktikkan penggunaan **seleksi multi-kondisi** dan **validasi input** dalam Python untuk menyelesaikan berbagai permasalahan sederhana.
