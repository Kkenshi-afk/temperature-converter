#print("python is so easy")
#print('python\`s is so easy') yaparsan tek tirnak icine tek tirnak yazabilirisn cift tirnak icin de gecerli
#if 7>2:#Burada if kosulunu 2 nokta ile yaptik, ifin altindaki girinti ise o sonucun ife bagli oldugunu soyluyor
   #print("Python!!!")
#print("Sa") girinti birakmadik iften ciktik anlaminda
#x=7
#y="python"
#print(x)
#print(y)
#burada bir degiskenin veri tipini belirtmek istiyorsak kullaniriz,diger sekilde gerek yoktur.
#x=str(7)#burada 7`yi string olarak aldik,burada 7 matematiksel 7 degil string olan 7`dir`
#y=int(7)#burada integeer olarak aldik
#z=float(7)#burada float olarak aldik yanlarina ne oldugunu yazarsak o sekilde alabilriiz
#print(x)
#print(y)
#print(z)
#x=7
#y="python"
#print(type(x))#type fonksiyonunu kullanarak o degiskenin ne oldugunu bulabiliriz burada int dedi
#print(type(y))#burada ise str dedi
#y="python"#boyle string ifadeleri tek ve cift tirnak ile kullanabiliriz,burada da buyuk kucuk harf duyarliligi var
#x,y,z="Grap","Banana","Watermelon" burada oldugu gibi tek satirda birden fazla degiskene deger atayabiliriz,veriable ile deger sayilari ayni olmali
#eger veriablelere sadece tek bir deger atarasak butun veriableler ayni degere sahip olur
#colors=[1,2,3,4,5]
#x,y,z,t,n=colors dersek sirayla degerlerimiz x=1,y=2 gibi olur
#x="python"
#y="good"
#z="very"
#print(x,y,z) burada oldugu gibi coklu veriableleri boyle yazabiliriz "," yerine"+" da kullanabiliriz
#+ kullaninca arada bosluk birakmaz ama +`yi yazilarda kullan
# sayilarda kullanirsan toplama islemi olur`
#eger biri sayi biri string olursa pythonda + kullanamazsin, ama , kullanabilirsin
#name="Cagri"
#age=20
#weight=84.5
#comp=2j
#print("isim:",name,"yas:",age,"agirlik:",weight,"comp:",comp) burada goruldugu gibi birden cok degiskeni tek bir yerde toplayabiliyoruz
#print("isim:"+name+"yas:"+str(age)+"agirlik:"+str(weight)+"comp:"+str(comp)) burada ise hepsini stringe cevirip + ile bagalayabiliyoruz
#tuple ile liste farki tupledeki elemanlar degistirilemez liste [] bu tuple () bunla gosterilir
#myrange=range(7) ise bize 0 ve 7 arasi sayilari olusturur 7 dahil degil 0 1 2 3 4 5 6 ya kadar
#print(myrange) yazarsak cikti (0,7) olarak doner
#print(*myrange) diye yazarsak cikti 0 1 2 3 4 5 6 bu olur
#mydict={"name":"Cagri","age":34} dictionary ikili deger ciftlerinden olusur suslu parantezle gosterilir
#boolean sadece true ve false degerini alir
#myboo=True gibi
#x=None bu c dilindeki NULL`a karsilik gelir yani bos demek
#import sys #burada sys kutuphanesini dahil ettik import dahil et demek sys`de kutup iste
#x=7
#print(sys.getsizeof(x)) #pointer mantigi sistemde kac bytelik yer kapladigini soyler
#name=b"python" burada string degil artik bytes tipi oldu yani 0 ve 1`lerle calismaya basladik,
#b`blabla` burada ice bir deger alirsak bu degerin ASCII karakter tablosunda olduguna dikkat et, mesela turkce karakterleri kabul etmez
#8.videodaki 14.17 kismina bak hatta bundan sonraki kisma bak
#memoryview onemli oraya bak
#x=str("Hello World!") bu str fonksiyonu ile metinsel ifadeye cevirdik
#print(type(x)) burada typesine baktik
#print(x) ile de yazdirdik cikti olarak Hello World! verdi
#boolen ifdeler olan true ve falseye`de bu islemleri uygularsak onlar artik boolean olmaktan cikar ve metinsel ifadeler olurlar
#x=int(7.19) dersek bunu tam sayiya cevirir ve 7 olarak cikti verir
#x=int(True) ya da false yaparsak bunlari 0  ve 1 olarak bize cikti verir
#x=float(7) dersek 7.0 cikar metinsel ifadeler float ve int olmaz 
#x=complex(2,3) dersek cikti olarak 2+3j verir bu karmasik sayidir
#x=complex('3-2j') dersek 3-2j ciktisi verir + islemini - yaptik
#frozenset({}) ile gosterilir
#x=bool(buraya ne yazarsak yazalim 0 haric hepsini true dondurur bir tek 0`i false dondurur`)
#\n isareti burada da alt alta yazamyi sagliyor
#print("ali\nveli")
#y=19E4 buradaki e 19*10^4 gibi bir sayi ve boyle yazinca destekliyor
#x=complex(7) diyince karmasik sayilarda 7+0j diye donduruyor ama
#x=int(2+7j) diyince integeere donusturmuyor hata veriyor
#pi=3.14159
#radius_of_circle=float(input("Yari cap:"))#input scanf ayni gorevde, burada float yapmamizin nedeni kullanici ondalikli sayi girebilir,bufada dairenin yaricapini aldik
#area_of_circle=pi*radius_of_circle*radius_of_circle
#print("Dairenin alani:",area_of_circle)
#x=float(input("Enter first number:"))
#y=float(input("Enter second number:"))
#print("Sum:",x+y)
#import random ile random modulunu ekliyoruz ve rastgele sayilar uretebiliyoruz
#print(random.random()) ile rastgele bir sayi uretilir 0 ile 1 arasi uretir, bizim sistemimizin saatini kullanarak bunu uretir
#random.seed(7) yaparsak hep ayni sayiyi uretir cunku biz sabit sayi atadik ama digerinde sistem saati surekli degistigi icin rastgele sayilar uretir
#11.videoyu izle
#12.videoyu izle
#text="""This is so good
#life is good
#i`m a veriable
# multiline strings """` yaparak cok fazla satirda yazi yazabiliriz 3 tirnak olduguna dikkat et,tek tirnak icin de gecerli
#cars=["BMW","WOLKSWAGEN","VOLVO"]
#print(cars[0]) ile BMW yazdirdik
# stringler de birer arraydir
# text="Hello World!" 
#print(text[0]) ile H harfini cagirdik
#print(len(text)) ile arrayin uzunlugunu aldik
#print("free" in text) burada in ile free kelimesinin text metinin icinde olup olmadigina baktik not in kullanirsak yok mu diye kontrol ederiz
#text="Python is very good"
#print(text[1:5]) burada oldugu gibi dilimleme yaptik metini bir dizi gibi dusundu ve 1 ile 5. elemanlar arasini aldi 1 dahil 5 dahil degil
#text[:5] yaparsak 0`dan yani p harfinden baslar
# text[-5:-1] dersek dilimleme soldan baslar
#text="Python"
#text2="is very good"
#result=text + text2 ile birlestirebiliriz
#boyle yapinca pythonis very good olur
#result=text +" " + text2 yaparsak ikisi arasinda bosluk birakir
#print(text.upper()) yaparsak tum metni buyuk harfle yazar
#print(text.lower()) yaparsak da kucuk harfle yazar
#print(text.strip()) ile de metinin basinda veya sonunda bosluk birakilmissa onu siler
#print(text.replace("P","T")) burada ise P yerine T harfini getirdik
#text=1,2,3,4
#result=text.split(",") yani virgul gordugun zaman ayir dedik
#[1,2,3,4] diye cikti verir onlari ayirmis olur bunu metinde de yapabilirsin usendik
# text="Hello\rPy"
#print(text) yaparsak  \r imleci basa donduruyor
# yani bize cikti olarak Pyllo veriyor ikinci metni onun ustune yaziyor 
#\t bir tab bosluk birakiyor    Pyllo diye yazar
#\b ise HellPython diye yazar cunku bir harf geriye gider ve ordan yazmaya devam eder
#text="\120\171\164\150\157\156" ile ascii karakterleri kullanarak python yazabiliriz sadece python degil her seyi yazabiliriz
#bunu hexadecimal ile de yapabiliriz
#age=34
#text="My name is cagri, i am " + age yaparsak bize hata dondurur biz string yaparak bunu duzeltebiliriz
#text="My name is cagri, i am " + str(age) 
#text="My name is cagri,i am {}".format(age) yaparak da bunu yapabiliriz
#surname=rmk
#text="My name is cagri {1},i am {0}".format(surname,age)  yaparak birden fazla veriableyi ekleyebiliriz
#yukarida iclerine istedigimiz sayiyi yazabilirz eger yazarsak my name is cagri 34 i am rmk diye dondurur
#bunlar eski yontemlermis yeni yontem f ile yapiliyor
#text=f"My name is cagri{name},i am {age}" yaparsak usttekilerin gorevini yapar f string yapinca kumelerin icine istedigimiz seyi atayabiliriz
#.1f ile floattan sonra kac basamak istersek birin yerine yazmak yeter
#midterm_exam_score=input("Enter the midterm exam score:")
#final_exam_score=input("Enter the final exam score:")
#average=(float(midterm_exam_score)+float(final_exam_score))/2
#result=f"Your midterm exam score:{midterm_exam_score}\nyour final exam score:{final_exam_score}\nyour average:{average}"
#print(result)
#string metotlari icin 19.videoya don
#print(2**16) yaparak da us alabiliyoruz bu 2^16 demek
#print(int("61",16)) burada da 61 sayisini 16lik sistemde ver dedik
#print("ç".encode("utf-8"))#parantez icinde utf-8 yazmasaydik da utf-8`e gore kodlicakti,icine ascii yazarsak da ascii`ye gore bir degere atacakti
#asciiye attigimiz icin hata verecekti ve orda bir kod cikacakti u+1212312 gibisinden bu onun kodudur unityden onu bulabiliriz
#text.decode() ile de tekrar string`e cevirebiliyoruz
#yukarida oldugu gibi encode olarak kullanirsak onu binary forma atmis oluruz b`\xc3\xa7 diye bir cikti veriyor c3a7 olarak saklanmis demek
#print(bin(50087)) yaparsa da bıze 2"lık sıstemde nasıl saklandıgını gosterır 101010101 gıbı
#print(bin(50087).bit_length()) yaparsak da bize kac bitlik alanda saklandigini soyler 8/16 gibi
#21.video son 6dk
#text="My world to very hard mode on, i  hate my world"
#result=text.count("world",11,22) #yaparsak world kelimesi textte kac kere var onu sayar,yanda 11,22 ise 11 ve 22. degerler arasi arama yapacak
#result-text.startswith("world") dedik eger parantez icindeki degerle baslarsa true doner bitmezse false bunda da aralik belirtebiliriz
#result=text.endswith("world") eger parantezdeki ile biterse true bitmezse false dondur,bunda da aralik belirtebiliriz
#text="p\ty\tt\th\to\tn"
#print(text.expandtabs())#eger icine hicbir sey yazmazasak 8 alanlik bosluk birakir \n olmazsa olmaz
#text="Hi my name is python, I am 17 years old"
#result=text.find("python") python kelimesi hangi indexte baslarsa onu donduruyor,icinde olmayan bir deger aratirsak -1 dondurur, index`te find ile ayni ama index
#bulamazsa hata verir
#result=text.isalnum() #alfanumerik yani sadece sayi ve rakamdan olusuyorsa true dondurur,bosluk girsen bile false dondurur
#result=text.isalpha() bu ise sadece harf olacak ne rakam ne isaret hicbirini kabul etmez
#result=text.isascii() bu da eger ascii kodu iceren sayi harf ne vraasa iste true dondurur
#mesela turkce karakter kullaninca ascii de yok bu yuzden hata verir
#result=text.isdecimal() bu da sadece rakama izin verir, unitydeki kodunu yazsak bile kabul eder assagida oldugu gibi
#text2="\u0032" yazip isdecimalde kontrol edersek true dondurur cunku unityde 2 rakamina denk gelir
#text3="\u0048" yaparsak isdecimalde kabul etmez cunku H harfini dondurur
# text="The price only {price:.2f} Turkish lira!" #{} format metodu kumeli parantez yani yer tutucularla kullanilir
# print(text.format(price=70))
# text="The price only {price:.2f} Turkish lira!".format(price=70)#olarak da kullanilir
# text="The price only {0:.2f} Turkish lira!".format(70)#boyle de kullanilir
# text="we don`t have {:<10} children"#< bu isareti yaptiktan sonra icerde hngi sayi varsa o kadar bosluk birakip (sola hizalama) formatin icinde yazdigimizi yazar
# print(text.format(7))#> isaretiyle de saga hizaliyoruz
# text="we don`t have {:^10} children"#bu ise formatin icindeki sayiyi tam ortasina yazar 5 sagdan 5 soldan bolsuk birakir
# print(text.format(7))
# text="we don`t have {:=10} children"#formatin icinde isaret varsa -7 gibi - ile 7`yi ayirir ama + da bu belli olmaz
# print(text.format(-7))
# text="The temparature is between {:+} and {:-} degrees celcius"#{} icine + veya - yazmamiz sonucun isaretini belirtir
# print(text.format(4,-7))
# text="The temparature is between {: } and {: } degrees celcius"#{} icinde bosluk birakmak pozitif sayilardan once ekstra bir bosluk birakir,negatifte ise - isaretini
# print(text.format(4,-7))
# text="The temparature is {:,} degrees celcius"#{}:, yapmak binlik ayirici olarak 3 sifirlari ayirir virgul yerine_ koyarsak da _ olarak ayirir
# print(text.format(1390000000000))
# text="The binary version of {0} is {0:b}"#{0:b} onu binary forma donusturur,b yerine c yazarsak da unicode karakterine donusturur
# print(text.format(6))
# text="we have {:d} children"#{} icine d yazdik yani decimal parantez icine 0b yazarak onun binary oldugunu soyledik ve kodu yazdik 101=5 5 yazacak
# print(text.format(0b101))#0b binary 0x ise hexadecimal 0o ise octal sayilar icin sayilar icin kullanilan on ektir kullanmayi unutma 
# text="we don`t have {:e} children"#{]e ise matematiksel gosterim,E yazarsak da matematiksel gosterimde buyuk E yazar kucuk yerine
# print(text.format(7))
#18 ile 23.dakikadaki Buyuk F kullanimina bak 24.video,25,26,27 videolar
#text="Your number is {:.0%}" ise yuzdelik olarak gosterir
#print(text.format(0.55)) cikti olarak %55 verir
#true ve falseye boolean veri turu deniyormus
#x=bool(7)
#y=bool("python") ile string ve int`i bool turune cevirebiliyoruz bos " " veri turu haric her seyi 1 yani true olarak ceviri sayilarda ise 0 haric hepsini
#1 olarak ceviri
#print("bool(7)":,bool(7)) ile yazdirmaya calisirsak cikti olarak bool(7):true yazar
#liste,tuple de olsa true dondurur
#Bool(none) yazarsak da false dondurur cunku none zaten bos demek,tuple,dizi,liste eger bos gonderirsen onlari da false olarak cevirir
# x=3
# y=3
# result=x**y us alma 2 tane ** ile yapilir
# print(result)
# x=3
# y=7
# result=x//y pythonda iki // tam degeri verir yani 3/7=0.424242 diye gitsin ama \\ yapinca bize 0 dondurur yani sonucu al tam  sayiya yuvarlar
# , tek \ yapinca 0.424242 diye dondurur 
# print(result)
# x=7
# x &=12 burada 2li sayi sisteminde ikisinde de 1 varsa onu yazdi yani cevap 4
# print(x)
# x =7 
# x |=12
# print(x) burada ise 2li sayi sisteminde hangisinde 1 varsa okey
# x=7
# x ^=12 ikisi ayniysa 0 ikisi farkliysa 1 olarak alir 2`li sayi sisteminde
# print(x)
# x=16
# x >>=2 bytlerdeki 1 ve 0 lari kac birim yazarsan o kadar birim saga oteler << bu da sola oteler ve o degeri verir
# print(x)
#print(x:=4) yaparsak da print icinde yeniden x`e deger atayabiliyoruz boyle
#not(score>=50) 50`den buyuk esit degilse demek
# x=['strawberry',"banana","watermelon"]
# y=['strawberry',"banana","watermelon"]
# z=x
# print(x is z) #is ile her iki veriable ayni mi degil mi sorgular aynisa tru degilse false doner,bytlerdeki tutulduklari yere gore
# print(x is y) #x ve y ayni degil cikti, cunku bytlerdeki tutulma yerleri farkli
# print(x==y)#bura farkli
#print(x is not y) simdi burasi kontrol ediyor ve true donuyor ayni degilse demek
# x=['strawberry',"banana","watermelon"]
# print("strawberry" in x) eger listede varsa true yoksa false doner in komutu
# print("strawberry" not in x) ise olmamasini kontrol eder
# x=6 & 3 ikisinin de 1 old deger
#x=6 | 3 hnagisinde 1 varsa kabul eder
# x =6 ^ 3 ise ikisi ayniysa 0 farkliysa 1 dondurur 
# x =3<<3 #ise 3*2^3 yani kac yazarsak 2`nin ussu degisir
# print(x) 
# x =8>>3 ise bolme sekli
# print(x) 
# x=~3 x=-4 olarak doner onun degilinin bir fazlasini alir yani cevap 11 35.video 16.dakikada detayli anlatiyor
# print(x)
#listler [] parantez ile olusturulur,listlerde ayni elemani tekrar tekrar kullanabilirsin
# fruit=["apple","banana","watermelon","apple"] #eger negatif degiskenle cagirmak istersek son terim -1 olur ve oyle siralanir ilk indeks hep sifirdir
# fruit[-4]="Cucumber"
# print(fruit[-4])
#print(len(fruit)) ile kac eleman oldugunu bulabiliriz
#myList=[1,"Apple",True]#listler strutch yapisinda olabilir
# myList=list((1,"Apple",True))#parantez icine bir tane daha parantez acarak da list olusturabiliriz
# print(myList)
#tuple sirali,degistirelemz,yinelenebilir
# set sirali degil,degistirlemez,yinelenemez
# dictionary sirali,degistirilebilir,yinelenemez
# list sirali degistirilebilir yinelenebilir
#print(fruit(2:5)) 2 3 ve 4`u yazdirir
#fruit[2:6]= x,y yazarsak 2 elemani degisir 6.yere de y yazar onceki 6. eleman 7. eleman olur 38.video son 2 3 dk izle
# fruit=["apple","banana","watermelon","apple"]#+["Cucumber","Lime"]#boyle de liste yeni elemanlari ekleyebiliriz
# #newfruit=fruit+["Cucumber","Lime"]#yaparak da ekleyebiliriz
# #fruit.append("Cucumber")#boyle de ekleyebiliriz
# #fruit.insert(1,"Cucumber") #ile de istedigimiz indexe ekleyebiliriz
# fruit2=["pineapple","melon","strawberry"]
# fruit.extend(fruit2)#boylece baska bir listi baska bir liste ekleyebiliyoruz,sadece bu degil diger koleksiyon turlerinden hepsini ekleyebiliriz
# new_fruit=fruit #kopyalama islemini yapamazsin, burada newfruite uyguladigin her islemi fruite`de uygularsin,bu yuzzden kopyalanmaz
# new_fruit=fruit.copy() #ile bu kopyalama islemini yapabilirsin
# new_fruit=list(fruit)#ya da boyle 
# new_fruit=fruit[:]# ya da boyle
# print(fruit)
# import copy
# list1=[[1,2],[3,4]]
# list2=copy.deepcopy(list1)#eger ic ice list varsa onu boyle kopyalamak daha dogru olur
# fruit=["apple","banana","watermelon","apple"]
# #fruit.remove("apple")#remove ile listte istedigimiz degeri kaldirabiliriz
# #fruit.pop(2)#ile de sadece son ogeyi kaldirirz, hem de icine syi yazarsak o indexi kaldirir
# #del fruit[2]#ile de istedigimiz indexteki elemani kaldirirz,ama bunda icine sayi yazmaliyiz,eger [] yapmazsak tum listeyi siler
# #fruit.clear() #ile de listin icindeki tum degerleri bosaltiriz ve bos kume dondururuz
# result=fruit.index("banana") #yaprasak da bize banana nin index numarasaini dondurur,ama ilk olani birden fazla banana varsa
# result=fruit.count("banana")#ile de kac defa list icinde geciyorsa onu sayiyor
# print(fruit)
#fruit. () yaparsk da a`dan z`ye goturur + olarak kucukten buyuge dizer,buyuk harf duyarliligi var, once buyuk harfleri dizer sonra kucuk harfleri,41.video izle
#while xxx: eger buradaki kosul true ise while calisir
# i=1
# while (i<7):
#    #print(i,end="-Dadadanista") #icindeki end komutu ile yan yana yazabiliriz
#    i+=1
#    print("\n")
#    if(i==4):
#      # break#buradaki if break komutuyla donguden cikabiliriz ama continue yazarsak ordaki islemi sadece atlar
#      continue
#    print(i,end="-Falafel")
#while dongusu else ile calisabilir
# i=1
# while(i<7):
#    print(i,end=" ")
#    i+=1
# else:
#    print("While loop is over")
# mynumbers=[]#listeyi bos yapmazsan, ilk eleman yazdigin sayi olur
# i=0
# while(i<7):
#    input_numbers=int(input("Enter a number:"))
#    mynumbers.append(input_numbers)
#    i+=1

