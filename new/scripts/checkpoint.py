import os
import sys

import getdist
import matplotlib.pyplot as plt
from getdist import plots

# get chain root
chain_dir = "../chains"
chain_base = sys.argv[1]
chain_root = os.path.join(chain_dir, chain_base)

# outputs directory
outputs_dir = os.path.join(chain_dir, "outputs")
os.makedirs(outputs_dir, exist_ok=True)

# load MCMC chains
samples = getdist.loadMCSamples(chain_root, settings={"ignore_rows": 0.3})

# select parameters to be displayed
params = ["w", "wa", "beta_DE"]

# print Gelman-Rubin statistic
Rminus1 = samples.getGelmanRubin()
print("R-1 =", Rminus1)

# print marginalized parameters with uncertainties
param_latex = {param: samples.getInlineLatex(param, 1) for param in params}
for param in params:
    print(param_latex[param])

# triangle plot
g = getdist.plots.get_subplot_plotter(width_inch=8)
g.triangle_plot(samples, params, filled=True)
fig_path = os.path.join(outputs_dir, chain_base + "_triangle.png")
plt.savefig(fig_path, dpi=300)
print(f"triangle plot saved at {fig_path}")

# write marginalized parameters with uncertainties to a file
params_path = os.path.join(outputs_dir, chain_base + "_parameters.txt")
with open(params_path, "w") as f:
    f.write("R-1 = {:.5f}\n".format(Rminus1))
    f.write("\nMarginalized parameters with uncertainties:\n")
    for param in params:
        f.write("{} = {}\n".format(param, param_latex[param]))

# checking convergence
if Rminus1 < 0.01:
    sys.exit(0)
    # exit code 0 if converged below the threshold
else:
    sys.exit(1)
