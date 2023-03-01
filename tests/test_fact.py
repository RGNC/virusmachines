import time
import math
from fact import fact
from viruslatex import viruslatex
from formalverification import validate

# for n in range(0, 30):
#     vm = fact(n)
#     vm.compute()
#     if vm.get_configuration()[-1] == math.factorial(n):
#         print(vm.current_step, n, 'OK')
#     else:
#         print(n, vm.get_configuration()[-1], math.factorial(n))

vm = fact(14)
vm.compute()

# validate(vm, ["*","*","*","*","*","*","*","*","*"], "p", {"k" : 10, "n" : 4}, {"p" : range(0,1)})
