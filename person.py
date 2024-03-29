import unittest
import random

class Person(object):
    ''' Person objects will populate the simulation. '''

    def __init__(self, _id, is_vaccinated, infection=None):

        self._id = _id  # int
        self.is_alive = True  # boolean
        self.is_vaccinated = is_vaccinated  # boolean
        self.infection = infection  # Virus object or None

    def did_survive_infection(self):
        ''' Generate a random number and compare to virus's mortality_rate.
        If random number is smaller, person dies from the disease.
        If Person survives, they become vaccinated and they have no infection.
        Return a boolean value indicating whether they survived the infection.
        '''
        # print("Randome number:", self.infection.mortality_rate)
        if(self.infection is not None):
            print("Randome number:", self.infection.mortality_rate)
            num = random.uniform(0, 1)
            print(num)
            if(num < self.infection.mortality_rate):
                print("Dead")
                self.is_alive = False
                self.infection = None
                return False
            else:
                print("You get to live forever!", self._id, num)
                self.is_vaccinated = True
                self.infection = None
                return True
        # Only called if infection attribute is not None.
        # TODO:  Finish this method. Should return a Boolean


class MyTestCase(unittest.TestCase):

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
        assert person.did_survive_infection() is True
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
            # TODO: Write your own assert statements that test
            # the values of each attribute for a Person who survived
            # assert ...
        else:
            assert person.is_alive is False
            # TODO: Write your own assert statements that test
            # the values of each attribute for a Person who did not survive
            # assert ...
            pass


if(__name__ == '__main__'):
    unittest.main()
