from host import Host
from instruction import Instruction
from virusmachine import VirusMachine

def cantor(t1, t2):
    h1 = Host(t1)
    h2 = Host(t2)
    h3 = Host()
    h4 = Host(1)
    h5 = Host()
    env = Host(0)
    
    hosts = [h1,h2,h3,h4,h5,env]
    
    i1 = Instruction(h2, h3, 2)
    i2 = Instruction(h3, h2)
    i3 = Instruction(h3, h1)
    i4 = Instruction(h2, env)
    i5 = Instruction(h1, h3, 2)
    i6 = Instruction(h3, h1)
    i7 = Instruction(h3, h4)
    i8 = Instruction(h1, h2)
    i9 = Instruction(h4, h3, 2)
    i10 = Instruction(h3, h4)
    i11 = Instruction(h3, h5)
    i12 = Instruction(h2, h1)
    i13 = Instruction(h5, h3)
    i14 = Instruction(h3, h2)
    i15 = Instruction(h3, h5)
    i16 = Instruction(h2, env)
    i17 = Instruction(None, None, None)
    
    instructions = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17]
    
    instruction_connections = [(i1,i1,2),(i1,i2,1),
                               (i2,i3,2),(i2,i4,1),
                               (i3,i2,1),
                               (i4,i4,2),(i4,i5,1),
                               (i5,i5,2),(i5,i6,1),
                               (i6,i7,2),(i6,i8,1),
                               (i7,i6,1),
                               (i8,i9,2),(i8,i12,1),
                               (i9,i9,2),(i9,i10,1),
                               (i10,i11,2),(i10,i8,1),
                               (i11,i10,1),
                               (i12,i12,2),(i12,i13,1),
                               (i13,i13,2),(i13,i14,1),
                               (i14,i15,2),(i14,i16,1),
                               (i15,i14,1),
                               (i16,i16,2),(i16,i17,1)]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    return vm