# # mynumbers.sort() bu fonksiyonla kucukten buyuge siraladik
# # print(mynumbers)
# x=0
# k=0
# while(x<7):
#    print(k,"-",mynumbers[x])
#    x+=1
#    k+=1
# start_number=int(input("Please enter a start number:"))
# end_number=int(input("Please enter a ending number:"))
# while(start_number<end_number):
#    if(start_number%2==0):
#       print(start_number,"-is a both number")
#    else:
#       print(start_number,"-is a single number")
#    start_number+=1

# fruits=["grape","orange","strawberry","cher"]
# for item in fruits: #for dongusuyle listelerdeki her elemani item diye veriable olusturduk hepsini ona attik ve yazdirdik for boyle kullaniliyor
#    print(item)
# #list,tuple,dictionary,set bunlar iterable iterationdur for dongusunu bu tekrarlanabilir yapilari olusturmak icin kullaniyoruz,46.video
# for item in range(0,10):
#    if(item%2==0):
#       print(item,end="-")
#    else:
#       print(item,end="*")
# else:
#    print("Foor loop is finished!!!")#burada da else kullanabiliriz,eger ondan once break kullanirsak else blogu yazilmayacaktir
# for item in range(0,10):
#    if(item%2==0):
#       pass #burada hicbir sey yazmasaydik hata donerdi ama pass komutuyla bu hatayi dodgeledik ... 3 nokta da ayni gorevi gorebilir
#    #def myEmptyFunction():
#    #... ya da pass ile de bosda duracak fonksiyonu yazabiliriz
#    else:
#       print(item,end="*")
# else:
#    print("\nFoor loop is finished!!!") #47.video
   ######
   #48 ve 49.videolardaki ornekleri yap
