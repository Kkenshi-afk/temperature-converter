# class Myclass:
#     x=7 #property
#     bmw=2017
#     def __init__(self): #constructor method
#         print("Loading is succsessful!")  #burada gorundugu gibi biz istemesek de cagirdigimz bir fonksiyondur 
    
# obj=Myclass() #burdaki myclass sinifini objye atarak bir nesne olusturduk
# print(obj.bmw) #sinifimin icindeki degerlere boyle ulasiriz
# print(obj.x)
# class Myclass:
#     def __init__(self,brand,model,color):
#         self.brand=brand
#         self.model=model
#         self.color=color #constuructor`u boyle kullaniyoruz
# obj=Myclass("Bmw","S200","Blue")#fonksiyon kullanir gibi
# ob2=Myclass("honda","f5","blac") #burada ikinci nesne olusturmus olduk 
# print(f"This car is {obj.brand}, car model is {obj.model}, this color is {obj.color}")#burada gordugun gibi bir parametrede hepsini yapiyoz
###################################################################################################################################################
#object oriented programming dunder / magic methods
# class Person:
#     def __init__(self,n,m):
#         self.name=n
#         self.age=m
#     #def __str__(self):#bu kismi yapmadan calistirirsak ustteki kismin ramde nerde tutuldugunu verir
#      #   return f"Name:{self.name}\nAge:{self.age}" #bu kisim ise istedigimiz sekilde cikti verir
#     def __repr__(self):#bu ise hata ayiklama icin kullanilir, yani yazilimcilar icin, kodu daha detayli verir
#         return f"Name:{self.name!r}\nAge:{self.age!r}"
# p1=Person("Cagri",21)
# print(p1)

# class Person:
#     def __init__(self,n,m):
#         self.name=n
#         self.age=m
#     def my_func(self):#classlarin icerisinde olusturdugumuz tum fonksiyonlar method olarak adlandirilir
#         print(f"Hello my name is {self.name}")
#         print(f"I am {self.age} years old")


# p1=Person("Cagri",21)
# #p1.my_func()
# p1.age=33 #boyle de disardan classa ulasip bir veriableyi degisebiliriz
# del p1.name #boyle silebilirz sadece p1 yazarsak nesneyi siler
# p1.my_func()
###################################################################################################################################################

# class Person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
#     def myPrint(self):
#         print(self.firstname,self.lastname)
# # class Student(Person):#inheritance islemi boyle yapilir
# #     pass
# class Student(Person):#inheritance islemi boyle yapilir
#     def __init__(self, fname, lname):#Boyle constructur yaparsan parents classindaki contructuru gecersiz kilarsin
#         super().__init__(fname,lname)#boyle de parents constructurunu cagirabiliyoruz,diger methodlari da getirebiliriz boyle
#         self.graduationyear=2022
# p1=Student("Cagri","Rmk")
# p1.myPrint()
# print(p1.graduationyear)
###################################################################################################################################################

# class Animal:
#     def speak(self):
#         return "Sound"
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"#burda ve altta oldugu gibi miras almamiza ragmen neden kendi ayni isimli fonkisyonunu kullandi?
#     #cunku method overriding oldu vee kendi methodunu kullandi
# class Dog(Animal):
#     def speak(self):
#         return "Bark!"
# cat=Cat()
# dog=Dog()
# print(cat.speak())
# print(dog.speak())


# class FlyingVehicle:
#     def fly(self):
#         return "This vehicle can fly"
# class WaterVehicle:
#     def sail(self):
#         return "This vehicle can sail on water"
# class AmphibiousCar(FlyingVehicle,WaterVehicle):
#     def drive(self):
#         return "Then vehicle can also drive on land"
# car=AmphibiousCar()#We can multiple inheritance like here`s write
# print(car.fly())
# print(car.sail())
# print(car.drive())
# print(isinstance(car,WaterVehicle))#This code checks this class to see if there is another class that derives from this class.
# print(issubclass(AmphibiousCar,FlyingVehicle))#we look for which child`s class at the here 

