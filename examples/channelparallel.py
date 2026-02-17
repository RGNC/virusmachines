from host import Host
from cpinstruction import CPInstruction
from cpvirusmachine import CPVirusMachine

def channelparallel(n, semantics="OR"):
    h1 = Host(n)
    h2 = Host()
    h3 = Host()
    env = Host()
    
    hosts = [h1,h2,h3,env]
    
    i1 = CPInstruction([h1,h1],[h2,h3],[1,1])
    i2 = CPInstruction(None, None, None)
    i3 = CPInstruction(None, None, None)
    
    instructions = [i1,i2,i3]
    
    instruction_connections = [(i1,i2,2),(i1,i3,1)]
    
    vm = CPVirusMachine(hosts, instructions, instruction_connections, semantics)

    return vm
