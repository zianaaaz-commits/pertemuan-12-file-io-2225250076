def baca_data(nama_file):
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()

                if not baris:
                    continue

                nim, teks_nilai = baris.split(",")

                try:
                    nilai = float(teks_nilai)
                    data.append((nim, nilai))
                except ValueError:
                    print(f"Baris dilewati: {baris}")

    except FileNotFoundError:
        print("File tidak ditemukan.")

    return data


def tulis_rekap(data, nama_file):
    if not data:
        print("Tidak ada data valid.")
        return

    jumlah = len(data)
    rata_rata = sum(nilai for nim, nilai in data) / jumlah
    minimum = min(nilai for nim, nilai in data)
    maksimum = max(nilai for nim, nilai in data)
    jumlah_lulus = sum(1 for nim, nilai in data if nilai >= 60)

    with open(nama_file, "w", encoding="utf-8") as file:
        file.write(f"Jumlah data valid: {jumlah}\n")
        file.write(f"Rata-rata: {rata_rata:.2f}\n")
        file.write(f"Minimum: {minimum:.2f}\n")
        file.write(f"Maksimum: {maksimum:.2f}\n")
        file.write(f"Jumlah lulus: {jumlah_lulus}\n")


def main():
    data = baca_data("data/nilai.txt")
    tulis_rekap(data, "data/hasil_rekap.txt")
    print("Rekap ditulis ke data/hasil_rekap.txt")


if __name__ == "__main__":
    main()