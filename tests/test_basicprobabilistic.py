import time
from basicprobabilistic import basicprobabilistic
from viruslatex import viruslatex

n = 1000
p = 0.5
vm = basicprobabilistic(n,p)
print(vm.compute())
viruslatex(vm, filename="prob")
