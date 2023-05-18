from host import Host
from instruction import Instruction
from spvirusmachine import SPVirusMachine

def spsuma(n1, n2):
    h1 = Host(n1)
    h2 = Host(n2)
    env = Host()
    
    hosts = [h1,h2,env]
    
    i1 = Instruction(h1, env)
    i2 = Instruction(h2, env)
    i3 = Instruction(None, None, None)
    
    instructions = [i1,i2,i3]

    initial_instructions = {i1, i2}
    
    instruction_connections = [(i1,i1,2),(i1,i2,1),
                               (i2,i2,2),(i2,i3,1)]
    
    vm = SPVirusMachine(hosts, instructions, initial_instructions, instruction_connections)

    return vm



