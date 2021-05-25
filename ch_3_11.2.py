class Planet:
    def __init__(self, name=None, distance=0, mass=0, diameter=0):
        self.name = name
        self.distance = distance
        self.mass = mass
        self.diameter = diameter


class Cell:
    def __init__(self, value):
        self.value = value
        self.next_distance = None
        self.next_mass = None
        self.next_diameter = None


class LinkedList:
    def __init__(self):
        self.top = Cell(Planet())  # sentinel

    def add_planet_to_list(self, new_planet):
        current_planet = self.top
        while current_planet.next_distance and current_planet.next_distance.value.distance < new_planet.value.distance:
            current_planet = current_planet.next_distance
        new_planet.next_distance = current_planet.next_distance
        current_planet.next_distance = new_planet

        current_planet = self.top
        while current_planet.next_mass and current_planet.next_mass.value.mass < new_planet.value.mass:
            current_planet = current_planet.next_mass
        new_planet.next_mass = current_planet.next_mass
        current_planet.next_mass = new_planet

        current_planet = self.top
        while current_planet.next_diameter and current_planet.next_diameter.value.diameter < new_planet.value.diameter:
            current_planet = current_planet.next_diameter
        new_planet.next_diameter = current_planet.next_diameter
        current_planet.next_diameter = new_planet

    def sorted_by(self, parameter):
        current_planet = self.top
        current_index = 0
        print(f'LIST OF PLANETS SORTED BY {parameter}:')
        print('----------')
        while current_planet:
            print(f'{current_index}: {current_planet.value.name} ({current_planet.value.distance},'
                  f'{current_planet.value.mass},{current_planet.value.diameter})')
            if parameter == 'DISTANCE':
                current_planet = current_planet.next_distance
            elif parameter == 'MASS':
                current_planet = current_planet.next_mass
            elif parameter == 'DIAMETER':
                current_planet = current_planet.next_diameter
            else:
                break
            current_index += 1
        print('----------')


sample = LinkedList()
sample.add_planet_to_list(Cell(Planet('Mercury', 1, 1, 4)))
sample.add_planet_to_list(Cell(Planet('Venus', 2, 3, 5)))
sample.add_planet_to_list(Cell(Planet('Earth', 3, 2, 3)))
sample.sorted_by('DISTANCE')
sample.sorted_by('MASS')
sample.sorted_by('DIAMETER')
