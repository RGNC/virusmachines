from host import Host
from instruction import Instruction
from virusmachine import VirusMachine

def divisible(d, n, iters = 1000000000):
    h1 = Host(d)
    h2 = Host(n)
    h3 = Host(0)
    h4 = Host(0)
    h5 = Host(1)
    env = Host(0)
    
    hosts = [h1,h2,h3,h4,h5,env]
    
    i1 = Instruction(h1, h3, 1)
    i2 = Instruction(h1, h3, 1)
    i3 = Instruction(h2, h4, 1)
    i4 = Instruction(h3, h1, 1)
    i5 = Instruction(h2, h4, 1)
    i6 = Instruction(h4, h2, 1)
    i7 = Instruction(h1, h3, 1)
    i8 = Instruction(h2, h4, 1)
    i9 = Instruction(h3, h1, 1)
    i10 = Instruction(h2, h4, 1)
    i11 = Instruction(h4, h2, 1)
    iYES = Instruction(h5, env, 1)
    iNO = Instruction(None, None, None)
    
    instructions = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,iYES,iNO]
    
    instruction_connections = [(i1,i2,2),(i1,i3,1),(i2,i4,2),(i2,iYES,1),(i3,iNO,2),(i3,iYES,1),(i4,i4,2),(i4,i5,1),(i5,i6,2),(i5,iYES,1),(i6,i7,1),(i7,i8,2),(i7,i9,1),(i8,i7,2),(i8,iNO,1),(i9,i9,2),(i9,i10,1),(i10,i11,2),(i10,iYES,1),(i11,i7,1)]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    # for i in range(100):
    #     print(vm.step())
    return vm.compute(iters)



