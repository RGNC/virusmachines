import time
import math
from power3 import power
from viruslatex import viruslatex
from formalverification import validate

# for k in range(0,50):
#     for n in range(0,10):
#         vm = power(k,n)
#         vm.compute()
#         if vm.get_configuration()[-1] == k ** n:
#             print(k, n, 'OK')
#         else:
#             print(k, n, vm.get_configuration()[-1], k ** n)
        # print(vm.current_step, n * (1+) + k**n + 3)

vm = power(10,4)
vm.compute(verbose = 2)
# validate(vm, ["*","*","*","*","*","*","*","*","*"], "p", {"k" : 10, "n" : 4}, {"p" : range(0,1)})
