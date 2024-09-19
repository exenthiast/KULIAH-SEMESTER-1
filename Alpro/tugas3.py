def tampilkan_jadwal(hari):
    jadwal = {
        'Senin': 'Kuliah Algoritma Struktur Data jam 9',
        'Selasa': 'Kuliah Kalkulus 1 jam 7',
        'Rabu': 'Kuliah Algoritma Struktur Data jam 12',
        'Jumat': 'Kuliah Agama jam 9',
        'Sabtu': 'Libur',
        'Minggu': 'Libur'
    }
    
    kamis_jadwal = {
        '7-9': 'kuliah Pancasila di Filsafat',
        '9-10': 'kosong',
        '10-12': 'kuliah Bahasa Inggris I',
        '12-13': 'kosong',
        '13-15': 'kuliah Logika Informatika',
        '15-': 'kosong'
    }
    
    if hari == 'Kamis':
        print("Jadwal Kuliah untuk Kamis:")
        for waktu, mata_kuliah in kamis_jadwal.items():
            print(f"Jam {waktu}: {mata_kuliah}")
    elif hari in jadwal:
        print(f"Jadwal Kuliah untuk {hari}: {jadwal[hari]}")
    else:
        print("Hari tidak valid. Silakan masukkan hari yang valid (Senin, Selasa, Rabu, Kamis, Jumat, Sabtu, Minggu).")

hari = input("Masukkan hari: ").capitalize()
tampilkan_jadwal(hari)
