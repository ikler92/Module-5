class House:
    def __init__(self, name, floor):
        self.name = name
        self.number_of_floors = floor

    def go_to(self, new_floor):
        self.floar_goal = new_floor
        for i in range(1, self.number_of_floors):
            if new_floor > self.number_of_floors or new_floor < 1:
                print("Такого этажа не существует")
                break
            if i == new_floor:
                print(i)
                break
            print(i)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('ПИК', 4)
h1.go_to(5)
h2.go_to(10)
h3.go_to(5)

