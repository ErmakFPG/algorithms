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

    def add_link_to_planet(self, new_planet, next_link, attr):
        new_planet = Cell(new_planet)
        current_planet = self.top
        while getattr(current_planet, next_link) and getattr(getattr(current_planet, next_link).value, attr) < \
                getattr(new_planet.value, attr):
            current_planet = getattr(current_planet, next_link)
        setattr(new_planet, next_link, getattr(current_planet, next_link))
        setattr(current_planet, next_link, new_planet)

    def add_planet_to_list(self, new_planet):
        LinkedList.add_link_to_planet(self, new_planet, 'next_distance', 'distance')
        LinkedList.add_link_to_planet(self, new_planet, 'next_mass', 'mass')
        LinkedList.add_link_to_planet(self, new_planet, 'next_diameter', 'diameter')

    def sorted_by(self, parameter):
        current_planet = self.top
        if parameter == 'DISTANCE':
            current_planet = current_planet.next_distance
        elif parameter == 'MASS':
            current_planet = current_planet.next_mass
        elif parameter == 'DIAMETER':
            current_planet = current_planet.next_diameter
        current_index = 1
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
sample.add_planet_to_list(Planet('Mercury', 1, 1, 4))
sample.add_planet_to_list(Planet('Venus', 2, 3, 5))
sample.add_planet_to_list(Planet('Earth', 3, 2, 3))
sample.sorted_by('DISTANCE')
sample.sorted_by('MASS')
sample.sorted_by('DIAMETER')
