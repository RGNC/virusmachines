from host import Host
from instruction import Instruction
from virusmachine import VirusMachine

def power(k, n):
    h1 = Host(k)
    h2 = Host(n)
    h3 = Host()
    h4 = Host()
    h5 = Host()
    h6 = Host()
    h7 = Host(1)
    env = Host()
    
    hosts = [h1,h2,h3,h4,h5,h6,h7,env]
    
    i12 = Instruction(h2,h3)
    i5 = Instruction(h1,h4,2)
    i6 = Instruction(h4,h1)
    i7 = Instruction(h4,h6)
    i8 = Instruction(h6,h3)
    i9 = Instruction(h5,h4,2)
    i10 = Instruction(h4,h5)
    i11 = Instruction(h4,h7)
    i13 = Instruction(h7,env)
    i14 = Instruction(h5,h3)
    i15 = Instruction(h7,h5)
    i17 = Instruction(None, None)
    
    instructions = [i12,i5,i6,i7,i8,i9,i10,i11,i13,i14,i15,i17]
    
    # instruction_connections = [(i1,i1,2),(i1,i2,1),(i2,i2,2),(i2,i3,1)]
    instruction_connections = [
        (i12,i14,2),(i12,i13,1),
        (i5,i5,2),(i5,i6,1),
        (i6,i7,2),(i6,i8,1),
        (i7,i6,1),
        (i8,i9,2),(i8,i12,1),
        (i9,i9,2),(i9,i10,1),
        (i10,i11,2),(i10,i8,1),
        (i11,i10,1),
        (i13,i13,2),(i13,i17,1),
        (i14,i14,2),(i14,i15,1),
        (i15,i15,2),(i15,i5,1),
        ]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    return vm



