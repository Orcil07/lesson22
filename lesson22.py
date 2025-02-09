class House:
    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'



h1 = House('hightower ', 10)
h2 = House('warehouse', 5)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))