import time
import math
from automaticdiagnosis import build_virus_machine, inject_truth_value

input_formula = [((1, 1), (2, 1)), ((3, 1), (2, 1))]
truth_value = [0, 1, 0]

vm = build_virus_machine(input_formula)
inject_truth_value(vm, truth_value)
vm.compute(verbose = 2)
