# # 1-masala
# class BankHisobi:
#     def __init__(self, egasi, boshlangich_balans=0):
#         self.__egasi = egasi
#         self.__balans = boshlangich_balans
    
#     def get_egasi(self):
#         return self.__egasi
    
#     def get_balans(self):
#         return self.__balans
    
#     def pul_qosh(self, miqdor):
#         if miqdor <= 0:
#             print("Noto'g'ri miqdor!")
#             return
#         self.__balans += miqdor
    
#     def pul_yech(self, miqdor):
#         if miqdor <= 0:
#             print("Noto'g'ri miqdor!")
#         elif miqdor > self.__balans:
#             print("Mablag' yetarli emas!")
#         else:
#             self.__balans -= miqdor


# hisob = BankHisobi("Ozodbek", 5_000_000)
# print(hisob.get_egasi())
# print(hisob.get_balans())
# hisob.pul_qosh(200_000)
# print(hisob.get_balans())
# hisob.pul_yech(1_100_000)
# print(hisob.get_balans())
# hisob.pul_yech(200_000)
# hisob.pul_qosh(-100_000)



# class foydalanuvchi:
#     def __init__(self, ism: str, parol: str) -> str:
#         self.ism = ism
#         self.__parol = parol

#     def get_ism(self):
#         return self.ism
    
#     def get_parol(self):
#         return self.__parol
    
#     def parolni_tekshir(self, kiritilgan_parol):
#         if kiritilgan_parol == self.__parol:
#             return True
#         else:
#             return False
        
#     def parolni_ozgartir(self, eski_parol, yangi_parol):
#         if eski_parol != self.__parol:
#             print("Eski parol noto'g'ri!")
#             return False
#         elif len(yangi_parol) < 6:
#             print("Yangi parol kamida 6 ta belgidan iborat bo'lishi kerak!")
#             return False
#         else:
#             self.__parol = yangi_parol
#             return True

# user = foydalanuvchi("Sardor", "maxfiy123")
# print(user.get_ism())
# print(user.parolni_tekshir("noto'g'ri_parol"))
# print(user.parolni_tekshir("maxfiy123"))
# user.parolni_ozgartir("xato", "yangi456")
# user.parolni_ozgartir("maxfiy123", "123")
# user.parolni_ozgartir("maxfiy123", "yangiParol1")
# print(user.parolni_tekshir("maxfiy123"))
# print(user.parolni_tekshir("yangiParol1"))

# class Talaba:
#     def __init__(self, ism, fan):
#         self.__ism = ism
#         self.__fan = fan
#         self.__baholar = []

#     def get_ism(self):
#         return self.__ism
#     def get_fan(self):
#         return self.__fan
#     def baho_qosh(self, baho):
#         if not (0 <= baho <= 100):
#             print("baho 0 dan 100 gacha bolishi kerak")
#             return
#         else:
#             self.__baholar.append(baho)
#     def get_baholar(self):
#         return self.__baholar.copy()
#     def ortacha_baho(self):
#         if not self.__baholar:
#             print("hali baho yoq")
#             return None
#         else:
#             return round(sum(self.__baholar) / len(self.__baholar), 2)
        
# talaba1 = Talaba("dolliit", "math")
# talaba1.baho_qosh(90)
# talaba1.baho_qosh(100)
# talaba1.baho_qosh(80)
# print(talaba1.ortacha_baho())
# print(talaba1.get_baholar())







































