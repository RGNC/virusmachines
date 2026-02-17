import time
import math
from channelparallel import channelparallel

n = 1
vm = channelparallel(n, semantics = "OR")
vm.compute(verbose = 1)


vm = channelparallel(n, semantics = "AND")
vm.compute(verbose = 1)
