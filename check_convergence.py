import sys

import getdist

if len(sys.argv) < 2:
    sys.exit(1)

chain_root = "./chains/" + sys.argv[1]

samples = getdist.loadMCSamples(chain_root, settings={"ignore_rows": 0.3})
Rminus1 = samples.getGelmanRubin()

if Rminus1 < 0.1:
    sys.exit(0)
    # exit code 0 if converged below the threshold
else:
    sys.exit(1)
