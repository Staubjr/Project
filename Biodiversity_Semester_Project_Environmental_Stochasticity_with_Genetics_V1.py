import scipy
print(scipy.__version__)

import numpy as np
import math 
import sys
import random
import matplotlib.pyplot as plt


def standard_deviation(list_vals):
    ''' Return the standard error for the list of values '''
    
    length = len(list_vals)
    summed_list = sum(list_vals)
    average = summed_list / length
    
    pairs = []
    
    for index in range(length):
        pairs.append( (list_vals[index] - average)**2 )
        
    numerator = sum(pairs)
    
    STD = (numerator/length)**(1/2)
    
    return(STD)
    
    
class individual:
    
    def __init__(self, sex):
        
        self.sex = sex
        self.single = True
        
        if sex == 'male':
            self.male = True
            self.female = False
        
        if sex == 'female':
            self.female = True
            self.male = False
            
        self.living = True
            
        self.parent_1 = []
        self.parent_2 = []        
        self.genotype = []
        
        self.mate = []
        self.check_mate_number()

    def check_mate_number(self):
        if len(self.mate) > 1:
            raise Exception('Uh oh! Looks like this penguin is getting hot and heavy with                              another bird...')
                
class mating_pairs:
    
    def __init__(self, individual_1, individual_2):
        self.penguin_1 = individual_1
        self.penguin_2 = individual_2
        individual_1.check_mate_number()
        individual_2.check_mate_number()
        
        
    def reproduce(self):
        '''Reproduce and get genotypes between mating pairs '''
        
        
        random_number_allele_1 = random.randint(0,1)
        
        if random_number_allele_1 == 0:
            allele_1 = self.penguin_1.genotype[0]   
            
        if random_number_allele_1 == 1:
            allele_1 = self.penguin_1.genotype[1]
                
        random_number_allele_2 = random.randint(0,1)
                
        if random_number_allele_2 == 0:
            allele_2 = self.penguin_2.genotype[0]
            
        if random_number_allele_2 == 1:
            allele_2 = self.penguin_2.genotype[1]
            
        genotype = [allele_1, allele_2]
            
        random_sex_number = random.uniform(0,1)
        
        if random_sex_number <= 0.5:
            sex = 'male'
            
        if random_sex_number > 0.5:
            sex = 'female'
            
        baby = individual(sex)
        baby.genotype = genotype
        baby.parent_1 = self.penguin_1
        baby.parent_2 = self.penguin_2
        
        if len(baby.genotype) > 2:
            print(baby.genotype)
            raise Exception('Hey guy this individual has more than 2 alleles. WTF!')
            
        if baby.male == True and baby.female == True:
            raise Exception('This bird done got 2 sexes!')
            
        if baby.male == False and baby.female == False:
            raise Exception('This bird ain\'t got no sex!')  
            
        return baby

