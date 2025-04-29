import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# coord locations of extraction radii
R0 = 80

# Total ADM mass
M = 1.0
# The mode, as text
mode = "20"
# output data from running merger
data = np.loadtxt('~/Examples/BinaryBH/data/Weyl4_mode_20.dat')

# create figure and primary axis
fig, ax1 = plt.subplots(figsize=(10, 6))

# calculate retarded time
r0 = R0 + M * np.log(R0 / (2.0 * M) - 1.0)
timedata0 = (data[:, 0] - r0) / M

# extract real and imaginary parts
fluxdata0_re = data[:, 1]
fluxdata0_im = data[:, 2]

# --- time sequence ---
if not np.all(np.diff(timedata0) > 0):
    unique_indices = np.unique(timedata0, return_index=True)[1]
    timedata0 = timedata0[unique_indices]
    fluxdata0_re = fluxdata0_re[unique_indices]
    fluxdata0_im = fluxdata0_im[unique_indices]

# --- interpolate ---
time_smooth = np.linspace(timedata0.min(), timedata0.max(), 1000)

cs_re = CubicSpline(timedata0, fluxdata0_re)
cs_im = CubicSpline(timedata0, fluxdata0_im)

flux_re_smooth = cs_re(time_smooth)
flux_im_smooth = cs_im(time_smooth)

#--- plot ---
color_re = 'tab:blue'
ax1.set_xlabel(r"time $t/M$", fontsize=12)
ax1.set_ylabel(r"Re($\Psi_4$)", color=color_re, fontsize=12)
ax1.plot(time_smooth, flux_re_smooth, color=color_re, lw=1.5, label=r"Re($\Psi_4$)")
ax1.tick_params(axis='y', labelcolor=color_re)

ax2 = ax1.twinx()
color_im = 'tab:orange'
ax2.set_ylabel(r"Im($\Psi_4$)", color=color_im, fontsize=12)
ax2.plot(time_smooth, flux_im_smooth, color=color_im, lw=1.5, label=r"Im($\Psi_4$)")
ax2.tick_params(axis='y', labelcolor=color_im)

plt.title(r"$\Psi_4$ for $(\ell, m) = $" + mode, fontsize=14)
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2)
plt.tight_layout()
ax1.grid(True, linestyle='--', alpha=0.6)

#save
plt.savefig('~/weyl4_l2_m0.png', dpi=300, bbox_inches='tight')
