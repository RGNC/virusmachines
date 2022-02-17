from host import Host
from instruction import Instruction
from virusmachine import VirusMachine

def power(k, n):
    h1 = Host(k)
    h2 = Host(n)
    h3 = Host()
    h4 = Host()
    h5 = Host()
    h6 = Host(1)
    h7 = Host()
    env = Host()
    
    hosts = [h1,h2,h3,h4,h5,h6,h7,env]
    
    i1 = Instruction(h2,h7)
    i2 = Instruction(h4,h7)
    i3 = Instruction(h6,h4)
    i4 = Instruction(h1,h3,2)
    i5 = Instruction(h3,h1)
    i6 = Instruction(h3,h5)
    i7 = Instruction(h5,h7)
    i8 = Instruction(h4,h3,2)
    i9 = Instruction(h3,h4)
    i10 = Instruction(h3,h6)
    i11 = Instruction(h6,env)
    i12 = Instruction(None, None)
    
    instructions = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12]
    
    # instruction_connections = [(i1,i1,2),(i1,i2,1),(i2,i2,2),(i2,i3,1)]
    instruction_connections = [
        (i1,i2,2),(i1,i11,1),
        (i2,i2,2),(i2,i3,1),
        (i3,i3,2),(i3,i4,1),
        (i4,i4,2),(i4,i5,1),
        (i5,i6,2),(i5,i7,1),
        (i6,i5,1),
        (i7,i8,2),(i7,i1,1),
        (i8,i8,2),(i8,i9,1),
        (i9,i10,2),(i9,i7,1),
        (i10,i9,1),
        (i11,i11,2),(i11,i12,1),
        ]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    return vm



