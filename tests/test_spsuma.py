import time
import math
from spsuma import spsuma
from viruslatex import viruslatex
from formalverification import validate

n1 = 3
n2 = 4
vm = spsuma(n1,n2)
vm.compute(verbose = 2, steps = 10)
# viruslatex(vm, filename="suma")
# validate(vm, ["n1-k","n2",1,"k"], "k", {"n1" : n1, "n2" : n2}, {"k" : range(0, n1+1)})
# validate(vm, [0,"n2-k",2,"n1+k"], "n1+1+k", {"n1" : n1, "n2" : n2}, {"k" : range(0, n2+1)})
# validate(vm, [0,0,"#","n1+n2"], "n1+n2+3", {"n1" : n1, "n2" : n2}, {})

# viruslatex(vm, filename="suma")
