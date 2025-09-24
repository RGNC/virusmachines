
class Instruction(object):

    def __init__(self, origin_host, objective_host, multiplier = 1, name=None):
        self.origin_host = origin_host
        self.objective_host = objective_host
        self.multiplier = multiplier
        self.name = name

    def __str__(self) -> str:
        if self.name:
            return self.name
        else:
            return 'Unnamed instruction'
        
    def __repr__(self):
        return str(self)
