
#Operator overload
class Vault:
    def __init__(self, galleons, sickles, knuts):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts



    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"
    
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return  Vault(galleons, sickles, knuts)
    

gilbert = Vault(100,50,25)
print(gilbert)

porter = Vault(25, 50, 100)
print(porter)

total = gilbert + porter
print(total)