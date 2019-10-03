import random, sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    ''' Main class that will run the herd immunity simulation program.
    Expects initialization parameters passed as command line arguments when file is run.
    Simulates the spread of a virus through a given population.  The percentage of the
    population that are vaccinated, the size of the population, and the amount of initially
    infected people in a population are all variables that can be set when the program is run.
    '''
    def __init__(self, pop_size, vacc_percentage, initial_infected, virus):
        ''' Logger object logger records all events during the simulation.
        Population represents all Persons in the population.
        The next_person_id is the next available id for all created Persons,
        and should have a unique _id value.
        The vaccination percentage represents the total percentage of population
        vaccinated at the start of the simulation.
        You will need to keep track of the number of people currently infected with the disease.
        The total infected people is the running total that have been infected since the
        simulation began, including the currently infected people who died.
        You will also need to keep track of the number of people that have die as a result
        of the infection.
        All arguments will be passed as command-line arguments when the file is run.
        HINT: Look in the if __name__ == "__main__" function at the bottom.
        '''
        # TODO: Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding parts of the simulation.
        # TODO: Call self._create_population() and pass in the correct parameters.
        # Store the array that this method will return in the self.population attribute.
        # TODO: Store each newly infected person's ID in newly_infected attribute.
        # At the end of each time step, call self._infect_newly_infected()
        # and then reset .newly_infected back to an empty list.
        self.logger = None
        self.pop_size = pop_size # Int
        self.next_person_id = 0 # Int
        self.virus = virus # Virus object
        self.initial_infected = initial_infected # Int
        self.total_infected = 0 # Int
        self.current_infected = 0 # Int
        self.total_dead = 0 # Int
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus.name, pop_size, vacc_percentage, initial_infected)
        self.newly_infected = []
        self.vacc_percentage = vacc_percentage  # float between 0 and 1
        self.population = self._create_population(self.initial_infected) # List of Person objects
        print("Population:", len(self.population))

        #self.populationself._create_population(self, initial_infected)

    def _create_population(self, initial_infected):
        person_obj = []
        '''This method will create the initial population.
            Args:
                initial_infected (int): The number of infected people that the simulation
                will begin with.
            Returns:
                list: A list of Person objects.
        '''

        id = 0
        print( "Size of pop:", self.pop_size * self.vacc_percentage)
        print(f"Rest of world: {self.vacc_percentage}")
        try:  # Creates infected people and ID is # of initial_infected
            for pop_infected in range(initial_infected):
                person_obj.append(Person(id, False, self.virus))
                print("Person virus", person_obj[0].infection)
                id += 1
        except Exception:
            print("Could  create  person objects")
        try:
            for pop in range(int(self.pop_size * self.vacc_percentage) - initial_infected): #self.vacc_percentage):
                person_obj.append(Person(id, False, None))
                id += 1
            for pop_vac in range(int(self.pop_size * self.vacc_percentage)):
                person_obj.append(Person(id, True, None))
                id += 1
        except Exception:
            print("Could not create infected Person objects")
        print("length of pop:", len(person_obj))
        return person_obj




        # TODO: Finish this method!  This method should be called when the simulation
        # begins, to create the population that will be used. This method should return
        # an array filled with Person objects that matches the specifications of the
        # simulation (correct number of people in the population, correct percentage of
        # people vaccinated, correct number of initially infected people).

        # Use the attributes created in the init method to create a population that has
        # the correct intial vaccination percentage and initial infected.
        pass

    def _simulation_should_continue(self):
        ''' The simulation should only end if the entire population is dead
        or everyone is vaccinated.
            Returns:
                bool: True for simulation should continue, False if it should end.
        '''
        dead_count = 0
        vacc_count = 0
        for person in self.population:
            if(person.is_alive is False):
                dead_count += 1
            elif(person.is_vaccinated is True):
                vacc_count += 1
        print("Dead people:", dead_count)
        if(dead_count is len(self.population) or vacc_count is len(self.population)):
            return False
        else:
            return True
        # TODO: Complete this helper method.  Returns a Boolean.
        pass

    def run(self):
        ''' This method should run the simulation until all requirements for ending
        the simulation are met.
        '''
        # TODO: Finish this method.  To simplify the logic here, use the helper method
        # _simulation_should_continue() to tell us whether or not we should continue
        # the simulation and run at least 1 more time_step.

        # TODO: Keep track of the number of time steps that have passed.
        # HINT: You may want to call the logger's log_time_step() method at the end of each time step.
        # TODO: Set this variable using a helper
        time_step_counter = 0
        should_continue = self._simulation_should_continue()

        while True:
            time_step_counter += 1
            self.time_step()
            self._infect_newly_infected()
            self._simulation_should_continue()
            if(self._simulation_should_continue() is False):
                break
        # TODO: for every iteration of this loop, call self.time_step() to compute another
        # round of this simulation.

        print(f'The simulation has ended after {time_step_counter} turns., this is the total infected:{self.total_dead}')
        pass

    def time_step(self):
        interaction_counter = 0
        ''' This method should contain all the logic for computing one time step
        in the simulation.
        This includes:
            1. 100 total interactions with a randon person for each infected person
                in the population
            2. If the person is dead, grab another random person from the population.
                Since we don't interact with dead people, this does not count as an interaction.
            3. Otherwise call simulation.interaction(person, random_person) and
                increment interaction counter by 1.
            '''
        for people in self.population:
                print("The entire population", people._id)
        print("End")
        for person in self.population:
            print("Printing the populations", person._id)
            if(person.infection is not None):
                random_num = random.randint(1, len(self.population) - 1)
                random_person = self.population[random_num]
                #print("broken")
                while(True):
                    print("While loop")
                    if(random_person.is_alive is True):
                        for x in range(100):
                            interaction_counter += 1
                            #print("Random Person:", random_person)
                            self.interaction(person, random_person)
                        break

                    else:
                        random_num = random.randint(0, len(self.population)-1)
                        random_person = self.population[random_num]


        # TODO: Finish this method.
        pass

    def interaction(self, person, random_person):
        '''This method should be called any time two living people are selected for an
        interaction. It assumes that only living people are passed in as parameters.
        Args:
            person1 (person): The initial infected person
            random_person (person): The person that person1 interacts with.
        '''
        # Assert statements are included to make sure that only living people are passed
        # in as params
        assert person.is_alive == True
        assert random_person.is_alive == True

        # TODO: Finish this method.
        #  The possible cases you'll need to cover are listed below:
        if(random_person.is_vaccinated is True):
            pass
        elif(random_person.infection is not None):
            pass
        elif(random_person.infection is None and random_person.is_vaccinated is False):
            num = random.uniform(0, 1)
            if(num < self.virus.repro_rate):
                self.newly_infected.append(random_person._id)
        else:
            pass
            # random_person is vaccinated:
            #     nothing happens to random person.
            # random_person is already infected:
            #     nothing happens to random person.
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0 and 1.  If that number is smaller
            #     than repro_rate, random_person's ID should be appended to
            #     Simulation object's newly_infected array, so that their .infected
            #     attribute can be changed to True at the end of the time step.
        # TODO: Call slogger method during this method.
        pass

    def _infect_newly_infected(self):
        ''' This method should iterate through the list of ._id stored in self.newly_infected
        and update each Person object with the disease. '''
        #filter the zombie list
        infected_list = list(set(self.newly_infected))
        print("Length of new zomebilist:", len(infected_list))

        for person in self.population:
            for zombie in infected_list:
                if(person._id == zombie):
                    print("ID:", zombie)
                    person.infection = self.virus
                    if(person.did_survive_infection() is False):
                        self.total_dead += 1
                    print("Did it go through?:", person.infection)
                    self.current_infected += 1
        self.newly_infected = []

        print(self.total_dead)
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        pass


if __name__ == "__main__":
    params = sys.argv[1:]
    virus_name = str(params[0])
    repro_num = float(params[1])
    mortality_rate = float(params[2])

    pop_size = int(params[3])
    vacc_percentage = float(params[4])

    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1

    virus = Virus(virus_name, repro_num, mortality_rate)
    sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

    sim.run()
