import math
import random
import virusmachine

class ProbabilisticVirusMachine(virusmachine.VirusMachine):

    def __init__(self, hosts, host_connections, instructions, instruction_connections):
        self.hosts = hosts
        self.host_connections = host_connections
        self.instructions = instructions
        self.instruction_connections = instruction_connections
        self.current_step = 0
        if len(instructions):
            self.current_instruction = self.instructions[0]
        else:
            self.current_instruction = None

    def step(self):
        if self.current_instruction.host:
            host = self.current_instruction.host
            next_instructions = self.next_instructions(self.current_instruction)
            if host.viruses:
                host.viruses -= 1
                objective_hosts, cdf = self.next_hosts(host)
                obj_host_index = self.obj_host(cdf)
                objective_host = objective_hosts[obj_host_index][0]
                objective_host_multi = objective_hosts[obj_host_index][1]
                objective_host.viruses += 1 * objective_host_multi
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

    def next_hosts(self, current_host):
        next_hosts = []
        cdf = [0]
        for conn in self.host_connections:
            if conn[0] == current_host:
                next_hosts.append((conn[1], conn[2], conn[3]))
                cdf.append(cdf[-1] + conn[3])
        cdf.pop(0)
        return next_hosts, cdf

    def obj_host(self, cdf):
        rnd = random.random()
        index = 0
        while rnd > cdf[index]:
            index += 1
        return index

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
            viruses = '' if not self.hosts[h-1].viruses else str(self.hosts[h-1].viruses)
            hosts_code += '  \host{' + str(h) + '}{' + str(4*(h%horizontal_hosts)) + '}{' + str(2*math.floor(h/horizontal_hosts)) + '}{$' + viruses + '$}%\n'
        hosts_code += '  \env{' + str(2*horizontal_hosts) + '}{4}%\n'
        hosts_conns = set()
        for i in range(len(self.host_connections)):
            origin = 'env' if self.hosts.index(self.host_connections[i][0]) == (len(self.hosts)-1) else str(self.hosts.index(self.host_connections[i][0])+1)
            objective = 'env' if self.hosts.index(self.host_connections[i][1]) == (len(self.hosts)-1) else str(self.hosts.index(self.host_connections[i][1])+1)
            multiplier = str(self.hosts_connections[i][2]) + ', ' + str(self.host_connections[i][3]) if ((not (self.host_connections[i][2] == 1)) and (not (self.host_connections[i][3] == 1))) else str(self.host_connections[i][2]) if (not (self.host_connections[i][2] == 1)) else str(self.host_connections[i][3]) if (not (self.host_connections[i][3] == 1)) else ''
            if not (origin, objective) in hosts_conns:
                hosts_conns.add((origin, objective))
                hostconns_code += '  \hostconn[10]{' + multiplier + '}{above}{' + origin + '}{' + objective + '}%\n'
        for i in range(n_insts):
            insts_code += '  \instruction{' + str(i+1) + '}{' + str(2*(i%horizontal_insts)) + '}{' + str(-4-(2*math.floor(i/horizontal_insts))) + '}%\n'
            if self.instructions[i].host:
                # Here, the code needs the environment to be at the position -1 in the hosts list
                origin = 'env' if self.hosts.index(self.instructions[i].host) == (n_hosts-1) else str(self.hosts.index(self.instructions[i].host)+1)
                # objective = 'env' if self.hosts.index(self.instructions[i].objective_host) == (n_hosts-1) else str(self.hosts.index(self.instructions[i].objective_host)+1)
                # multiplier = '' if self.instructions[i].multiplier == 1 else str(self.instructions[i].multiplier)
                if verbose:
                    inst = 'i_{' + str(i+1) + '}'
                    orig = 'h_{' + origin + '}'
                    obj = '' # 'env' if objective == 'env' else 'h_{' + objective + '}'
                    legend_code += '  \legend{' + str(max_horizontal + 2) + '}{' + str(vertical_hosts*2-i) + '}{' + inst + '}{' + orig + '}{' + obj + '}%\n'
                insthost_code += '  \insthost[45]{i' + str(i+1) + '}{h' + origin + '}%\n'
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

