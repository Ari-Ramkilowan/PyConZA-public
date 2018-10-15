class Bee:
    all_bees = []
    bee_count = 0
    has_pollen = False

    def __init__(self):
        self.all_bees.append(self)
        self.bee_count += 1

    def get_pollen(self):
        self.has_pollen = True

    def deposit_pollen(self):
        self.has_pollen = False

def test_bee():
    bees = [Bee() for i in range(3)]
    for bee in bees:
        assert bee.all_bees == bees
        assert bee.bee_count == 3
