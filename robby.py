import random


def make_gene(*args):
    if len(args) == 1:
        gene = ""
        gene_length = 243
        for i in range(gene_length):
            gene = gene + str(random.randint(0, 6))
        return gene
    elif len(args) == 3:
        print('3 args')
    else:
        print('to many args')




class Robby:
    gene = ""

    def __init__(self):
        self.gene = make_gene(self)






