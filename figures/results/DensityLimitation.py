# -*- coding: utf-8 -*-
from matplotlib import rcParams
import matplotlib.pyplot as plt
import numpy as np
#########################################
### DEFS:
ax = plt.gca()
fontsize=18

##################### TITLE & LABEL-PADDING
plt.xlabel("...", labelpad=20)
plt.ylabel("...", labelpad=20)
ttl = ax.title
ttl.set_position([.5, 1.1])

######## LRU ########
x = np.array([0.5, 1.0, 2.0, 3.0])
y = np.array([99.4195, 99.4962, 99.543, 99.562])
plt.plot(x, y, color='b', linestyle='-', marker='x', label='LRU')

######## ARC ########
v = np.array([0.5, 1.0, 2.0, 3.0])
w = np.array([99.3669, 99.4836, 99.5371, 99.5578])
plt.plot(v, w, color='g', linestyle='-', marker='.', label='ARC')
plt.legend()

##################### LEGEND
legend = plt.legend(loc='lower right', fancybox=True, shadow=False, ncol=1, fontsize=12)
legend.get_frame().set_alpha(0.5)

##################### LABELS
plt.xlabel(u'Cache-Kapazität [kB]', fontsize=fontsize)
plt.ylabel('Hit-Rate [%]', fontsize=fontsize)
# plt.title('Vergleich von Hit-Rate (Dichte-Limitierung)', fontsize=fontsize+2)
plt.grid(True)

### AXIS:
plt.axis([0.25, 3.25, 99.35, 99.6])

##################### SAVE & SHOW
plt.tight_layout() # to avoid parts of title being cut off
plt.savefig("DensityLimitationHitRates.png")
plt.show()