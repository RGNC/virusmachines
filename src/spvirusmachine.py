import math
import random
import virusmachine

class SPVirusMachine(virusmachine.VirusMachine):

    def __init__(self, hosts, instructions, initial_instructions, instruction_connections, non_determinism = False):
        self.hosts = hosts
        self.instructions = instructions
        self.instruction_connections = instruction_connections
        self.non_determinism = non_determinism
        self.current_step = 0
        self.initial_instructions = initial_instructions
        self.current_instructions = self.initial_instructions

    def restart(self):
        for h in self.hosts:
            h.viruses = h.init_viruses
        self.current_instructions = self.initial_instructions
        self.current_step = 0

    def step(self):
        if self.current_instructions:
            open_channels = dict()
            instructions_upper = set()
            instructions_lower = set()
            for instruction in self.current_instructions:
                if instruction.origin_host:
                    if not (instruction.origin_host in open_channels):
                        open_channels[instruction.origin_host] = set()
                    open_channels[instruction.origin_host].add((instruction, self.hosts.index(instruction.objective_host)))
            new_viruses = [0] * len(self.hosts)
            for origin_host in open_channels:
                objective_hosts = set()
                selected_objective_hosts = set()
                o_hosts_number = 0
                # Open channels
                for host in open_channels[origin_host]:
                    if not (host[1] in objective_hosts):
                        objective_hosts.add(host[1])
                        o_hosts_number += 1
                # Select objective hosts for viruses
                if o_hosts_number <= origin_host.viruses:
                    new_viruses[self.hosts.index(origin_host)] -= o_hosts_number
                    selected_objective_hosts = objective_hosts
                    for elem in open_channels[origin_host]:
                        instructions_upper.add(elem[0])
                        new_viruses[elem[1]] += elem[0].multiplier
                else:
                    available_viruses = origin_host.viruses
                    new_viruses[self.hosts.index(origin_host)] = 0
                    selected_objective_hosts = random.sample(objective_hosts, available_viruses)
                    for elem in open_channels[origin_host]:
                        if elem[1] in selected_objective_hosts:
                            new_viruses[elem[1]] += elem[0].multiplier
                            instructions_upper.add(elem[0])
                        else:
                            instructions_lower.add(elem[0])
            # Add viruses to hosts
            for host_index in range(len(new_viruses)):
                self.hosts[host_index].viruses += new_viruses[host_index]
            # Select new set of instructions
            new_instructions = set()
            for instruction in instructions_upper:
                next_instructions = self.next_instructions(instruction)
                if len(next_instructions):
                    if self.non_determinism and (next_instructions[0][1] == next_instructions[1][1]):
                        index = random.randint(0, len(next_instructions) - 1)
                        new_instructions.add(next_instructions[index][0])
                    else:
                        new_instructions.add(next_instructions[0][0])
            for instruction in instructions_lower:
                next_instructions = self.next_instructions(instruction)
                if len(next_instructions):
                    if self.non_determinism and (next_instructions[0][1] == next_instructions[1][1]):
                        index = random.randint(0, len(next_instructions) - 1)
                        new_instructions.add(next_instructions[index][0])
                    else:
                        new_instructions.add(next_instructions[-1][0])
            self.current_instructions = new_instructions
            # Finish step
            self.current_step += 1
            return self.get_configuration()
        else:
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
        # config.append(self.instructions.index(self.current_instruction) + 1 if self.current_instruction else "#")
        # config.insert(-1, self.instructions.index(self.current_instruction) + 1 if self.current_instruction else "#")
        config.insert(-1, [self.instructions.index(x) for x in self.current_instructions])
        return config

    def set_host_viruses(self, host, viruses):
        self.hosts[host].viruses = viruses

    def get_printable_configuration(self):
        strout = 'C_{' + str(self.current_step) + '} = '
        config = self.get_configuration()
        for i in range(len(config[-2])):
            config[-2][i] += 1
        # if not (config[-2] == '#'):
        #     config[-2] = 'i_{' + str(config[-2]) + '}'
        strout += str(config)
        return strout

    def compute(self, verbose = 0, steps = 10000000000000000000000):
        init_step = self.current_step
        if verbose == 1:
            print(self.get_configuration())
        elif verbose == 2:
            print(self.get_printable_configuration())
        while (self.current_step - init_step < steps) and self.step() and self.current_instructions:
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
        for h in range(1,n_hosts):
            viruses = '' if not self.hosts[h].viruses else str(self.hosts[h].viruses)
            hosts_code += '  \host{' + str(h) + '}{' + str(4*(h%horizontal_hosts)) + '}{' + str(2*math.floor(h/horizontal_hosts)) + '}{$' + viruses + '$}%\n'
        hosts_code += '  \env{' + str(2*horizontal_hosts) + '}{4}%\n'
        hosts_conns = set()
        for i in range(n_insts):
            insts_code += '  \instruction{' + str(i+1) + '}{' + str(2*(i%horizontal_insts)) + '}{' + str(-4-(2*math.floor(i/horizontal_insts))) + '}%\n'
            if self.instructions[i].origin_host:
                # Here, the code needs the environment to be at the position -1 in the hosts list
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