class population:
    
    no_nino_lambdas = 1.3
    
    el_nino_lambda = 0.3
    
    el_nino_frequency = 5
        
    carrying_capacity = 2000
    
    initial_population_size = 500
    
    minimum_population = 10
    
    minimum_effective_population = 35
    
    trial_number = 100
    
    def __init__(self):
        self.el_nino_frequency = population.el_nino_frequency
        self.minimum_population = population.minimum_population
        self.minimum_effective_population = population.minimum_effective_population
        self.el_nino_lambda = population.el_nino_lambda
        self.no_nino_lambda = population.no_nino_lambdas
        self.trials = population.trial_number
        self.extinctions = 0
        self.extantions = 0
        self.carrying_capacities_hit = 0
        self.minimum_effective_polulations_hit = 0
        self.list_of_individuals = []
        self.list_of_females = []
        self.list_of_males = []
        self.list_of_mating_pairs = []
        self.generations = []
        self.homo_A = []
        self.homo_B = []
        self.heteros = []
        
        
    def initialize_population(self):
        ''' This makes the first however many individuals for the first 
            parent genration in the population. This function needs to be passed
            a value for the percent of the A and B alleles in the population; otherwise,
            we will let it default to A = 0.5 and B = 0.5 '''
            
        A = 0.5
        # B = 0.5
        # Do not need B as a constrains B
        
        for individual_index in range(0 , population.initial_population_size):
            
            random_number_allele_1 = random.uniform(0,1)
            random_number_allele_2 = random.uniform(0,1)
            random_number_sex = random.uniform(0,1)
            
            if random_number_allele_1 <= A:
                allele_1 = 'A'
            
            if random_number_allele_1 > A:
                allele_1 = 'B'
                
                
            if random_number_allele_2 <= A:
                allele_2 = 'A'
                
            if random_number_allele_2 > A:
                allele_2 = 'B'
                
            genotype = [allele_1, allele_2]
            
            if random_number_sex <= 0.5:
                sex = 'male'
                
            if random_number_sex > 0.5:
                sex = 'female'

            
            indiv = individual(sex)
            indiv.genotype = genotype
                        
            self.list_of_individuals.append(indiv)
            
            if indiv.sex == 'male':
                self.list_of_males.append(indiv)
                
            else:
                self.list_of_females.append(indiv)
                
            
    def find_mating_pairs(self):
        ''' We are maximizing the potential mating pairs that we can have. 
            Also, note how we are checking if the penguin is single, then we
            look at the sex of the penguin when we are determining whether
            to put the penguin in the list of single females or single males. '''
        
        single_females = []
        single_males = []
        
        for penguin in self.list_of_individuals:
            if penguin.single == True:
                
                if penguin.sex == 'male':
                    single_males.append(penguin)
                    
                    
                if penguin.sex == 'female':
                    single_females.append(penguin)
                    

        total_boys = len(single_males)
        total_girls = len(single_females)
            
        if total_girls >= total_boys:
            for male_penguin in single_males:
                mate_number = random.randint(0, len(single_females)-1)
                
                #### Mate the penguins ####
                male_penguin.mate.append(single_females[mate_number])
                male_penguin.single = False
                
                single_females[mate_number].mate.append(male_penguin)
                single_females[mate_number].single = False
                
                #### Create the mating pair object in the mating pair class ####
                pair_of_mates = mating_pairs(male_penguin, single_females[mate_number])
                self.list_of_mating_pairs.append(pair_of_mates)
                
                #### Remove the mates from the potential mate list ####
                single_females.pop(mate_number)
                
                
        if total_boys > total_girls:
            for female_penguin in single_females:
                mate_number = random.randint(0, len(single_males)-1)
                
                #### Mate the penguins ####
                female_penguin.mate.append(single_males[mate_number])
                female_penguin.single = False
                
                single_males[mate_number].mate.append(female_penguin)
                single_males[mate_number].single = False
                
                #### Create the mating pair object in the mating pair class ####
                pair_of_mates = mating_pairs(single_males[mate_number], female_penguin)
                self.list_of_mating_pairs.append(pair_of_mates)
                
                #### Remove the mates from the potential mate list ####
                single_males.pop(mate_number)
                
                
    def mate_the_pairs(self):
        ''' Mates them and we are just choosing a number between 0-3 for 
            how many eggs they can have successfully.  Note for the environmental
            stochasticity model we have to do maximum fecundity because else wise
            we won't have enough individuals to meet the new populaion size'''
        
        for pair_of_penguins in self.list_of_mating_pairs:
#            fecundity = random.randint(0,3)
            fecundity = 3
            
            for baby_penguin in range(fecundity):
                baby = pair_of_penguins.reproduce()
                
                self.list_of_individuals.append(baby)
                
                if baby.male == True:
                    self.list_of_males.append(baby)
                    
                if baby.female == True:
                    self.list_of_females.append(baby)
                    
