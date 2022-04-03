class Programmer:
    company = "Microsoft"

    def __init__(self , name , product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} & the product is {self.product}")

saif = Programmer("Saif" , "Dell")
rehan = Programmer("Rehan" , "Delloite")
saif.getInfo()
rehan.getInfo()