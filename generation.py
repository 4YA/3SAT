from argparse import ArgumentParser

from random import random, sample

def generate_clause(variable,literal):
    total_v = [ i for j in (range(-variable,0), range(1, variable+1)) for i in j]
    return sample(total_v, literal)
    
def appendFile(c):
    fo = open("instance.in","a")
    for i in c:
        fo.write(str(i) + " ")
    fo.write(str(0) + "\n")
    fo.close()

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-v", dest="variable" ,type=int, default=5)
    parser.add_argument("-l", dest="literal" ,type=int, default=3)
    parser.add_argument("-c", dest="clause" ,type=int, default=25)
    parser.add_argument("-m", dest="mode" ,type=int, default=1)
    ''' if user select mode = 0, the system will generate 1 unsat 1 sat with same clause, so system would ignore -c argument
        if user select mode = 1, the system just generate an instance with specific number, unsat and sat are possible.'''
    
    args = parser.parse_args()
    fo = open("instance.in","w")
    fo.write("p cnf " + str(args.variable) + " " + str(args.clause) +"\n")
    fo.close()
    if args.mode == 1:
        for i in range(args.clause):
            c = generate_clause(args.variable,args.literal)
            appendFile(c)
    else:
        while(1):
            c = generate_clause(args.variable,args.literal)
            appendFile(c)
      