#    def determine_survival_demographic_stochasticity(self):
#        ''' This method determiens how many of the individuals survive.
#            I am thinking this is where a lot of the assumptions will come into
#            play. First, we are simulating demographic stochasticity and we
#            want N to stay relatively fixed, we can do that.  We will keep it 
#            around approximately 500 individuals, our initial population size.'''
#         
#            
#        #### First we need to determine the survivors ####
#            
#        Number_to_Survive = population.initial_population_size
#        Surviving_Penguins = []
#        
#        for index in range(Number_to_Survive):
#            penguin_index = random.randint(0, len(self.list_of_individuals) - 1)
#            Surviving_Penguins.append(self.list_of_individuals[penguin_index])
#            self.list_of_individuals.pop(penguin_index)
#                            
#        #### Clear out the list of individuals, males, and females ####
#    
#        del self.list_of_individuals[0: len(self.list_of_individuals)]
#        del self.list_of_males[0: len(self.list_of_males)]
#        del self.list_of_females[0: len(self.list_of_females)]
#        del self.list_of_mating_pairs[0: len(self.list_of_mating_pairs)]
#        
#        
#        #### Update all the lists of individuals ####
#        
#        for penguin in Surviving_Penguins:
#            self.list_of_individuals.append(penguin)
#        
#        for penguin in self.list_of_individuals:
#            
#            if penguin.sex == 'male':
#                self.list_of_males.append(penguin)
#                
#            if penguin.sex == 'female':
#                self.list_of_females.append(penguin)
#                
#        
#        #### Now we need to update all of our mating pairs.  First, let's find
#        #### out which of our pairs are still around.  Then we will update their
#        #### single parameter and we will find new mates for the others in the next
#        #### generation.
#        
#        mate_check_list = []
#        
#        for penguin in self.list_of_individuals:
#            mate_check_list.append(penguin)
#                        
#        for penguin in mate_check_list:
#            
#            if len(penguin.mate) == 1:
#                mate_alive = False
#                
#                
#                for mate_index in range(0, len(mate_check_list)):    
#                    if penguin.mate[0] == mate_check_list[mate_index]:
#                        mate_alive = True
#                        true_mate = mate_check_list[mate_index]
#                        
#            if len(penguin.mate) == 0:
#                mate_alive = False
#                        
#                        
#            if mate_alive == False:
#                penguin.single = True
#                if len(penguin.mate) == 1:
#                    penguin.mate.pop(0)
#            
#            if mate_alive == True:
#                penguin.single == False
#                couple = mating_pairs(penguin, true_mate)
#                self.list_of_mating_pairs.append(couple)
#                mate_check_list.pop(mate_index)
                    
    def el_nino_year(self):
        ''' Need to find the new population size for the environmental stochasticity
            model and we need to find if the poulation dies out '''
        
        random_number = random.uniform(0,1)
        
        el_nino = False
        
        if random_number <= 1/self.el_nino_frequency:
            el_nino = True
            
        if el_nino == True:
            new_pop = len(self.list_of_individuals) * population.el_nino_lambda
            new_pop_size = int(round(new_pop))
            
        if el_nino == False:
            new_pop = len(self.list_of_individuals) * population.no_nino_lambdas
            new_pop_size = int(round(new_pop))
        
        if new_pop_size <= population.minimum_population:
            new_pop_size = 0
            
        if new_pop_size >= population.carrying_capacity:
            new_pop_size = population.carrying_capacity

        return new_pop_size
            
                    
    def determine_survival_environmental_stochasticity(self, new_pop_size):
        ''' This method determines how many of the individuals survive.
            I am thinking this is where a lot of the assumptions will come into
            play. First, we are simulating environmental stochasticity and we
            want to let the N vary due to the el nino year or severity.'''
         
            
        #### First we need to determine the survivors ####
            
        Number_to_Survive = new_pop_size
        Surviving_Penguins = []
        
        for index in range(Number_to_Survive):
            penguin_index = random.randint(0, len(self.list_of_individuals) - 1)
            Surviving_Penguins.append(self.list_of_individuals[penguin_index])
            self.list_of_individuals.pop(penguin_index)
                            
        #### Clear out the list of individuals, males, and females ####
    
        del self.list_of_individuals[0: len(self.list_of_individuals)]
        del self.list_of_males[0: len(self.list_of_males)]
        del self.list_of_females[0: len(self.list_of_females)]
        del self.list_of_mating_pairs[0: len(self.list_of_mating_pairs)]
        
        
        #### Update all the lists of individuals ####
        
        for penguin in Surviving_Penguins:
            self.list_of_individuals.append(penguin)
        
        for penguin in self.list_of_individuals:
            
            if penguin.sex == 'male':
                self.list_of_males.append(penguin)
                
            if penguin.sex == 'female':
                self.list_of_females.append(penguin)
                
        
        #### Now we need to update all of our mating pairs.  First, let's find
        #### out which of our pairs are still around.  Then we will update their
        #### single parameter and we will find new mates for the others in the next
        #### generation.
        
        mate_check_list = []
        
        for penguin in self.list_of_individuals:
            mate_check_list.append(penguin)
                        
        for penguin in mate_check_list:
            
            if len(penguin.mate) == 1:
                mate_alive = False
                
                
                for mate_index in range(0, len(mate_check_list)):    
                    if penguin.mate[0] == mate_check_list[mate_index]:
                        mate_alive = True
                        true_mate = mate_check_list[mate_index]
                        
            if len(penguin.mate) == 0:
                mate_alive = False
                        
                        
            if mate_alive == False:
                penguin.single = True
                if len(penguin.mate) == 1:
                    penguin.mate.pop(0)
            
            if mate_alive == True:
                penguin.single == False
                couple = mating_pairs(penguin, true_mate)
                self.list_of_mating_pairs.append(couple)
                mate_check_list.pop(mate_index)                    
                
    def calculate_heterozygosity(self):
        ''' Just finding the amount of homozygotes for A, heterozygotes,
            and homozygotes for B '''
            
