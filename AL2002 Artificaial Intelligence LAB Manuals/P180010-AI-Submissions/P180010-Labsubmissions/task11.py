import random 
from collections import Counter

class GeneticAlgo:
    def __init__(self, size=3):
        self.size = size
        self.dna = self.generate_dna()
        self.show_dna()
        
        while True:
            self.total_f = 0
            for i in range(len(self.dna)): 
                f = self.fitness_calc(self.dna[i])
                print('Fitness is ', f)
                self.total_f += f
            if self.check_goal:
                return
            selected = self.selection()
            self.dna = self.crossover(self.dna)
            self.mutation()
            print()
            self.show_dna()
            
    def generate_dna(self, n=8):
        size = self.size * self.size
        parents = []
        parents.append([0] * size)
        print(parents)
        
        for i in range(n-1):
            p = []
            for j in range(size):
                x = random.randint(0,1)
                p.append(x)
            parents.append(p)
        return parents
    
    def show_dna(self):
        for i in range(len(self.dna)):
            print(self.dna[i])
    
    def check_goal(self):
        size = self.size * self.size
        for i in range(len(self.dna)):
            if self.fitness_calc(self.dna[i] == size):
                print(f"Goal Achieved {self.dna[i]} Fitness(P{i+1}) = ",self.fitness_calc(self.dna[i]))
                return True
        
    def fitness_calc(self,dna):
        c = Counter(dna)
        size = self.size * self.size
        return c[1]
    
    def select_sec(self, seq):
        return seq[1]
    
    def crossover(self,predescessor):
        size = self.size * self.size
        divid = random.randint(1,size-1)
        p1,p2,p3,p4 = predescessor[0],predescessor[1],predescessor[2],predescessor[3]
        
        # print("Crossover = ",divid)
        # print("P1 = ",p1)
        # print("P3 = ",p3)

        f_h_p1 = p1[:divid]
        f_h_p3 = p3[:divid]
        f_h_p2 = p2[:divid]
        f_h_p4 = p4[:divid]
        s_h_p1 = p1[divid:]
        s_h_p3 = p3[divid:]
        s_h_p2 = p2[divid:]
        s_h_p4 = p4[divid:]
        c1 = f_h_p1 + s_h_p3
        c2 = f_h_p3 + s_h_p1
        c3 = f_h_p2 + s_h_p4
        c4 = f_h_p4 + s_h_p2
    
        
        return [c1,c2,c3,c4]
    def selection(self):
        l = []
        for i in range(len(self.dna)):
            prob = self.fitness_calc(self.dna[i]) / self.total_f
            print(f"Probability of (P{i+1}) = ",prob)
            l.append((i,prob))
        
        l.sort(key=self.select_sec,reverse = True)
        print ("gdfgdfgdf lllll : ",l)
        
        return (l)
    
    def mutation(self):
        size = self.size * self.size
        m = random.randint(0,size-1)
        for chromosome in self.dna:
            m = random.randint(0,size-1)
            chromosome[m] = 1
    

g = GeneticAlgo()        
            