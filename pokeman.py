class Pokemon:
    sound="sound"
    def __init__(self,name,level):
        
        if name=="":
            raise ValueError("name cannot be empty")
        if level<=0:
            raise ValueError("level should be > 0")
        self._name=name
        self._level=level
    def __str__(self):
        return "{} {} {} {}".format(self.name,'-',"Level",self.level)
    @classmethod
    def make_sound(cls):
        print(cls.sound)
    @property
    def name(self):
        return self._name
    @property
    def level(self):
        return self._level
class running(Pokemon):
    runn=""
    @classmethod
    def run(cls):
        print("{}".format(cls.runn))
class flying(Pokemon):
    flyy=""
    @classmethod
    def fly(cls):
        print("{}".format(cls.flyy))
class swimming(Pokemon):
    swimm=""
    @classmethod
    def swim(cls):
        print("{}".format(cls.swimm))


        
        
class Pikachu(running,Pokemon):
    sound="Pika Pika"
    runn="Pikachu running..."
    def attack(self):
        print("Electric attack with {} damage".format(10*self.level))
        
        
class Squirtle(running,swimming,Pokemon):
    sound="Squirtle...Squirtle"
    runn="Squirtle running..."
    swimm="Squirtle swimming..."
    def attack(self):
        print("Water attack with {} damage".format(9*self.level))
        
        
class Pidgey(flying,Pokemon):
    sound="Pidgey...Pidgey"
    flyy="Pidgey flying..."
    def attack(self):
        print("Air attack with {} damage".format(5*self.level))
        
        
        
class Swanna(flying,swimming,Pokemon):
    sound="Swanna...Swanna"
    flyy="Swanna flying..."
    swimm="Swanna swimming..."
    def attack(self):
        print("Water attack with {} damage".format(9*self.level))
        print("Air attack with {} damage".format(5*self.level))
        
        
        
class Zapdos(flying,Pokemon):
    sound="Zap...Zap"
    flyy="Zapdos flying..."
    def attack(self):
        print("Electric attack with {} damage".format(10*self.level))
        print("Air attack with {} damage".format(5*self.level))
        
        
class Island:
    total_island_list=[]
    def __init__(self,name,max_no_of_pokemon,total_food_available_in_kgs):
        self._name=name
        self._max_no_of_pokemon=max_no_of_pokemon
        self._total_food_available_in_kgs=total_food_available_in_kgs
        self._pokemon_left_to_catch=0
        self.total_island_list.append(self)
        
        

        
    @property
    def name(self):
        return self._name
    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
    @property
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
    @property
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
    
    def __str__(self):
        return "{} {} {} {} {} {} {}".format(self.name,'-',self.pokemon_left_to_catch,"pokemon",'-',self.total_food_available_in_kgs,"food")
        
    def add_pokemon(self,pokemon):
        if self._pokemon_left_to_catch<self._max_no_of_pokemon:
            self._pokemon_left_to_catch+=1
        else:
            print("Island at its max pokemon capacity")
    @classmethod
    def get_all_islands(cls):
        return cls.total_island_list
        

        
    '''def collect_food(self):
        pass'''
        
            
            
class Trainer:
    def __init__(self,name):
        self._name=name
        self._experience=100
        self._max_food_in_bag=10*self.experience
        self._food_in_bag=0
        self.pokemon_list=[]
        self._current_island=None
        
        #self.list_pokemon=[]
    def __str__(self):
        return self._name
        
    @property
    def name(self):
        return self._name
    @property
    def experience(self):
        return self._experience
    @property
    def max_food_in_bag(self):
        return self._max_food_in_bag
    @property
    def food_in_bag(self):
        return self._food_in_bag
        
    def move_to_island(self,island_1):
        self.current_island=island_1
        
    @property
    def current_island(self):
        if(self._current_island==None):
            print("You are not on any island")
        else:
            return self._current_island
            
            
    def collect_food(self):
        if self._current_island==None:
            print("Move to an island to collect food")
        elif self._current_island._total_food_available_in_kgs>self._max_food_in_bag:
            self._current_island._total_food_available_in_kgs-=self._max_food_in_bag
            self._food_in_bag=self._max_food_in_bag
        elif self._current_island._total_food_available_in_kgs<self._max_food_in_bag:
            
            self._food_in_bag=self._current_island._total_food_available_in_kgs
            self._current_island._total_food_available_in_kgs=0
        
        

    def catch(self,pokemon):
        pokemon._master = self
        self.pokemon_list.append(pokemon)
        if self._experience>=100*pokemon.level:
            print("You caught {}".format(pokemon.name))
            self._experience+=20
        else:
            print("You need more experience to catch {}".format(pokemon.name))
    def get_my_pokemon(self):
        return self.pokemon_list
    
        
        
        #if .master==self.name:
            #print(True)
        #else:
            #print("False")
        #for i in pokemon_list:
            #print(i)
    #def get_my_pokemon(self):
        #print(self.pokemon_list)
#trainer=Trainer("sai")
        
'''island = Island(name="Island1", max_no_of_pokemon=5, total_food_available_in_kgs=10000)   
print(Island.get_all_islands())'''     
'''if self._current_island != None:
            if self.current_island._total_food_available_in_kgs > self._max_food_in_bag:
                if self._food_in_bag < self._max_food_in_bag:
                    self._food_in_bag += self._max_food_in_bag
                    self.current_island._total_food_available_in_kgs -= self._food_in_bag
                else:
                    self._food_in_bag = self._max_food_in_bag
            else:
                self._food_in_bag = self.current_island._total_food_available_in_kgs
                self.current_island._total_food_available_in_kgs = 0
                
        else:
            print("Move to an island to collect food")'''
            
