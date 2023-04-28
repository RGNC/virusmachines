from host import Host
from probabilisticinstruction import ProbabilisticInstruction
from probabilisticvirusmachine import ProbabilisticVirusMachine

def basicprobabilistic(n, p):
    h1 = Host(n)
    h2 = Host()
    h3 = Host()
    env = Host()

    hosts = [h1,h2,h3,env]

    host_connections = [(h1,h2,1,p),(h1,h3,1,1-p)]

    i1 = ProbabilisticInstruction(h1)
    i2 = ProbabilisticInstruction(None)

    instructions = [i1,i2]

    instruction_connections = [(i1,i1,2),(i1,i2,1)]

    vm = ProbabilisticVirusMachine(hosts, host_connections, instructions, instruction_connections)

    return vm

def suma(n1, n2):
    h1 = Host(n1)
    h2 = Host(n2)
    env = Host()
    
    hosts = [h1,h2,env]
    
    i1 = Instruction(h1, env)
    i2 = Instruction(h2, env)
    i3 = Instruction(None, None, None)
    
    instructions = [i1,i2,i3]
    
    instruction_connections = [(i1,i1,2),(i1,i2,1),
                               (i2,i2,2),(i2,i3,1)]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    return vm