# fruit=["Melon","Watermelon","Kiwi","Cucumber","Orange","Strawberry","Apple"]
# for item in range(2,len(fruit)):#boyle bir yazim var
#       print(fruit[item])
# fruit=["Melon","Watermelon","Kiwi","Cucumber","Orange","Strawberry","Apple"]
# [print(item) for item in fruit]#boyle daha kisa yazarak da for kullanabilirsin
#fruit=["Melon","Watermelon","Kiwi","Cucumber","Orange","Strawberry","Apple"]
# new_list=[]
# for item in fruit:
#    if("g"in item ):
#       new_list.append(item)#bu yontemle icinde g gecen kelimeleri alip ayir bir liste yaptik
# print(new_list)
# new_list=[item  for item in fruit if("g" in item)] boyle de kisa yol ile yazabilirsin
# print(new_list)
#tupla () ile olusturulur
#eger tuple olusuturp tek deger verirsen onu string olarak dondurur ama tek deger verip , atarsan tuple olarak dondurur
# tup=("ali",12,True)
# print(f"His name:{tup[0]},his age:{tup[1]},this is:{tup[2]}")
#simdi tupleler degistirilemzdi ama onu listeye cevirip degistirip tekrar tupleye cevirebiliriz
# tup=("ali","veli","49","50")
# result=list(tup)
# result[0]="mehmet"
# result2=tuple(result)
# #tuppleyi degistiremedigimiz icin bir sey ekleyemeyiz ama onu list`e cevirip list de yaptigimiz metotlari kullanabiliriz
# print(result2)
# tup=("ali","veli","49","50")
# extup=("watermelon",)#eger sondaki virgulu eklemezsek tuple oldugunu anlamicak py  eger tek veri varsa
# tup += extup
# print(tup)
# del tup ile tupleyi silebiliriz
# fruits=("apple","banana","cucmber","pinneapple","strawberry")
# fruits2=("apple","banana","cucumber")
# (x,y,z)=fruits2
# print(x,y,z) boyle tuple paketleme islemini yapiyoruz
# fruits=("apple","banana","cucmber","pinneapple","strawberry")
# (x,y,*z)=fruits#burada ilk 2 elemani x ve y ye verdi geri kalanlari goturup z ye verdi
# print(x,y)
# print(z)
#63 64. videolar
#result=fruits.union(fruits2) yaparsak bu setleri birlestirir onceki iki sete bir sey olmaz sadece yeni bir set olusur
#union komutuyla sadece setleri birlestirmiyor diger veri turlerini de birlestiriyor, tuple falan
#result=fruits|fruits2 ile de bunlari birlestirebiliriz ama bu metotla sadece 2 seti birlestirebilirsin
#fruit.update(Fruits2) ile fruiti guncelliyoruz
#result=fruits.intersection(Fruis2) ile ortak elemanlari bize verir
#result=fruits & fruits2 bu da sadece setlerde calisir ve ortak elemanlari verir
#fruits.intersection_update(fruits2)   ile fruitsi ortak elemanlarla guncelleyebiliriz
#fruits&=fruits2 ile de bu komutu halledebiliriz eger 3 ve daha fazla eleman istesek fruits&=fruits2&fruits3 yapmamiz yeterli
#result=fruits,diffrence(fruits2) yapinca da fruits de olup fruits2de olmayanlari getirecek
#fruits-fruits2 yaparsak da ayni islem ama sdece setlerde olur
#fruits.diffrence.update(fruits2) ile de fruitsi olmayanlarla guncelleriz
#fruits-=fruits2 ile de bu islemi yapabiliriz eger birden fazla olsaydi fruits-=fruits2 |fruits3 yapacaktik
#result=fruits.symmetric.difference(fruits2) ile ikisinde olmayanlari yapiyoruz
#result=fruits^fruits2 yaparsak da ayni islemi verir
#fruits.symmetric.difference(fruits2)  boylece birinci listeyi guncelleriz
#fruits^=fruits2 ile de bunun kisa yolu
#result=fruits.copy()
#result=fruit.isdisjoint(fruits2) eger burda ortak eleman varsa 0 yoksa 1 dondurur evet dogru anladin ters islem var
#result=fruit.issubset(fruits2) fruit ogeleri fruits2de var mi diye kontorl eder eger varsa true yoksa false dondurur
#result=fruit<=fruits2 de ayni gorevi gorur
#result=fruit.isupperset(fruits2) bununla fruits2 deki degerler fruitste var mi diye kontrol ettik hepsi olmak zorunda
#result=fruit>=fruits2 de ayni gorevi gorur
#person=dict(name="Seyda",surname="Ay") boyle de dictionary olusturulabilir
#print(f"{person.get("name")}-{person.get("surname")}) get fonksiyonuyla da format metotlari kullanilabilir
#my_keys=person.keys() ile anahtarlari tutariz yani name ve surnameyi
#person["student"]=True dersek yeni bir anahtar ekler o da student
#my_keys=person.values()`de degerlere ulasmayi saglar
#person["name"]="Elif" dersek deger degisir
#68.video
#person2=person yaparsak personu person2`ye kopyalamis olmuyoruz referans gostermis oluyoruz
#personda yapilan tum degisiklikler person2`de de olur bu yuzden kopyalama islemi olamaz
#person2=person.copy() yaparsak kopyalama islemini yapmis oluruz
#person2=dict(person) yaparsak da kopyalamis oluruz
#69.video 6 ila 13.dk arasi hatta kalan videoyu izle
#def  fullname(*args) eger fonksiyon olusturdugumuzda kac tane deger gelecegini bilmiyorsak * isaretiyle bunu dodgeleyebiliriz
# def  fullname(*args):
#     print("My name is:"+args[2])
# fullname("Fehmi","Mithat","Agah")
#fonkisyon icinde de global veriable tanimliyabiliriz
#def function():
#global x dersek tanimlanir
#75.video son 2 dk 77.video ilk 5dk
# a=min(11,12,23,123,124) min ve max`i verir`
# b=max(11,12,23,123,124)
# print(a,b)

