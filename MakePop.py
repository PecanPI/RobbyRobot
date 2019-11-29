import random

class makePop:
    genes = 243
    move_options = 6
    gene:
    # 243 genes of random numbers 0-6
    def make_individual(self):
        genes = 243
        move_options = 6
        gene = ""
        for i in range(genes):
            gene += random.randint(6)