###################################################################################################################################################

#Magic Methods

# #We do not call these methods, they work on their own
# class Customlist:
#     def __init__(self,items):
#         self.items=items
#     def __len__(self):
#         return len(self.items)
# my_list=Customlist([1,7,19,12,5,2])
# print(len(my_list))#we call len function here and up  __len__ work on their own

# class   Greet:
#     def __call__(self,name):
#         return f"Hello {name}"
# greet=Greet()#Bu fonksiyonla selfi hic kullanmadik, normal fonksiyonmus gibi cagirdik
# print(greet("Fehmi Uyar"))

# class Customlist:
#     def __init__(self,items):
#         self.items=items
#     def __getitem__(self,index):#getitem ile listeden istedigimz indexi cektik
#         return self.items[index]
#     def __setitem__(self,index,value):
#         self.items[index]=value
#     def __delitem__(self,index):
#         del self.items[index]
# my_list=Customlist([19,70,25])#burda nesneyi liste gibi kullandik
# print(my_list[2])
# my_list[2]=30#burada setitemi kullandik setitem listeden eleman degistirmemize yariyor
# print(my_list[2])
# print(my_list.items)
# del my_list[2] #burada delitemi kullandik ve silmek istedigimiz elemani sildik
# print(my_list.items)

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __eq__(self,other):#equal(esittir)
#         return self.age==other.age
#     def __lt__(self,other):#less than(<)
#         return self.age<other.age
#     def __le__(self,other):#less than or equal
#         return self.age<=other.age
#     def __gt__(self,other):
#         return self.age>other.age
#     def __ge__(self,other):#grater than or equal
#         return self.age>=other.age
#     def __ne__(self,other):
#         return self.age!=other.age
# p1=Person("Fehmi uyar",24)
# p2=p1=Person("Mithat Aker",41)
# print(p1==p2)
# print(p1>=p2)
# print(p1<=p2)
# print(p1!=p2)
# print(p1>p2)
# print(p1<p2)

# class Person:
#     def __init__(self):
#         print("Object created")
#     def __del__(self):
#         print("Obejct deleted")
# obj=Person()
# del obj#nesneyi siler silmez __del calisir

# class Number:
#     def __init__(self,value):
#         self.value=value
#     def __add__(self,other):
#         return Number(self.value+other.value)
#     def __sub__(self,other):
#         return Number(self.value-other.value)
#     def __mul__(self,other):
#         return Number(self.value*other.value)
#     def __truediv__(self,other):
#         if(other.value==0):
#             return ValueError
#         return Number(self.value/other.value)
#     def __floordiv__(self,other):
#         return Number(self.value//other.value)
#     def __mod__(self,other):
#         return Number(self.value%other.value)
#     def __pow__(self,other):
#         return Number(self.value**other.value)
#     def __neg__(self):
#         return Number(-self.value)
#     def __pos__(self):
#         return Number(+self.value)
#     def __abs__(self):
#         return Number(abs(self.value))
#     def __str__(self):#bunlari string olarak cevirmeliyiz yoksa bellek adreslerini verir
#         return str(self.value)
# number1=Number(10)
# number2=Number(3)
# print(number1+number2)
# print(number1-number2)
# print(number1*number2)
# print(number1/number2)
# print(number1//number2)
# print(number1%number2)
# print(number1**number2)
# print(-number1)
# print(+number2)
# print(abs(number1))

#102. video 2.kisim

# class Person:
#     def __init__(self,n):
#         self.name=n
#     def __getattr__(self, attr):#nesnede bu attribute olup olmadigini kontrol eder
#         return f"'{attr}'attribute (property) is not found"
#     def __setattr__(self,attr,value):#bununla nesne icindeki bir veriableyi nesne disinda degistirebiliriz
#         super.__setattr__(attr,value)#burda hata aldik buna bi bak 103.video ilk

