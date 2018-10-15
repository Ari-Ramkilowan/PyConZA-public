from typing import List, ClassVar
class Bee:
    all_bees: ClassVar[List["Bee"]] = [] # ClassVar isa class level variable, each instance doesn't have this var
    bee_count: ClassVar[int] = 0
    has_pollen: bool = False 

    def __init__(self)->None:
        self.all_bees.append(self)
        Bee.bee_count = self.bee_count + 1

    def get_pollen(self)->None:
        self.has_pollen = True

    def deposit_pollen(self)->None:
        self.has_pollen = False

def test_bee():
    bees : List[Bee]= [Bee() for i in range(3)]
    for bee in bees:
        assert bee.all_bees == bees
        assert bee.bee_count == 3