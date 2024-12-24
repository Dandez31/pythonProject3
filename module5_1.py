class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.current_floor = 1

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Наверное Вы ошиблись домом')
            new_floor = int(input('На какой этаж поедем? : '))
            return self.go_to(new_floor)

        else:
            for floor in range(1, self.number_of_floors):
                if floor == new_floor:
                    print('<- Вы поднялись на этаж ', {new_floor})
                else:
                    print(f'{floor}')
                    continue
            print(f'<- последний этаж       ', {self.number_of_floors})


h1 = House('ЖСК Горский', 18)
h2 = House('Домик в деревне', 2)
print(h1.name, h1.number_of_floors)

new_floor = int(input('На какой этаж поедем? : '))
h1.go_to(new_floor)