# p1=Person("Fehmi Uyar")
# print(p1.name)
# print(p1.age) #getattr`yi boyle cagirdik
# p1.age=35
# print(p1.age)
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         def __delattr__(self, attr):
#             if(attr=="name"):
#                 raise AttributeError("Cannot delete name attribute!")#name valuesini silemez boylece,#burayi calistiramdik 103 devami iste
#             super().__delattr__(attr)#silme islemi boyle yapiliyor
# p1=Person("Fehmi Uyar",34)
# print(p1.name)
# print(p1.age)
# del p1.name
# print(hasattr(p1,"name"))#bu fonksiyonla nesne silinmis mi silinmemis mi kontrol ederiz
# class Number:
#     def __init__(self,value):
#         self.value=value
#     def __int__(self):
#         return int(self.value)
#     def __float__(self):
#         return float(self.value)
# number=Number(7.19)
# print(int(number))#boylece nesnein turunu degistirebiliriz
# print(float(number))


#publicte hicbir sey yok, her zaman yaptigimiz gibi yapabilin gardascim
#protected _bir tane,yalnizca class icinde veya miras alan child classlar ulasabilir
#private __ iki tane
# class Animal:
#     def __init__(self,n,s):
#         self.name=n #public attribute
#         self._species=s #_ dikkat et noktanin yaninda bu protected attribute
#     def _makeSound(self): #protected method bastaki _ isarete dikkat
#         return "Animal sound"
# class Dog(Animal): #child class
#     def __init__(self, n, b):
#         super().__init__(n,"Dog")
#         self.breed=b
#     def display_info(self):
#         return f"Dog name:{self.name},Breed:{self.breed},Species:{self._species}"
#     def make_sound(self):#public method
#         return self._makeSound()#protected method
# dog=Dog("Wolf","Bulldog")
# print(dog.display_info())
# print(dog.make_sound())

#Privateler classin icinde kullanilir baska bir classin icinde kullanilamaz
# class BankAccount:
#     def __init__(self,account_number,balance):
#         self.account_number=account_number #public
#         self.__balance=balance #private
#     def deposit(self,amount):
#         if(amount>0):
#             self.__balance+=amount
#             return f"Deposited:${amount} New Balance :${self.__balance}"
#         return "Invalid deposid amount!"
#     def __display_balance(self): #private method
#         return f"Balance:${self.__balance}"
#     def get_balance(self): #public method
#         return self.__display_balance() #bakiyeyi disaridan gorebilmek icin yaptik cunku onceki private methotdu
# account=BankAccount("12345678",2000)
# #print(account.__balance)#bir private classa disaridan  ulasamazsin,private methodada ulasamazsin
# print(account.get_balance())

# class Vehicle:
#     def move(self):#polimorfiz farkli classlarda ayni isimli methodlarin bulunmasi
#         return "This vehicle moves"
# class Car(Vehicle):
#     def move(self):
#         return "This car drives on the road"
# class Boat(Vehicle):
#     def move(self):
#         return "This boat sails on water"
# class Airplane(Vehicle):
#     def move(self):
#         return "This airplane flies on the sky"
# class Bicycle(Vehicle):#burda pass yaziyor, yazdirmak istedigimizde miras aldigi class`in icindeki kismi yazar
#     pass
# vehicle=[Car(),Boat(),Airplane(),Bicycle()]
# for item in vehicle:
#     print(item.move())
# #106.video son ornek-108.video
#110.VIDEO
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod#class methodlar selfle degil cls ile calisir
    def birth_year(cls,name,birth_year):
        current_year=2025
        calculated_age=current_year-birth_year
        return cls(name,calculated_age)#burada cls yerine person varmis gibi dusun
    def display_info(self):
        return f"{self.name} is {self.age} years old"
p1=Person.birth_year("Cagri Rmk",2004)#classta ise boyle calisir
print(p1.display_info())
#112.video