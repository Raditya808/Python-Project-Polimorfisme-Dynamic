# tanpa return fix (ide radit)
# dan tanpa for i 

class pegawai:
    def __init__(self,nama,bagian):
        self.nama = nama
        self.bagian = bagian
    
class manajer(pegawai):
    def __init__(self,nama,bagian,gaji,bonus):
        super().__init__(nama,bagian)
        self.gaji = gaji 
        self.bonus = bonus 
    def output(self):
        print(self.nama)
        print(self.bagian)
        print(f"{self.gaji + self.bonus}")
        return self.gaji + self.bonus
class programmer(pegawai):
    def __init__(self,nama,bagian,gaji,bonus2):
        super().__init__(nama,bagian)
        self.gaji = gaji 
        self.bonus2 = bonus2
    def output2(self):
        print(self.nama)
        print(self.bagian)
        print(f"{self.gaji + self.bonus2}")
ts1 = manajer("radit","manajer",200,100)
print(ts1.output())
print("\n")
ts2 = programmer("dimas","programmer",100,200)
ts2.output2()
        