#        Number_of_Alleles = len(self.list_of_individuals) * 2
        
        homo_A = 0
        heteros = 0
        homo_B = 0
        
        for penguin in self.list_of_individuals:
            if penguin.genotype[0] == 'A' and penguin.genotype[1] == 'A':
                homo_A += 1
            
            if penguin.genotype[0] == 'A' and penguin.genotype[1] == 'B':
                heteros += 1
                
            if penguin.genotype[0] == 'B' and penguin.genotype[1] == 'A':
                heteros += 1
                
            if penguin.genotype[0] == 'B' and penguin.genotype[1] == 'B':
                homo_B += 1
                
        homo_A_percent = homo_A / len(self.list_of_individuals)
        H = heteros / len(self.list_of_individuals)
        homo_B_percent = homo_B / len(self.list_of_individuals)
        
        demographics = [homo_A_percent, H, homo_B_percent]
        
        return(demographics)
                
        

def main():
    
    #### Make a list of the generation ####
    generations = []

    for i in range(0,100):
        generations.append(i)
        
        
    homo_A = []
    uncertainty_homo_A = []
    
    hetero = []
    uncertainty_hetero = []
    
    homo_B = []
    uncertainty_homo_B = []
    
    all_my_populations = []
    
    
    pop_number = 0
    
    for pop in range(100):
        print(pop_number)
        
        pop = population()
        pop.initialize_population()
        vals = pop.calculate_heterozygosity()
        pop.generations.append(0)
        pop.homo_A.append(vals[0])
        pop.heteros.append(vals[1])
        pop.homo_B.append(vals[2])
            
        for generation_index in range(1, 100):
            
            pop.find_mating_pairs()
            new_size_population = pop.el_nino_year()
            pop.mate_the_pairs()
            
            if new_size_population > 0:
            
                pop.determine_survival_environmental_stochasticity(new_size_population)        
                vals = pop.calculate_heterozygosity()
                
                pop.generations.append(generation_index)
                pop.homo_A.append(vals[0])
                pop.heteros.append(vals[1])
                pop.homo_B.append(vals[2]) 
                
            if new_size_population == 0:
                pop.generations.append(generation_index)
                pop.homo_A.append(0)
                pop.heteros.append(0)
                pop.homo_B.append(0)                 
        
        all_my_populations.append(pop)
        pop_number += 1
     
    for year in range(100):
        
        A = []
        B = []
        AB = []
        
        for pop in all_my_populations:
            A.append(pop.homo_A[year])
            B.append(pop.homo_B[year])
            AB.append(pop.heteros[year])
        
        tot_A = sum(A)
        tot_B = sum(B)
        tot_AB = sum(AB)
        
        A_val = tot_A/len(A)
        B_val = tot_B/len(B)
        AB_val = tot_AB/len(AB)
        
        A_unc = standard_deviation(A)
        B_unc = standard_deviation(B)
        AB_unc = standard_deviation(AB)
        
        homo_A.append(A_val)
        homo_B.append(B_val)
        hetero.append(AB_val)
        uncertainty_homo_A.append(A_unc)
        uncertainty_homo_B.append(B_unc)
        uncertainty_hetero.append(AB_unc)
                
    saveFile = open('Environmental_Stochasticity_Data.txt', 'w')
    
    for index in range(len(generations)):
        saveFile.write(str(generations[index]))
        saveFile.write(' , ')
        saveFile.write(str(homo_A[index]))
        saveFile.write(' , ')
        saveFile.write(str(uncertainty_homo_A[index]))
        saveFile.write(' , ')
        
        saveFile.write(str(hetero[index]))
        saveFile.write(' , ')
        saveFile.write(str(uncertainty_hetero[index]))
        saveFile.write(' , ')
        
        saveFile.write(str(homo_B[index]))
        saveFile.write(' , ')
        saveFile.write(str(uncertainty_homo_B[index]))
        
        saveFile.write('\n')
        
    saveFile.close()
           
    fig, ax = plt.subplots()
