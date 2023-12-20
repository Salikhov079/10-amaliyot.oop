class Talaba:
    def __init__(self, ism, familya, tugilgan_yili):
        self.ism = ism
        self.familya = familya
        self.tugilgan_yili = tugilgan_yili
    
    def __str__(self):
        return f"Ismi: {self.ism}\nFamilyasi: {self.familya}\nTug'ilgan yili: {self.tugilgan_yili}"
    
    def get_first_name(self):
        return f"Ismi: {self.ism}"
    
    def get_last_name(self):
        return f"Familyasi: {self.familya}"
        
    def get_fullname(self):
        return f"Ismi: {self.ism}\nFamilyasi: {self.familya}"
    
    def get_age(self):
        return 2023 - self.tugilgan_yili

t1 = Talaba(input("ismini kiriting: "), input("familyani kiriting: "), int(input("Tug'ilgan yilini kiritng: ")))
t2 = Talaba("Murod", "Husanov", 2001)
t3 = Talaba("Sirojiddin", "Ahmadov", 2011)

print(t1.__str__())
print(t1.get_first_name())
print(t2.get_last_name())
print(t3.get_fullname(), t3.get_age())

    
