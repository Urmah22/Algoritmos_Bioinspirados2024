import random

class Antigen:
    def __init__(self, id):
        self.id = id

class Antibody:
    def __init__(self, id, antigen_id):
        self.id = id
        self.antigen_id = antigen_id

class ImmuneSystem:
    def __init__(self, antigen_count, antibody_count):
        self.antigens = [Antigen(i) for i in range(antigen_count)]
        self.antibodies = [Antibody(i, random.randint(0, antigen_count - 1)) for i in range(antibody_count)]

    def evolve_antibodies(self):
        for antibody in self.antibodies:
            antibody.antigen_id = random.randint(0, len(self.antigens) - 1)

    def match_antibodies(self):
        matches = 0
        for antibody in self.antibodies:
            if antibody.antigen_id == antibody.id:
                matches += 1
        return matches

if __name__ == "__main__":
    antigen_count = 5
    antibody_count = 10

    immune_system = ImmuneSystem(antigen_count, antibody_count)

    print("Initial Antibodies:")
    for antibody in immune_system.antibodies:
        print(f"Antibody ID: {antibody.id}, Target Antigen ID: {antibody.antigen_id}")

    print("\nEvolving Antibodies...")
    immune_system.evolve_antibodies()

    print("\nEvolving Antibodies Completed!")
    print("Updated Antibodies:")
    for antibody in immune_system.antibodies:
        print(f"Antibody ID: {antibody.id}, Target Antigen ID: {antibody.antigen_id}")

    print("\nMatching Antibodies with Target Antigens...")
    matches = immune_system.match_antibodies()
    print(f"Number of Antibodies Matching Target Antigens: {matches}/{antibody_count}")