import os
import sys

import getdist
import matplotlib.pyplot as plt
from getdist import plots

# get chain root
if len(sys.argv) < 2:
    sys.exit(1)

chain_root = "./chains/" + sys.argv[1]

# directory and base name
chain_dir = os.path.dirname(chain_root)
chain_base = os.path.basename(chain_root)

# outputs directory
outputs_dir = os.path.join(chain_dir, "outputs")
os.makedirs(outputs_dir, exist_ok=True)

# load MCMC chains
samples = getdist.loadMCSamples(chain_root, settings={"ignore_rows": 0.3})

# act_tau
params = ["H0", "w", "wa", "beta_DE"]

print("R-1 =", samples.getGelmanRubin())

param_latex = {param: samples.getInlineLatex(param, 1) for param in params}
for param in params:
    print(param_latex[param])

# triangle plot
g = getdist.plots.get_subplot_plotter(width_inch=8)
g.triangle_plot(samples, params, filled=True)
fig_path = os.path.join(outputs_dir, chain_base + "_triangle.png")
plt.savefig(fig_path, dpi=300)
print(f"triangle plot saved at {fig_path}")

# Write marginalized parameters with uncertainties to a file
params_path = os.path.join(outputs_dir, chain_base + "_parameters.txt")
with open(params_path, "w") as f:
    f.write("R-1 = {:.5f}\n".format(samples.getGelmanRubin()))
    f.write("\nMarginalized parameters with uncertainties:\n")
    for param in params:
        f.write("{} = {}\n".format(param, param_latex[param]))
print(f"parameters saved at {params_path}")
