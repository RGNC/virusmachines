from host import Host
from instruction import Instruction
from virusmachine import VirusMachine

def fact(n):
    h1 = Host(n)
    h2 = Host()
    h3 = Host()
    h4 = Host()
    h5 = Host(1)
    h6 = Host()
    env = Host()
    
    hosts = [h1,h2,h3,h4,h5,h6,env]
    
    i1 = Instruction(h1,h6)
    i2 = Instruction(h6,h4)
    i3 = Instruction(h3,h6)
    i4 = Instruction(h5,h3)
    i5 = Instruction(h1,h2,2)
    i6 = Instruction(h2,h1)
    i7 = Instruction(h2,h4)
    i8 = Instruction(h4,h6)
    i9 = Instruction(h3,h2,2)
    i10 = Instruction(h2,h3)
    i11 = Instruction(h2,h5)
    i12 = Instruction(h5,env)
    i13 = Instruction(None, None)
    
    instructions = [i1,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i2]
    
    # instruction_connections = [(i1,i1,2),(i1,i3,1),(i3,i3,2),(i3,i4,1)]
    instruction_connections = [
        (i1,i2,2),(i1,i12,1),
        (i3,i3,2),(i3,i4,1),
        (i4,i4,2),(i4,i5,1),
        (i5,i5,2),(i5,i6,1),
        (i6,i7,2),(i6,i8,1),
        (i7,i6,1),
        (i8,i9,2),(i8,i1,1),
        (i9,i9,2),(i9,i10,1),
        (i10,i11,2),(i10,i8,1),
        (i11,i10,1),
        (i12,i12,2),(i12,i13,1),
        (i2,i3,1)
        ]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    return vm