#import math ile matematik modullerini dahil et
#math.e ile euler sayisini alirsin
#math.inf + sonsuz
#-math.inf - sonsuz
#math.nan not a number demek yani bu bir sayi degil demek
#math.pi pi
#math.tau bir dairenin cevresinin yaricapina orani o da 2piye esittir yaklasik olarak
#77.video 13 ile 15 arasi
#math.degrees(8.90) bir aciyi radyandan dereceye donusturur
#math.radians(180) dereceden radyana donusturur
#math.ceil ile en yakin ustteki sayiya yuvarlar (11.00001) verirsen 12ye yuvarlar
#math.floor ise bir alt sayiya yuvarlar(11.9999) ise 11`e yuvarlar
#math.isqrt() ile karekokun icindeki sayiyi en yakin alt sayiya yuvarlar diyelim sonuc 5.123123 cikti cevap 5tir
#math.trunc(14.5) ise ondalikli basamagi kaldiriyor yuvarlama yok
#math.remainder(9,2) ise 78.video 11`den sonrasini izle
#math.comb(7,4) 7nin 4 lu kombinasyonunu aliyor
#math.copysign(6,2) ilkinin degerini 2.nin isaretini alip float turunden bir sayi dondurur
#79.video
#math.fabs(-23) yaparsak mutlak deger alir ama ondalikli sekilde cikti verir
#math.factorial(6) ise faktoriyel
#math.fmod(48,24) 48/24`un kalanini verir kalan 0 float seklinde verir
#80.video 6`dan 11`e kadar
#number=[1,2,3,4,5]
#math.fsum(number) ile liste veya tupledeki butun elemanlari topladik
#80.video 13.5 ile 24 arasi bak
#math.prod(number) ise liste veya tupledeki degerleri carpar bos tuple veya list verirsen 1 sonucunu dondurur
#math.prod(number,start=10) dersek 10*1*2*3*4*5 olarak dondurur yani baslangicla carpacagi bir deger atadik
#math.gcd(10,12) dersek obebini bulur bunlarin
#math.hypot(5,12) ise 13 verir hiptenus formulu
#81.video 8 ile 17dk arasi
#math.isfinite(100) mesela sayi sonlu ise true sonsuz ise false verir
#math.isinf(math.inf)  ise sonluysa true sonsuszsa false 
#math.isnan() ise    not a number ise true degilse false
#81.video 20 ile 33.dk
#math.log10(10) log 10 tabaninda 10 demek
#82.video 1 `den 4`e kadar
#math.log2(5) ise log 2 tabaninda 5 demek
#math.perm(5,2) ise permutasyon hesaplar
#import cmath ile complex modulleri ekliyoruz
#cmath.e euler sayisi
#cmath.inf sonsuz
#cmath.infj karmasik sonsuz sayi imajiner kismi temsil eder
#cmath.nan ve cmath.nanj
#cmath.pi
#cmath.tau
#cmath.sqrt(4+3j)
#83.video ilk 10dk
#cmath.isinfinite sonlu mu diye kontrol ediyor sonluysa true doner
#cmath.isinf sonsuz mu diye
#cmath.isnan not a number mi diye kontrol ediyor
#84.video
# import statistics ile istatistik fonkisyonlarini dahil et
#statistics.harmonic_mean(sayilar) sayilar kumesi icinndeki sayilarin harmonik ort alir
#statistics.mean(sayilar) ile ortalamasini buluruz
#statistics.median(sayilar) ile medyanini verir
#85.video 8 ile 14. dk 
#statistics.mode(sayilar) ile modunu verir
#statistics.multimode(sayilar) ise tum modlari liste halinde verir
#statistics.pstdev ile standart sapmayi hesaplarsin,formulune bakmak istersen 86.video ilk dklar
#statistics.stdev bir orneklemin standart sapmasini hesaplar 86`nin devami
#statistics.pvariance bir veri setindeki degerlerin ortalamadan ne kadar saptigini hesaplar
#statistics.variance 86 son kisim
#import datatime ile ekle
#result=dir(datetime) ile icinde neler oldugunu ogrenebilirsin
#datetime.datetime.now() ile simdiki zamani buluruz
#87 2 ile 5.dklar arasi
#datetime(2008,4,26,15,30) son ikisi saat geri kalan yil ay gun
#suanin tarihini alip .day,.year gibi ypaip istedigin seyi cekebilirsin microsecond ile onu da alirsin
#bunlar integeer olarak cekilir
#dataime.today() ile de yaparsin
#datatime.weekday() ile haftanin gununu alirisn
#datatime.ctime() ile haftanin gunu de dahil olmak uzere detayli tarih verir
#datatime.strftime ile string olarak aliriz
#87.video son kisim
#88.video
#89.video
#90.video
#result= lambda x: x+10 dedik 
#print(result(9)) dersek cevap 19 verir yani tek satirda fonkisyon gibi
#kossulu_ifade=lambda x:"dogru" if x>0  else "yanlis" x sifirdan buyukse dogru degisle yanlis yazsin dedik
#map() liste tuplelerde genelde calisir icine yazdigin listenin tamamini istedigin fonksiyon veya lambdaya yollar
#numbers=[2,3,4,5] dedik, asagida sayilari 2 ile carp diye fonksiyon olusturmusuz gibi dusun
#result=map(sayilari_carp,numbers) once fonksiyonun adini sonra kullanacagimiz listenin adini yazdik
# sayilari tek tek 2 ile carpip baska bir listeye atarak kullanabilirsin
#result=map(lambda x: x*2,numbers) burda ise lambdayla kullanimi gorduk
#result=filter(lambda x: x%2==0,numbers) burada sadece kosulu saglayan ifadeler yazilir gerisi atlanir
#92 10`la 12 arasi
#93.video decorator kismi
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#