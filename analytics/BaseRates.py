
from .ratebands import AgeRateBandDict

class InsuranceCostModel(object):
    """Insurance Cost Model.

    Attributes:
        baserate: An integer representing the number of wheels the car has.
        totalcost: The integral number of miles driven on the car.
        personalhistorycost: The make of the car as a string.
        mortalitycost: The model of the car as a string.
        adminstrativecost: The integral year the car was built.
        provisioningcost :
        marketingcose: The date the vehicle was sold.

          savingcost: The date the vehicle was sold.
           typocommunity: The date the vehicle was sold.
           typocity: The date the vehicle was sold.
           sleepRewards
           workOutRewards
    """

    def __init__(self,AgeRateBandDict, baserate = 900, personalhistorycost = 0, mortalitycost=0, adminstrativecost=0, savingcost=0, typocommunity ={},typocity={},sleepRewards=0,workOutRewards=0):
        """Return a new Car object."""
        self.baserate = baserate
        self.AgeRateBandDict = AgeRateBandDict
        self.personalhistorycost = personalhistorycost
        self.mortalitycost = mortalitycost
        self.adminstrativecost = adminstrativecost
        self.savingcost = savingcost
        self.typocommunity = typocommunity
        self.typocity = typocity
        self.sleepRewards = sleepRewards
        self.workOutRewards = workOutRewards


    
    def age_cost(self,agekey):

        AgeRateBandDict = {'1': 10, '2': 20, '3': 30}
        Costval=0
        if agekey is not None:
             if AgeRateBandDict[agekey] == 1:
               Costval =  AgeRateBandDict[agekey]
             if AgeRateBandDict[agekey] == 2:
                Costval =  AgeRateBandDict[agekey]
             if AgeRateBandDict[agekey] == 3:
                Costval =  AgeRateBandDict[agekey]
        return Costval

    def admin_cost(self):
        adminstrativecost = 9000
        return adminstrativecost

    def personal_history_cost(self):
        """Return the price for which we would pay to purchase the car."""
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return 8000 - (.10 * self.miles)

    @property
    def total_cost(self,currentage):
        total = self.age_cost(self,currentage)+ self.admin_cost()
        return total