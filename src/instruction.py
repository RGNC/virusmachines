
class Instruction(object):

    def __init__(self, origin_host, objective_host, multiplier = 1):
        self.origin_host = origin_host
        self.objective_host = objective_host
        self.multiplier = multiplier
