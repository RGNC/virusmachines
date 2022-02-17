
def validate(virusmachine, configuration, expression, variables, bucles={}, verbose=True):
    virusmachine.restart()
    ensure_properties(virusmachine, configuration)
    properties = properties_to_satisfy(configuration, expression, variables, bucles)
    properties = verify_properties(virusmachine, properties)
    is_true = all_true(properties)
    if verbose:
        print(is_true[1])
    else:
        return is_true
    
def ensure_properties(virusmachine, configuration):
    if not len(virusmachine.get_configuration()) == len(configuration):
        print("Configuration not compatible. Length of the vm configuration: " + str(len(virusmachine.get_configuration())) + ", length of the spected configuration: " + str(len(configuration)))
        exit(-1)

def satinize_configuration(configuration):
    if isinstance(configuration[-2], str) and (not configuration[-2] == "#"):
        configuration[-2] = int(configuration[-2][1:])
    return configuration

def satinize_bucles(bucles):
    for bucle in bucles:
        if list(bucles[bucle]):
            bucles[bucle] = list(bucles[bucle])
        else:
            bucles[bucle] = [0]
    return bucles

def properties_to_satisfy(configuration, expression, variables, bucles):
    variable_sets = []
    configuration = satinize_configuration(configuration)
    variable_sets.append(variables)
    bucles = satinize_bucles(bucles)
    for element in variable_sets:
        new_variable_sets = []
        for bucle in bucles:
            for index in bucles[bucle]:
                new_element = element.copy()
                new_element[bucle] = index
                new_variable_sets.append(new_element)
        if new_variable_sets:
            variable_sets = new_variable_sets
    properties = {}
    for variable_set in variable_sets:
        properties[eval(expression, variable_set)] = \
        [list(map(lambda x: special_eval(str(x), variable_set), configuration)), False]
    return properties

def special_eval(x, variable_set):
    if (x == "#") or (x == "*"):
        return x
    else:
        return eval(x, variable_set)

def verify_properties(virusmachine, properties):
    if virusmachine.current_step in properties:
        res = compare(properties[virusmachine.current_step][0], virusmachine.get_configuration())
        properties[virusmachine.current_step][1] = res
        if not res:
            properties[virusmachine.current_step].append(virusmachine.get_configuration())
    while virusmachine.current_step <= max(properties) and virusmachine.step() and virusmachine.current_instruction:
        if virusmachine.current_step in properties:
            res = compare(properties[virusmachine.current_step][0], virusmachine.get_configuration())
            properties[virusmachine.current_step][1] = res
            if not res:
                properties[virusmachine.current_step].append(virusmachine.get_configuration())
    if virusmachine.current_step in properties:
        res = compare(properties[virusmachine.current_step][0], virusmachine.get_configuration())
        properties[virusmachine.current_step][1] = res
        if not res:
            properties[virusmachine.current_step].append(virusmachine.get_configuration())
    return properties
    
def compare(properties, configuration):
    res = True
    for i in range(len(properties)):
        if not properties[i] == "*":
            if not properties[i] == configuration[i]:
                res = False
    return res

def all_true(properties):
    all_true = True
    res = ""
    for response in properties:
        if not properties[response][1]:
            all_true = False
            r = str(response)
            p0 = str(properties[response][0])
            p2 = str(properties[response][2]) if len(properties[response]) == 3 else str([])
            res += "Configuration " + r + " is not fulfilled.\n\tExpected:" + p0 + "\n\tObtained:" + p2 + "\n"
    if all_true:
        res = "All tests passed!"
    return (all_true, res)
