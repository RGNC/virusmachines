import math

class VirusMachine(object):

    def __init__(self, hosts, instructions, instruction_connections):
        self.hosts = hosts
        self.instructions = instructions
        self.instruction_connections = instruction_connections
        self.current_step = 0
        self.current_instruction = self.instructions[0]

    def restart(self):
        for h in self.hosts:
            h.viruses = h.init_viruses
        self.current_instruction = self.instructions[0]
        self.current_step = 0

    def step(self):
        if self.current_instruction.origin_host:
            origin_host = self.current_instruction.origin_host
            objective_host = self.current_instruction.objective_host
            multiplier = self.current_instruction.multiplier
            next_instructions = self.next_instructions(self.current_instruction)
            if origin_host.viruses:
                origin_host.viruses -= 1
                objective_host.viruses += 1 * multiplier
                if len(next_instructions):
                    self.current_instruction = next_instructions[0][0]
                else:
                    self.current_instruction = None
                self.current_step += 1
            else:
                if len(next_instructions):
                    self.current_instruction = next_instructions[-1][0]
                else:
                    self.current_instruction = None
                self.current_step += 1
            return self.get_configuration()
        else:
            self.current_instruction = None
            self.current_step += 1
            return None

    def next_instructions(self, current_instruction):
        next_instructions = []
        for conn in self.instruction_connections:
            if conn[0] == current_instruction:
                next_instructions.append((conn[1], conn[2]))
        next_instructions.sort(reverse=True, key=lambda x: x[1])
        return next_instructions

    def get_configuration(self):
        config = []
        for h in self.hosts:
            config.append(h.viruses)
        config.insert(-1, self.instructions.index(self.current_instruction) + 1 if self.current_instruction else "#")
        return config

    def get_printable_configuration(self):
        strout = 'C_{' + str(self.current_step) + '} = '
        config = self.get_configuration()
        if config[-2] == '#':
            config[-2] = '#'
        else:
            config[-2] = 'i_{' + str(config[-2]) + '}'
        strout += str(config)
        return strout

    def compute(self, verbose = 0, steps = 10000000000000000000000):
        init_step = self.current_step
        if verbose == 1:
            print(self.get_configuration())
        elif verbose == 2:
            print(self.get_printable_configuration())
        while (self.current_step - init_step < steps) and self.step() and self.current_instruction:
            if verbose == 1:
                print(self.get_configuration())
            elif verbose == 2:
                print(self.get_printable_configuration())
        if verbose == 1:
            print(self.get_configuration())
        elif verbose == 2:
            print(self.get_printable_configuration())
        return (self.current_step - init_step, self.get_configuration())

    def generate_LaTeX(self, vertical_hosts=2, vertical_insts=2, verbose=True):
        latex_code = '\\begin{tikzpicture}\n'
        hosts_code = ''
        hostconns_code = ''
        insts_code = ''
        instconns_code = ''
        insthost_code = ''
        legend_code = ''
        n_hosts = len(self.hosts)
        horizontal_hosts = max(1, math.floor(n_hosts / vertical_hosts))
        n_insts = len(self.instructions)
        horizontal_insts = max(1, math.floor(n_insts / vertical_insts))
        max_horizontal = max(horizontal_hosts * 4, horizontal_insts * 2)
        for h in range(n_hosts-1):
            viruses = '' if not self.hosts[h].viruses else str(self.hosts[h].viruses)
            hosts_code += '  \host{' + str(h+1) + '}{' + str(4*(h%horizontal_hosts)) + '}{' + str(2*math.floor(h/horizontal_hosts)) + '}{$' + viruses + '$}%\n'
        hosts_code += '  \env{' + str(2*horizontal_hosts) + '}{4}%\n'
        hosts_conns = set()
        for i in range(n_insts):
            insts_code += '  \instruction{' + str(i+1) + '}{' + str(2*(i%horizontal_insts)) + '}{' + str(-4-(2*math.floor(i/horizontal_insts))) + '}%\n'
            if self.instructions[i].origin_host:
                origin = 'env' if self.hosts.index(self.instructions[i].origin_host) == (n_hosts-1) else str(self.hosts.index(self.instructions[i].origin_host)+1)
                objective = 'env' if self.hosts.index(self.instructions[i].objective_host) == (n_hosts-1) else str(self.hosts.index(self.instructions[i].objective_host)+1)
                multiplier = '' if self.instructions[i].multiplier == 1 else str(self.instructions[i].multiplier)
                if verbose:
                    inst = 'i_{' + str(i+1) + '}'
                    orig = 'h_{' + origin + '}'
                    obj = 'env' if objective == 'env' else 'h_{' + objective + '}'
                    legend_code += '  \legend{' + str(max_horizontal + 2) + '}{' + str(vertical_hosts*2-i) + '}{' + inst + '}{' + orig + '}{' + obj + ('' if multiplier == '' else '\hspace{1mm}(' + multiplier + ')') + '}%\n'
                if not (origin, objective) in hosts_conns:
                    hosts_conns.add((origin, objective))
                    hostconns_code += '  \hostconn[10]{' + multiplier + '}{above}{' + origin + '}{' + objective + '}%\n'
                insthost_code += '  \insthost[45]{i' + str(i+1) + '}{h' + origin + 'h' + objective + '}%\n'
        for ic in self.instruction_connections:
            weight = '' if ic[2] == 1 else str(ic[2])
            origin = str(self.instructions.index(ic[0])+1)
            objective = str(self.instructions.index(ic[1])+1)
            instconns_code += '  \instconn[10]{' + weight + '}{above}{' + origin + '}{' + objective + '}%\n'
        latex_code += '\n  % HOSTS\n\n' + hosts_code + '\n  % HOSTS CONNECTIONS\n\n' + hostconns_code + '\n  % INSTRUCTIONS\n\n' + insts_code + '\n  % INSTRUCTION CONNECTIONS\n\n' + instconns_code + '\n  % DIGRAPH CONNECTIONS\n\n' + insthost_code
        if verbose:
            latex_code += '\n  % LEGEND\n\n' + legend_code
        latex_code += '\end{tikzpicture}\n'
        return latex_code
