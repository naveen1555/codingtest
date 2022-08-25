class All_planet:
    def __init__(self,planet,atmospheric_gases,moons,rings):
        self.planet=planet
        self.atmospheric_gases=atmospheric_gases
        self.moons=moons
        self.rings=rings
 
class Mercury(All_planet):
    def __init__(self,planet,atmospheric_gases,moons,rings):
        super().__init__(planet,atmospheric_gases,moons,rings)
        
class Venus(All_planet):
    def __init__(self,planet,atmospheric_gases,moons,rings):
        super().__init__(planet,atmospheric_gases,moons,rings)
        
class Earth(All_planet):
    def __init__(self,planet,atmospheric_gases,moons,rings):
        super().__init__(planet,atmospheric_gases,moons,rings)
        
class Jupitor(All_planet):
    def __init__(self,planet,atmospheric_gases,moons,rings):
        super().__init__(planet,atmospheric_gases,moons,rings)
        
class Saturn(All_planet):
    def __init__(self,planet,atmospheric_gases,moons,rings):
        super().__init__(planet,atmospheric_gases,moons,rings)
        
class Uranus(All_planet):
    def __init__(self,planet,atmospheric_gases,moons,rings):
        super().__init__(planet,atmospheric_gases,moons,rings)
        
def test():
    mercury=Mercury(planet="mercury",atmospheric_gases="nill",moons=0,rings="No")
    venus=Venus(planet="venus",atmospheric_gases=["carbon_ioxide","Nitrogen"],moons=0,rings="No")
    earth=Earth(planet="earth",atmospheric_gases=["Nitrogen","oxygen"],moons=1,rings="No")
    jupitor=Jupitor(planet="jupitor",atmospheric_gases=["hydrogen","helium"],moons=79,rings="Yes")
    saturn=Saturn(planet="saturn",atmospheric_gases=["hydrogen","helium"],moons=83,rings="Yes")
    uranus=Uranus(planet="uranus",atmospheric_gases=["hydrogen","helium","methane"],moons=27,rings="Yes")
    
def gasesplanet(All_planet):
    gases_planet=All_planet.atmospheric_gases!="null",
    print(gases_planet.planet)
    
gasesplanet(All_planet)

def moons_count_having_rings(All_planet):
    moons_count=0
    planet_having_rings=All_planet().count(rings="Yes")
    for i in range(planet_having_rings):
        moons_count+=All_planet.planet_having_rings.moons[i]
        print(moons_count)

moons_count_having_rings(All_planet)