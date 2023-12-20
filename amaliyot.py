class Talaba:
    def __init__(self, ism, familya, tugilgan_yili):
        self.ism = ism
        self.familya = familya
        self.tugilgan_yili = tugilgan_yili
    
    def __str__(self):
        return f"Ismi: {self.ism}\nFamilyasi: {self.familya}\nTug'ilgan yili: {self.tugilgan_yili}"

t1 = Talaba(input("ismini kiriting: "), input("familyani kiriting: "), int(input("Tug'ilgan yilini kiritng: ")))

print(t1.__str__())
    
