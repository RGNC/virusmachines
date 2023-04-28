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
