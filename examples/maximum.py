from host import Host
from instruction import Instruction
from virusmachine import VirusMachine

def maximum(n1, n2):
    h1 = Host(n1)
    h2 = Host(n2)
    h3 = Host()
    h4 = Host()
    env = Host()
    
    hosts = [h1,h2,h3,h4,env]
    
    i1 = Instruction(h1, h3)
    i2 = Instruction(h2, h4)
    i3 = Instruction(h1, h3)
    i4 = Instruction(h2, h4)
    i5 = Instruction(h4, env)
    i6 = Instruction(h3, env)
    i7 = Instruction(None, None, None)
    
    instructions = [i1,i2,i3,i4,i5,i6,i7]
    
    instruction_connections = [(i1,i2,2),(i1,i4,1),(i2,i1,2),(i2,i3,1),(i3,i3,2),(i3,i6,1),(i4,i4,2),(i4,i5,1),(i5,i5,2),(i5,i7,1),(i6,i6,2),(i6,i7,1)]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    return vm