#    ax.scatter(generations, homo_A, color = 'r', label = 'A Homozygous')
#    ax.errorbar(generations, homo_A, yerr = uncertainty_homo_A, capsize = 5, linewidth = 1, color = 'k', fmt = ' ')
    ax.scatter(generations, hetero, color = 'm', label = 'Heterozygous')
    ax.errorbar(generations, hetero, yerr = uncertainty_hetero, capsize = 5, linewidth = 1, color = 'k', fmt = ' ')
#    ax.scatter(generations, homo_B, color = 'b', label = 'B Homozygous')
#    ax.errorbar(generations, homo_B, yerr = uncertainty_homo_B, capsize = 5, linewidth = 1, color = 'k', fmt = ' ')
    ax.set_xlabel('Generation (years)')
    ax.set_ylabel('Percent of Population')
    ax.legend( title = 'Parameter:')
    
#    fig.savefig('Environmental_Stochasticity_H_with_error_bars.png', filetype = 'png')
    
    fig.show()
    plt.show()

        
    

#    print(len(pop_1.list_of_individuals), len(pop_1.list_of_females), len(pop_1.list_of_males))
 


    sys.exit(20)
#    fig.savefig('K_Extinction%_Minimum_Eps_Figure.png', filetype = '.png')
#    Z_k = np.zeros([len(el_nino_frequencies), len(el_nino_lambdas)])
#    Z_min_pops = np.zeros([len(el_nino_frequencies), len(el_nino_lambdas)])
#    Z_extinction_probs = np.zeros([len(el_nino_frequencies), len(el_nino_lambdas)])  
    
if __name__ == "__main__":
    main()
