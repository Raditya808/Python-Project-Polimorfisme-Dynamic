# ide kedua zidan menggunakan super().__init__ agar dapat dipanggil class paling awal 
# menggunakan metode class pewaris metode constructor

class Pegawai:
    def __init__(self, nama):
        self.nama = nama

    def gaji(self):
        return 0

class Manajer(Pegawai):
    def __init__(self, nama, bonus):
        super().__init__(nama)
        self.bonus = bonus

    def gaji(self):
        return f"{self.bonus}"


class Programer(Pegawai):
    def __init__(self, nama, project):
        super().__init__(nama)
        self.bonus_project = project

    def gaji(self):
        gaji_1project = 2000
        return f"{self.bonus_project + gaji_1project}"

def hitung_gaji(pegawai):
    print(f"Nama : {pegawai.nama}, Dengan Gaji : Rp{pegawai.gaji()}")


m1 = Manajer("zidane manajer", 2000)
p1 = Programer("radit programer", 300)

hitung_gaji(m1)
hitung_gaji(p1)
