# try:
#     x=7
#     print(x)
# except:
#     print("Something went wrong")
# else:#else blogunda try calisirsa calisir
#     print("Nothing went wrong")
# finally:#her kosulda calisir
#     print("The try-except is finished")
# #ic ice try except kullanilabilir

# try:
#     x=int(input("Enter a number"))
#     print(x)
#     if x<0:
#         raise ValueError("No") raise hatayi firlatir except yakalar
# except ValueError as e:
#     print("Error:",e)
# x='a'
# try:
#     if not type(x) is int:
#         raise TypeError("Only integeers are allowed")#type erorr istedigimiz tipte degilse calisir
# except TypeError as e:
#     print("Error",e)
#arithmetic error:sayisal islemlerde hata varsa onu dondurur,tum matsal hatalari yakalar, zerodevison gibi
#floatingpointerror: ise ondalikli sayilarda hesaplama hatasi olunce
#overflowerror: sayisal bir hesaplamanin sonucu cok buyuk olunca  
#assertionerror:bir assert ifadesi basarisiz olunca
try:
    number=7
    assert number<5,"number is not less than 5"
    print("number is less then")
except AssertionError:
    print("Error")








