from host import Host
from instruction import Instruction
from virusmachine import VirusMachine

def resto(n, d):
    h1 = Host(n)
    h2 = Host(d)
    h3 = Host()
    h4 = Host()
    h5 = Host()
    h6 = Host()
    env = Host()
    
    hosts = [h1,h2,h3,h4,h5,h6,env]
    
    i1 = Instruction(h1,h3,1)
    i2 = Instruction(h2,h4,1)
    i3 = Instruction(h1,h3,1)
    i4 = Instruction(h3,h5,1)
    i5 = Instruction(h5,env,1)
    i6 = Instruction(None, None, None)
    i7 = Instruction(h2,h4,1)
    i8 = Instruction(h4,h2,1)
    i9 = Instruction(h2,h4,1)
    i10 = Instruction(h1,h3,1)
    i11 = Instruction(h3,h5,1)
    i12 = Instruction(h5,env,1)
    i13 = Instruction(h3,h6,1)
    i14 = Instruction(h4,h2,1)
    i15 = Instruction(h2,h4,1)
    i16 = Instruction(h1,h3,1)
    i17 = Instruction(h3,h5,1)
    i18 = Instruction(h5,env,1)
    i19 = Instruction(h3,h6,1)
    
    instructions = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19]
    
    instruction_connections = [(i1,i2,2),(i1,i6,1),(i2,i7,2),(i2,i3,1),(i3,i3,2),(i3,i4,1),(i4,i4,2),(i4,i5,1),(i5,i5,2),(i5,i6,1),(i7,i8,2),(i7,i6,1),(i8,i9,1),(i9,i10,2),(i9,i13,1),(i10,i9,2),(i10,i11,1),(i11,i11,2),(i11,i12,1),(i12,i12,2),(i12,i6,1),(i13,i13,2),(i13,i14,1),(i14,i14,2),(i14,i15,1),(i15,i16,2),(i15,i19,1),(i16,i15,2),(i16,i17,1),(i17,i17,2),(i17,i18,1),(i18,i18,2),(i18,i6,1),(i19,i19,2),(i19,i14,1)]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    return vm



