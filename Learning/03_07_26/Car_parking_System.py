class Car:
    Model=""
    Car_No=""
    Owener_name=""
    Ownner_Mobile=0   
    Check_In=""
    Check_Out=""
    Amount=0
    date=""
    total_time_in_mins=0
    def __init__(self,Model="",Car_No="sdubv",Owener_name="",Ownner_Mobile=0,Check_In="",Check_Out="",date=""):
        self.Model=Model
        self.Car_No=Car_No
        self.Owener_name=Owener_name
        self.Ownner_Mobile=Ownner_Mobile
        self.Check_In=Check_In
        self.Check_Out=Check_Out
        self.date=date
        self.Amount=5*3
        self.total_time_in_mins= 6+10
    
    def Display(self):
        print(self.Model+"  "+self.Car_No+"  "+self.Owener_name+"  ",self.Ownner_Mobile,"  "+self.Check_In+"  "+self.Check_Out+"  ",self.Amount,"  "+self.date+"  ",self.total_time_in_mins)
        

c1 = Car(Model="Tata indica",Car_No="TN47AM5958",Owener_name="Rohanth R B",Ownner_Mobile=9345696520,Check_In="12:24AM",Check_Out="12:12PM",date="03/07/2026")
c2 = Car(Model="Tata indica",Owener_name="Rohanth R B",Ownner_Mobile=9345696520,Check_In="12:24AM",Check_Out="12:12PM",date="03/07/2026")

c1.Display()
c2.Display()
