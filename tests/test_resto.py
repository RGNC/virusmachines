import time
import math
from resto import resto
from viruslatex import viruslatex

for d in range(50):
    for n in range(1, d):
        vm = resto(n, d)
        validate(vm, [0,"d-(n+1)",0,"n+1",0,0,"#","n"], "4*n+7", {"n" : n, "d" : d}, {})
        
vm = resto(n, d)
validate(vm, [0,"d-(n+1)",0,"n+1",0,0,"#","n"], "4*n+7", {"n" : n, "d" : d}, {})

a = vm.compute(30)
print(a)

vm = resto(4,2)
print(vm.compute())


start_time = time.time()
for n in range(500):
    for d in range(2, n+1):
        vm = resto(n, d)
        q = math.floor(n/d)
        r = n-q*d
        ran = list(range(0,q-1))
        if not ran:
            ran = [0]
        ver = validate(vm, ["n-(k+1)*d",0,0,"d",0,"(k+1)*d",14,0], "(3*d+4)+k*(4*d+3)", {"n" : n, "d" : d}, {"k" : ran}, False)
        if not ver[0]:
            print(ver[1])
            exit(-1)
        ver = validate(vm, [0,"d-r-1",0,"r+1",0,"q*d","#","r"], "4*q*d+3*q+4*r+7", {"n" : n, "d" : d, "q" : q, "r" : r}, {}, False)
        if not ver[0]:
            print(ver[1])
            exit(-1)

total_time = time.time() - start_time
print("Total time (s):", total_time)

# n = 1092830
# d = 6
# q = math.floor(n/d)
# ran = list(range(0,q-1))
# vm = resto(10,6)
# viruslatex(vm, filename='resto.tex')
# validate(vm, ["n-(k+1)*d",0,0,"d",0,"(k+1)*d",14,0], "(3*d+4)+k*(4*d+3)", {"n" : n, "d" : d}, {"k" : ran})
# print(vm.generate_LaTeX())
# vm.compute()
# print(vm.get_configuration())
