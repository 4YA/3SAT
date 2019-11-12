from argparse import ArgumentParser
from random import random, sample
from satispy import Variable, Cnf
from satispy.solver import Minisat
from satispy.io import DimacsCnf


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

    exp = Cnf()
    parser = ArgumentParser()
    parser.add_argument("-v", dest="variable" ,type=int, default=5)
    parser.add_argument("-l", dest="literal" ,type=int, default=3)
    parser.add_argument("-c", dest="clause" ,type=int, default=25)
    parser.add_argument("-f", dest = "file_name",type=str, default = "instance")
    args = parser.parse_args()

    v = []
    for i in range(args.variable):
        v.append(Variable('v%d' % (i+1)))
    
    for i in range(args.clause):
        c = Cnf()
        
        k = sample(v,args.literal)
        for j in k:
            if random() >= 0.5:
                c |= j
            else:
                c |= -j
        exp &= c

    solver = Minisat()
    solution = solver.solve(exp)

    
    dimacsCnf = DimacsCnf()
    print(dimacsCnf.tostring(exp))
    if solution.error != False:
        print("Error:")
        print(solution.error)
        
    elif solution.success:
        print("Success:")
        for i in range(args.variable):
            print(v[i], solution[v[i]])
        
        fo = open('%s.in' % (args.file_name),"w")
        fo.write(dimacsCnf.tostring(exp))
        fo.close()

        fo = open('answer.dat',"w")
        for i in range(args.variable):
            fo.write(str(v[i]) + " " + str(solution[v[i]]) + "\n")
        fo.close()
       
    else:
        print("The expression cannot be satisfied")

        fo = open('%s.in' % (args.file_name),"w")
        fo.write(dimacsCnf.tostring(exp))
        fo.close()