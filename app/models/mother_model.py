from abc import ABC, abstractmethod

class AbstractParent(ABC):

  @abstractmethod
  def hello_friend(self):
    raise NotImplementedError
  
class Mother:
  def __init__(self, age):
    self.age = age
    print("mother constructor")
    
  def do_work(self):
    print("im working")
  def status(self):
    print("want to sleep")
  def do_house_work(self)
    print("listening music")
    
    
class Father(AbstractParent):

  def __init__(self):
    print("father constructor")
    
  def play_guitar(self):
    print("play guitar")
    
  def do_house_work(self)
    print("sitting on the sofa and drink beer")
  
  
class Daughter(Mother, Father):

  def __init__(self, age=0):
    Father().__init__(self)
    Mother().__init__(self, age=age)
    
  def hello_friend(self)
    pass

  def do_work(self):
    print("im working like a horse")
    
class Friend:
  pass
    

def greet_mother(mother : Mother):
   print("hello mother!!!")
   mother.do_work()
   
def greet_father(father : Father):
   print("time to beer")
   father.play_guitar()
 
if __name__ == '__main__':
  dauther = Daughter()
  #mother.do_work()
  
    #change parent
  #dauther.__class__=Frined
  
  
  greet_mother(dauther)
  greet_father(dauther)
  dauther.hello_friend()
  dauther.do_house_work()
  
  for x in [dauther]:
    x.do_hourse_work()
  #list
  povtorka_list = ["mathan_2", "programming_2"]  
  #tuple  
  vasian = ("11 years",12,3.14, dauther)
  #set
  my_set = {23,11,10,10,"call"}
  print(my_set)
  #frozen_set
  another_set = frozenset(["do","re","mi"])
  #dictionary
  my_dict = {1: "first","2": 123, (1,2,3): "tuple_as_a_key"}