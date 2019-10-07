import unittest
from logger import Logger
from person import Person
from simulation import Simulation
from virus import Virus
import random


class MyTestCase(unittest.TestCase):

    def test_virus_instantiation(self):
        #TODO: Create your own test that models the virus you are working with
        '''Check to make sure that the virus instantiator is working.'''
        virus = Virus("HIV", 0.8, 0.3)
        assert virus.name == "HIV"
        assert virus.repro_rate == 0.8
        assert virus.mortality_rate == 0.3

    def test_logger_instantiation(self):
        """Checks if data is corrently being written in file answer.txt """
        name = "Tongue"
        pop = 10
        vacc = 0.4
        mortality = 0.7
        initial_infected = 1
        log = Logger("answers.txt")
        log.write_metadata(name, pop, vacc, mortality, initial_infected)
        file = open("answers.txt", 'r')
        value = file.readline()
        assert value.strip() == f"Virus name:{name}, Population size:{pop},VACCINATION %:{vacc}, Morality rate:{mortality}, INITIALLY INFECTED:{initial_infected}"  # Strip removes /n

    def test_simulation(self):
        pop_size = 100
        vacc_percentage = 0.5
        initial_infected = 1
        virus = Virus("Dysentery", 0.5, 0.5)
        sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)
        sim.run()
        assert sim.total_dead <= pop_size * vacc_percentage
        pass

    def test_vacc_person_instantiation(self):
        # create some people to test if our init method works as expected
        person = Person(1, True)
        assert person._id == 1
        assert person.is_alive is True
        assert person.is_vaccinated is True
        assert person.infection is None

    def test_not_vacc_person_instantiation(self):
        person = Person(2, False)
        assert person._id == 2
        assert person.is_vaccinated is False
        assert person.is_alive is True
        assert person.infection is None

    # TODO: complete your own assert statements that test
    # the values at each attribute
    # assert ...
        pass

    def test_sick_person_instantiation(self):
        # Create a Virus object to give a Person object an infection
        virus = Virus("Dysentery", 0.7, 0.2)
        # Create a Person object and give them the virus infection
        person = Person(3, False, virus)
        person_2 = Person(23, False, virus)
        # TODO: complete your own assert statements that test
        assert person.infection is not None
        assert person.did_survive_infection() is False
        print(person_2.did_survive_infection())
        # the values at each attribute
        # assert ...
        pass

    def test_did_survive_infection(self):
        # TODO: Create a Virus object to give a Person object an infection
        virus = Virus("Dysentery", 0.7, 0.2)
        # TODO: Create a Person object and give them the virus infection
        person = Person(4, False, virus)

        # Resolve whether the Person survives the infection or not
        survived = person.did_survive_infection()
        # Check if the Person survived or not
        if survived:
            assert person.is_alive is True
            assert person.infection is None
            assert person.is_vaccinated is True
            # TODO: Write your own assert statements that test
            # the values of each attribute for a Person who survived
            # assert ...
        else:
            assert person.is_alive is False
            assert person.infection is None
            assert person.is_vaccinated is False
            # TODO: Write your own assert statements that test
            # the values of each attribute for a Person who did not survive
            # assert ...
            pass


if __name__ == '__main__':
    unittest.main()
