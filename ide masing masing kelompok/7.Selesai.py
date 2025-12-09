# fix masing masing ide
# alpa,ripal,zidan,ipan 
# menggunakan for i 
class pegawai:
    def __init__(self,nama,bagian):
        self.nama = nama 
        self.bagian = bagian
    def output(self):
        print("Nama anda =",self.nama)
        print("Bagian    =",self.bagian)
        
class manajer(pegawai):
    def __init__(self,nama,bagian,gaji,bonus):
        super().__init__(nama,bagian)
        self.gaji = gaji 
        self.bonus = bonus 
    def output(self):
        super().output()
        print("Gaji  =",self.gaji)
        print("Bonus =",self.bonus)
        print("Total =",self.bonus + self.gaji)
class programmer(pegawai):
    def __init__(self,nama,bagian,gaji,bonus):
        super().__init__(nama,bagian)
        self.gaji = gaji
        self.bonus = bonus
    def output(self):
        super().output()
        print("Gaji    =",self.gaji)
        print("Bonus   =",self.bonus)
        print("Total   =",self.gaji + self.bonus)

# memanggil dengan metode for i (perulangan)
Pgawai_list[
manajer("dimas","manajer",200,100),
programmer("alfa","programmer",100,200),
manajer("ripal","manajer",200,120),
programmer("zidan","programmer",200,100)
]

for pegawai in Pgawai_list
    pegawai.output()
