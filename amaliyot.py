# class Talaba:
#     def __init__(self, ism, familya, tugilgan_yili):
#         self.ism = ism
#         self.familya = familya
#         self.tugilgan_yili = tugilgan_yili
    
#     def __str__(self):
#         return f"Ismi: {self.ism}\nFamilyasi: {self.familya}\nTug'ilgan yili: {self.tugilgan_yili}"
    
#     def get_first_name(self):
#         return f"Ismi: {self.ism}"
    
#     def get_last_name(self):
#         return f"Familyasi: {self.familya}"
        
#     def get_fullname(self):
#         return f"Ismi: {self.ism}\nFamilyasi: {self.familya}"
    
#     def get_age(self):
#         return 2023 - self.tugilgan_yili

# t1 = Talaba(input("ismini kiriting: "), input("familyani kiriting: "), int(input("Tug'ilgan yilini kiritng: ")))
# t2 = Talaba("Murod", "Husanov", 2001)
# t3 = Talaba("Sirojiddin", "Ahmadov", 2011)

# print(t1.__str__())
# print(t1.get_first_name())
# print(t2.get_last_name())
# print(t3.get_fullname(), t3.get_age())


# class Car:
#     def __init__(self, model, color, weight, high_speed):
#         self.model = model
#         self.color= color
#         self.weight = weight
#         self.high_speed = high_speed
    
#     def get_model(self):
#         return self.model
#     def get_color(self):
#         return self.color
#     def get_weight(self):
#         return self.weight
#     def get_high_speed(self):
#         return self.high_speed
#     def get_info(self):
#         return f"Modeli: {self.get_model()}\nRangi: {self.get_color()}\nOg'irligi: {self.get_weight()}kg\nTezligi: {self.get_high_speed()}km/s"
    
# c1 = Car(input("Modelini kiriting: "), input("Rangini kiriting: "), int(input("O'g'irligini kiriting (kg): ")), int(input("Tezligini kiriting (km/s): ")))
# c2 = Car("KIA", "K5", 120, 250)
# c3 = Car("Mesedes-Benz", "A210", 100, 300)

# # print(f"Modeli: {c1.get_model()}\nRangi: {c1.get_color()}\nOg'irligi: {c1.get_weight()}kg\nTezligi: {c1.get_high_speed()}km/s")
# print(c1.get_info())
# print(c2.get_info())
# print(c3.get_info())


class Circle:
    def __init__(self, radius, color) -> None:
        self.radius = radius
        self.color = color
    
    def get_radius(self):
        return f"Radiusi: {self.radius}"

    def set_radius(self):
        self.radius = int(input("Radiusni qayta kiriting: "))

    def get_color(self):
        return f"Rangi: {self.color}"
    
    def set_color(self):
        self.color = input("Rangini qayta kiriting: ")

    def get_area(self):
        S = self.radius**2*3.14
        return f"Yuzi: {S}"
    
    def get_circumference(self):
        L = self.radius*2
        return f"Doira uzunligi: {L}"

    def get_info(self):
        return f"{self.get_radius()}\n{self.get_color()}\n{self.get_area()}\n{self.get_circumference()}"
    
d1 = Circle(int(input("Radiusini kiriting: ")), input("Rangini kiriting: "))

d1.set_radius()
d1.set_color()
print(d1.get_info())