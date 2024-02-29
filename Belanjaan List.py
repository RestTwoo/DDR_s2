product = {
    "caffe americano": 37000,
    "caramelmachiato": 59000,
    "asian docle latte": 55000,
    "caramel latte": 52000,
    "vanilla latte": 52000,
    "caffe latte": 48000,
    "cappucino": 48000,
    "caffe mocha": 55000, 
}

def belanja():
    print("Selamat datang, selamat berbelanja")
    print("Berikut adalah daftar barang yang tersedia:")
    for minum, harga in product.items():
        print(f"{minum}: Rp{harga} per cup") 
        
    total_belanja = 0
    while True:
        minum_dipilih = input("Masukkan nama minu yang ingin anda beli(atau 'selesai' untuk selesai)").lower()
        if minum_dipilih.lower() == 'selesai':
             break
        if minum_dipilih not in product:
            print("Maaf, barang tersebut tidak tersedia")
            continue
        jumlah = float(input(f"Berapa cup {minum_dipilih} yang anda inginkan?"))
        total_belanja += product[minum_dipilih] * jumlah

    print(f"total Belanja anda adalah: Rp{total_belanja}")

    ppn = total_belanja * 0.1
    print(f"ppn 10%: Rp{ppn:.2f}")

    if total_belanja > 350000:
        diskon = total_belanja * 0.15
        print(f"diskon 15% Rp{diskon:.2f}")
        total_belanja -= diskon
        print(f"total belanja anda setelah pajak dan diskon: {total_belanja - ppn - diskon}")
         
belanja()
