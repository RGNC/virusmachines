import time
import math
from cantor import cantor
from viruslatex import viruslatex

# vm = cantor(3, 4)
# viruslatex(vm, filename="cantor", verbose=True)
for t1 in range(0,50):
    for t2 in range(0,50):
        vm = cantor(t1,t2)
        vm.compute()
        if vm.get_configuration()[-1] == int(((t1+t2)*(t1+t2+1)/2)+t2):
            print(t1, t2, 'OK')
        else:
            print(t1, t2, vm.get_configuration()[-1], int(((t1+t2)*(t1+t2+1)/2)+t2))


