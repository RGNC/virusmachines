from host import Host
from instruction import Instruction
from virusmachine import VirusMachine

def lpd(n):
    h1 = Host(n)
    h2 = Host(2)
    h3 = Host()
    h4 = Host()
    h5 = Host(1)
    env = Host()
    
    hosts = [h1,h2,h3,h4,h5,env]
    
    i1 = Instruction(h2, h3)
    i2 = Instruction(h1, h4)
    i3 = Instruction(h1, h4)
    i4 = Instruction(h4, h1)
    i5 = Instruction(h3, env)
    i6 = Instruction(h5, h2, 2)
    i7 = Instruction(h2, h5)
    i8 = Instruction(h4, h1)
    i9 = Instruction(h3, h2)
    i10 = Instruction(None, None, None)
    
    instructions = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,env]
    
    instruction_connections = [(i1,i2,2),(i1,i3,1),
                               (i2,i1,2),(i2,i6,1),
                               (i3,i4,2),(i3,i5,1),
                               (i4,i9,1),
                               (i5,i5,2),(i5,i10,1),
                               (i6,i7,1),
                               (i7,i8,1),
                               (i8,i8,2),(i8,i9,1),
                               (i9,i9,2),(i9,i1,1)]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    return vm



