import time
import math
from lpd import lpd
from viruslatex import viruslatex
from formalverification import validate

n = 5*13
vm = lpd(n)
vm.compute(verbose=2)
