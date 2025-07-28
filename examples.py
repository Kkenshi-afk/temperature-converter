class arac:
    olusturulan_arac=0
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        arac.olusturulan_arac+=1
    @classmethod
    def info(cls):
        return f"Olusturulan arac sayisi:{cls.olusturulan_arac}"
c1=arac("BMW",2017)
print(c1.info())
c2=arac("KMW",2017)
print(c2.info())
c3=arac("CMW",2017)
print(c3.info())
