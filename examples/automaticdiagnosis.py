from host import Host
from cpinstruction import CPInstruction
from cpvirusmachine import CPVirusMachine

def calculate_variables(clauses):
    m = 0
    for clause in clauses:
        for literal in clause:
            if literal[0] > m:
                m = literal[0]
    return m

def initialize_variable(haux):
    hxit = Host()
    hxin = Host()
    hxia = Host()

    ixi1 = CPInstruction([hxit],[hxin],[1])
    ixi2 = CPInstruction([hxin],[hxit],[1])
    ixi3 = CPInstruction([haux],[hxin],[2])
    ixi4 = CPInstruction([hxin],[haux],[1])

    ic12 = (ixi1, ixi2, 2)
    ic13 = (ixi1, ixi3, 1)
    ic34 = (ixi3, ixi4, 1)

    return ([hxit, hxin, hxia], [ixi1, ixi2, ixi3, ixi4], [ic12, ic13, ic34])

def initialize_dnf_clause(variables, clause):
    instructions = []
    variables_hosts = []
    aux_hosts = []
    length_clause = len(clause)
    for literal in clause:
        variables_hosts.append(variables[literal[0]-1][0][1-literal[1]])
        aux_hosts.append(variables[literal[0]-1][0][2])
    icj1 = CPInstruction(variables_hosts, aux_hosts, [1]*length_clause)
    icj2 = CPInstruction(aux_hosts, variables_hosts, [1]*length_clause)
    icj3 = CPInstruction(aux_hosts, variables_hosts, [1]*length_clause)

    ic12 = (icj1, icj2, 2)
    ic13 = (icj1, icj3, 1)

    return ([icj1, icj2, icj3], [ic12, ic13])

def initialize_output(haux):
    hout = Host()

    iout1 = CPInstruction([haux],[hout],[1])
    iout0 = CPInstruction(None, None, None)

    return (hout, iout1, iout0)

def initialize_extras(haux, variables, clauses, output):
    instructions = []
    instruction_connections = []
    n = len(variables)
    p = len(clauses)
    for i in range(1, n):
        instruction_connections.extend([
            (variables[i-1][1][1], variables[i][1][0], 1),
            (variables[i-1][1][3], variables[i][1][0], 1)])  
    instruction_connections.extend([
        (variables[len(variables)-1][1][1], clauses[0][0][0], 1),
        (variables[len(variables)-1][1][3], clauses[0][0][0], 1)])
    for j in range(1, p):
        instruction_connections.extend([
            (clauses[j-1][0][2], clauses[j][0][0], 1),
            (clauses[j-1][0][1], output[1], 1)
        ])
    instruction_connections.append(
        (clauses[len(clauses)-1][0][2], output[2], 1)
        )
    return instruction_connections

def finalize_virus_machine(haux, variables, clauses, output, extras):
    hosts = []
    instructions = []
    instruction_connections = []
    for i in range(len(variables)):
        hosts.append(variables[i][0][0])
        hosts.append(variables[i][0][2])
        hosts.append(variables[i][0][1])
        instructions.extend(variables[i][1])
        instruction_connections.extend(variables[i][2])
    for j in range(len(clauses)):
        instructions.extend(clauses[j][0])
        instruction_connections.extend(clauses[j][1])
    hosts.extend([haux, output[0]])
    instructions.extend(output[1:3])
    instruction_connections.extend(extras)
    return hosts, instructions, instruction_connections
        
def build_virus_machine(formula_clauses):
    n = calculate_variables(formula_clauses)
    variables = []
    clauses = []
    output = []
    extras = []
    haux = Host(1)
    for i in range(1, n+1):
        variables.append(initialize_variable(haux))
    for c in formula_clauses:
        clauses.append(initialize_dnf_clause(variables, c))
    output = initialize_output(haux)
    extras = initialize_extras(haux, variables, clauses, output)

    hosts, instructions, instruction_connections = finalize_virus_machine(haux, variables, clauses, output, extras)
    vm = CPVirusMachine(hosts, instructions, instruction_connections, semantics = "AND")
    return vm

def inject_truth_value(vm, truth):
    for i in range(len(truth)):
        vm.hosts[i*3].viruses = truth[i]
    return vm
