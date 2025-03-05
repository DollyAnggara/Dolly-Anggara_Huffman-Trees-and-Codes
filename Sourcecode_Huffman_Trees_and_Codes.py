# Nama: Dolly Anggara
# NIM: 23343034
# Prodi: Informatika
# Matkul: Perancangan dan Analisis Algoritma (INF1.62.4001)

import heapq
from collections import defaultdict

# Membuat kelas untuk node pohon Huffman
class Node:
    def __init__(node, karakter, frekuensi):
        node.karakter = karakter  # Karakter
        node.frekuensi = frekuensi  # Frekuensi karakter
        node.kiri = None   # Pointer ke kiri
        node.kanan = None  # Pointer ke kanan

    # Membuat perbandingan antar node untuk kepentingan heapq (priority queue)
    def __lt__(node, node_lain):
        return node.frekuensi < node_lain.frekuensi

# Fungsi untuk membangun pohon Huffman
def buat_pohon_huffman(teks):
    # Menghitung frekuensi setiap karakter
    frekuensi = defaultdict(int)
    for karakter in teks:
        frekuensi[karakter] += 1

    # Membuat heap (priority queue) dari node pohon
    heap = [Node(karakter, frekuensi) for karakter, frekuensi in frekuensi.items()]
    heapq.heapify(heap)

    # Membangun pohon Huffman
    while len(heap) > 1:
        kiri = heapq.heappop(heap)  # Ambil node dengan frekuensi terendah
        kanan = heapq.heappop(heap)  # Ambil node dengan frekuensi terendah kedua

        # Gabungkan dua node tersebut menjadi satu node baru
        gabungan = Node(None, kiri.frekuensi + kanan.frekuensi)
        gabungan.kiri = kiri
        gabungan.kanan = kanan

        # Masukkan node gabungan ke dalam heap
        heapq.heappush(heap, gabungan)

    return heap[0]  # Mengembalikan akar pohon Huffman

# Fungsi untuk menghasilkan kode Huffman dari pohon
def buat_kode_huffman(node, kode="", kode_huffman={}):
    if node is not None:
        # Jika node adalah daun (memiliki karakter)
        if node.karakter is not None:
            kode_huffman[node.karakter] = kode

        # Lakukan rekursi pada anak kiri dan kanan
        buat_kode_huffman(node.kiri, kode + "0", kode_huffman)
        buat_kode_huffman(node.kanan, kode + "1", kode_huffman)

    return kode_huffman

# Fungsi utama untuk menjalankan algoritma Huffman
def encoding_huffman(teks):
    # Bangun pohon Huffman
    akar = buat_pohon_huffman(teks)

    # Hasilkan kode Huffman
    kode_huffman = buat_kode_huffman(akar)

    # Hasilkan hasil encoding berdasarkan kode Huffman
    teks_terkompresi = "".join(kode_huffman[karakter] for karakter in teks)

    return kode_huffman, teks_terkompresi

# Fungsi untuk mendekode pesan menggunakan kode Huffman
def decoding_huffman(teks_terkompresi, kode_huffman):
    # Membalik kode Huffman menjadi karakter
    kode_huffman_terbalik = {v: k for k, v in kode_huffman.items()}

    # Dekode pesan
    kode_saat_ini = ""
    teks_dekompresi = ""
    for bit in teks_terkompresi:
        kode_saat_ini += bit
        if kode_saat_ini in kode_huffman_terbalik:
            teks_dekompresi += kode_huffman_terbalik[kode_saat_ini]
            kode_saat_ini = ""

    return teks_dekompresi

print("\n=== Kompresi Teks dengan Algoritma Huffman ===")

# Input string dari pengguna
teks = input("Masukkan teks untuk dikodekan (encode): ")

# Encoding Huffman (proses kompresi)
kode_huffman, teks_terkompresi = encoding_huffman(teks)

# Output hasil encoding (encode)
print("\nKode Huffman untuk masing-masing karakter:")
for karakter, kode in kode_huffman.items():
    print(f"Karakter: {karakter} -> Kode Huffman: {kode}")

print(f"\nTeks setelah dikodekan (encode) menjadi bit: {teks_terkompresi}")

# Dekoding Huffman (proses dekompresi)
teks_dekompresi = decoding_huffman(teks_terkompresi, kode_huffman)
print(f"\nTeks setelah didekodekan (decode): {teks_dekompresi}")
