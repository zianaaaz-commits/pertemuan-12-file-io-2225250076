# Pertemuan 12 - File I/O dan Error Handling

Nama: Ziana Alfia Zahra  
NIM: 2225250076  
Kelas: 3A

## Tujuan

Membaca, memvalidasi, mengolah, dan menulis data file dengan Python.

## Format File Input

File `data/nilai.txt` berisi NIM dan nilai mahasiswa dengan format `NIM,nilai`.

Contoh isi file:

```text
A001,85
A002,78
A003,92
A004,abc
A005,74
A006,88
```

## Cara Menjalankan

Jalankan perintah berikut melalui terminal dari folder utama proyek:

```bash
python3 tugas/rekap_nilai_file.py
```

## Error yang Ditangani

- `FileNotFoundError`
- `ValueError`

## Test Case

| Kasus | Kondisi | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| Normal | Semua baris valid. | Semua record diproses dan rekap benar. | Semua record valid diproses dan rekap berhasil ditulis. | Berhasil |
| File hilang | `nilai.txt` tidak tersedia. | Pesan file tidak ditemukan; program tidak crash. | Pesan file tidak ditemukan ditampilkan dan program tidak crash. | Berhasil |
| Nilai invalid | `A004,abc`. | Baris invalid dilewati/dilaporkan; record lain tetap diproses. | Baris `A004,abc` dilewati dan record lain tetap diproses. | Berhasil |
| Baris kosong | Ada baris kosong. | Baris kosong dilewati. | Baris kosong dilewati dan proses tetap berjalan. | Berhasil |
| Batas lulus | Nilai 60. | Dihitung sebagai lulus. | Nilai 60 dihitung sebagai lulus. | Berhasil |

## Refleksi

Saya menemukan error `ValueError` ketika program membaca nilai yang bukan angka. Program menangani error tersebut dengan melewati baris yang tidak valid sehingga data lainnya tetap dapat diproses.