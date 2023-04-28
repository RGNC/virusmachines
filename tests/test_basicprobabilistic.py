import time
from basicprobabilistic import basicprobabilistic
from viruslatex import viruslatex

n = 1000
p = 0.5
vm = basicprobabilistic(n,p)
print(vm.compute())
# viruslatex(vm, filename="suma")
# validate(vm, ["n1-k","n2",1,"k"], "k", {"n1" : n1, "n2" : n2}, {"k" : range(0, n1+1)})
# validate(vm, [0,"n2-k",2,"n1+k"], "n1+1+k", {"n1" : n1, "n2" : n2}, {"k" : range(0, n2+1)})
# validate(vm, [0,0,"#","n1+n2"], "n1+n2+3", {"n1" : n1, "n2" : n2}, {})

# viruslatex(vm, filename="suma")
