# ism = 'ahad'
# print(ism != 'Ahad')
# print(ism.title()=='ahad')
#
# ####################################################################################################################
#
#
#
# nums1 = [1,2,3]
# nums2 = [1,2,3]
# print(nums1!=nums2)
# print(9**2>=7*9+18)
#
# ####################################################################################################################
#
#
# x = 10
# print(x*x<x**2)
# print(x*x>=float(f"{x**2}"))
#
# ####################################################################################################################
#
# son=float(input("Istalgan sonni kirting: "))
# if son>0:
#     print(son, "musbat son.")
# else:
#     print(son, "manfiy son.")
#
# ####################################################################################################################
#
#
# yosh=int(input("Yoshingizni kirting: "))
# if yosh<=7:
#     print("Sizga aftobus bepul.")
# else:
#     print("Chipta narxi 5000 so'm.")
#
# ####################################################################################################################
#
#
# avtolar=['audio', 'bmw', 'volvo', 'kia', 'hyundai']
# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())
#
# ####################################################################################################################
#
#
# javob=float(input("12x6 nechiga teng?>>> "))
# if javob !=72:
#     print("Javob xato. ")
# else:
#     print("Javob to'g'ri. ")
#
# ####################################################################################################################
#
#
# yosh=int(input("Yoshingiz nechida?>>> "))
# if yosh>=18:
#     print('Xush kelibsiz!')
# else:
#     print('Kirish mumkin emas! ')
#
# ####################################################################################################################
#
#
# yil=int(input("Tug'ilgan yilingizni kirting: "))
# if 2023-yil<18:
#     print(f"Yoshingiz {2023-yil}da ekan.")
#     print("Kirish mumkin emas!")
# else:
#     print("Xush kelibsiz !")
#
# ####################################################################################################################
#
#
# login=input("Yangi login tanlang :")
# if len(login)<=5:
#     print("Login 5 harifdan ko'proq bo'lishi shart !")
# else:
#     print("Login muvaffaqiyatli yuklandi !")
#
# ####################################################################################################################
#
#
# son=int(input("Son kiriting: "))
# if son>0:
#     print("Son musbat. ")
# elif son<0:
#     print("Son manfiy. ")
# else:
#     print("Son 0 ga teng. ")
#
# ####################################################################################################################
#
# yosh=int(input("Yoshingiz nechida? "))
# if yosh<4:
#     print("Sizga kirish bepul. ")
# elif yosh<=12:
#     print("Sizga kirish 5 000 so'm. ")
# else:
#     print("Sizga kirish 10 000 so'm")
#
# ####################################################################################################################
#
# yosh=int(input("Yoshingiz nechida? "))
# if yosh<4:
#     narx = 0
# elif yosh<=12:
#     narx = 5000
# else:
#     narx = 10000
# print(f"Sizga kirish {narx} so'm")
#
# ####################################################################################################################
#
# yosh=int(input("Yoshingiz nechida? "))
# if yosh<4:
#     narx = 0
# elif yosh<=12:
#     narx = 5000
# elif yosh<65:
#     narx = 10000
# else:
#     narx = 8000
# print(f"Sizga kirish {narx} so'm")
#
# ####################################################################################################################
#
#
# yosh=int(input("Yoshingiz nechida? "))
# if yosh<4:
#     narx = 0
# elif yosh<=12:
#     narx = 5000
# elif yosh<65:
#     narx = 10000
# elif yosh>=65:
#     narx = 8000
# print(f"Sizga kirish {narx} so'm")
#
# ####################################################################################################################
#
#
# kun = input("Bugun nima kun?>>> ")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print("Bugun dam olish kuni. ")
# else:
#     print("Bugun ish kuni. ")
#
# ####################################################################################################################
#
# kun = input("Bugun nima kun ?>>> ")
# harorat = float(input("Havo harorati qanday ?>>> "))
# if kun.lower()=='yakshanba' or kun.lower()=='shanba' and harorat>=30:
#     print("Cho'milgani ketdik ! ")
# elif kun.lower()=='yakshanba' or kun.lower()=='shanba' and harorat<30:
#     print("Uyda dam olamiz. ")
#
#
# ####################################################################################################################
#
# kun = input("Bugun nima kun ?>>> ")
# yosh = int(input("Yoshingiz nechida ?>>>"))
# if (yosh<7 or yosh>65) and kun == 'chorshanba':
#     print("Bugun siz uchun muzeyga kirish bepul.
#
# ####################################################################################################################
#
#
#                        ########  (1)-True  ######  (0)-False  ######
#
# narx = 15000 # Mijoz 15000 so'mga taom oldi.
# choy = 1  #  Mijoz choy ham oldi.
# salat = 0  # Mijoz salat ham oldi.
# if choy and salat:  # agar Mijoz choy va salat olgan bo'lsa.
#     narx = narx+10000 # narxga 10000 so'm qo'shamiz.
# elif choy or salat: # agar choy yoki salat olgan bo'lsa.
#     narx = narx+5000 # narxga 5000 so'm qo'shamiz.
# print(f"Jami narx {narx} so'm") #  Jami narxni chiqarmiz.
#
#
# ####################################################################################################################
#
#
# narx = 15000
# choy = 1
# salat = 0
# non = 1
# kompot = 1
# assorti = 0
# if choy:
#     print("Mijoz choy oldi.")
#     narx = narx+3000
# if salat:
#     print("Mijoz salat olmadi.")
#     narx = narx + 5000
# if non:
#     print("Mijoz non oldi.")
#     narx = narx+2000
# if kompot:
#     print("Mijoz kompot oldi.")
#     narx = narx + 5000
# if assorti:
#     print("Mijoz assorti olmadi.")
#     narx = narx+15000
# print(f"Jami narx {narx} so'm")
#
# ####################################################################################################################
#
#
# ##################################  in OPERATORI  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#
# menyu = ['osh', 'qozonkavob', 'shashlik', 'norin', 'somsa']
# 'manti' in menyu ### Menyu da manti bor yoki yo'qligini tekshiryapmiz .
#
#
# menyu = ['osh', 'qozonkavob', 'shashlik', 'norin', 'somsa']
# 'osh' in menyu ### Menyu da osh bor yoki yo'qligini tekshiryapmiz .
#
# ####################################################################################################################
#
# menyu = ['osh', 'qozonkavob', 'shashlik', 'norin', 'somsa']
# ovqat = input("Nima ovqat yeysiz ?>>> ")
# if ovqat.lower() in menyu:
#     print("Buyurtma qabul qilindi. ")
# else:
#     print("Afsus, bizda bunday ovqat yo'q. ")
#
# ####################################################################################################################
#
#
# ##########################  not in  OPERATORI  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#
#
#
# menyu = ['osh', 'qozonkavob', 'shashlik', 'norin', 'somsa']
# 'osh' not in menyu ### Menyu da osh yo'qmi ?.
#
# ####################################################################################################################
#
# menyu = ['osh', 'qozonkavob', 'shashlik', 'norin', 'somsa']
# ovqat = input("Nima ovqat yeysiz ?>>> ")
# if ovqat.lower() not in menyu:
#     print("Afsus, bizda bunday ovqat yo'q .")
# else:
#     print("Buyurtma qabul qilindi .")
#
#
# ####################################################################################################################
#
# menyu = ['osh', 'qozonkavob', 'shashlik', 'norin', 'somsa']
# buyurtmalar = ['osh', 'shashlik', 'manti', 'norin']
# for taom in buyurtmalar:
#     if taom in menyu:
#         print(f"Menyuda {taom} bor. ")
#     else:
#         print(f"Kechrasiz, menyuda {taom} yo'q. ")
#
#
# ####################################################################################################################
#
#
# list1 = [1,2,3,4]
# if list1:        # Ro'yxatda element bor yokli yo'qligini tekshirish usuli .
#     print("Ro'yxatda element bor . ")
#
# ####################################################################################################################
#
# menyu = ['osh', 'qozonkavob', 'shashlik', 'norin', 'somsa']
# buyurtmalar = ['osh', 'shashlik', 'manti', 'norin']
# if buyurtmalar:
#     for taom in buyurtmalar:
#         if taom in menyu:
#             print(f"Menyuda {taom} bor. ")
#         else:
#             print(f"Kechrasiz, menyuda {taom} yo'q. ")
# else:  ###  Agar RO'YXAT bo'sh bo'lsa .
#     print("Savatchangiz bo'sh .")
#
#
# ####################################################################################################################
#
#
#     #############################################################################################################
# #####################################       UY  ISHI        ##########################################################
# #######################################################################################################################
#
#
#   @ #   1. Foydalanuvchidan Juft son kirtishini so'rash va ko'nsulga chiqarish .
#
#
#
# son = float(input("Juft son kirting:>>> "))
# if son%2:
#     print("Bu son juft emas. ")
# else:
#     print("Raxmat . ")
#
#
# ####################################################################################################################
#
#
#   @ #   2.  Foydalanuvchidan yoshini so'raydigan va Muzeyga kirish narxini ko'rsatadigan ko'd .
#
# yosh = int(input("Yoshingiz nechida ?>>> "))
# if yosh<4:
#     print("Sizga kirish bepul.")
# elif yosh>60:
#     print("Sizga kirish bepul.")
# elif yosh<18:
#     print("Sizga kirish 10000 so'm.")
# elif yosh>18:
#     print("Sizga kirish 20000 so'm.")
#
# ####################################################################################################################
#
#
#   @ #   3. Foydalanuvchidan 2 ta son kiritishini so'rash va ularni solishtirish .
#
# a = float(input("Brinchi sonni kirting .>>> "))
# b = float(input("Ikkinchi sonni kirting .>>> "))
# if a==b:
#     print(f"{a} = {b} dan.")
# elif a<b:
#     print(f"{a} < {b} dan.")
# else:
#     print(f"{a} > {b} dan. ")
#
# ####################################################################################################################
#
#
#   @ #   4.  Oydalanuvchidan mahsulot kiritishini so'rash va bor yoki yo'qligi haqidagi malumotni ko'nsulga chiqarish .
#
# mahsulotlar = ['sabzi', "go'sht", "karam", 'piytoz', "karto'shka", "sholg'om", 'pamidor', 'bodring', 'turub', 'ridiska']
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatg {n+1}-mahsulotni qo'shing: "))
#
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
# else:
#     print(f"Do'konimizda {mahsulot} yo'q.")
#
# ####################################################################################################################
#
#
#
#   @ #   5.  Foydalanuvchidan mahsulot kiritishini so'rash va bor yoki yo'qligi haqidagi malumotni ko'nsulga chiqarish .
#
# mahsulotlar = ['sabzi', "go'sht", "karam", 'piytoz', "karto'shka", "sholg'om", 'pamidor', 'bodring', 'turub', 'ridiska']
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatg {n+1}-mahsulotni qo'shing: "))
#
# bor_mahsulotlar  =[]
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
#
# if mavjud_emas:
#     print(f"Do'konimizda quydagi mahsulotlar yo'q: ")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
#
#
# ####################################################################################################################
#
#
#
#   @ #   6. Foydalanuvchidan LOGIN so'rash .
#
# users = ['alisher', 'aziza', 'yasina', 'umar']
#
# login = input("Yangi login tanlang: ")
#
# if login in users:
#     print("Login band, yangi login tanlang! ")
# else:
#     print(f"Xush kelibsiz, {login.title()}! ")
#
#
# ####################################################################################################################
#
#
#
#
#   @ #   7.  Foydalanuvchidan son kiritishini so'rash va qoldiqsiz bo'linadigan sonlarni topish .
#
# son = int(input("Istalgan butun son kirting:"))
#
# for n in range(2,11):
#     if not(son%n):
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi. ")
#
#
