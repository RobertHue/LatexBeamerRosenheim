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
y = np.array([951, 747, 651, 613])
plt.plot(x, y, color='b', linestyle='-', marker='x', label='LRU')

######## ARC ########
v = np.array([0.5, 1.0, 2.0, 3.0])
w = np.array([1166, 783, 668, 623])
plt.plot(v, w, color='g', linestyle='-', marker='.', label='ARC')
plt.legend()

##################### LEGEND
legend = plt.legend(loc='best', fancybox=True, shadow=False, ncol=1, fontsize=12)
legend.get_frame().set_alpha(0.5)

##################### LABELS
plt.xlabel(u'Cache-Kapazität [kB]', fontsize=fontsize)
plt.ylabel('Loaded Bytes [MB]', fontsize=fontsize)
#plt.title('Vergleich der Kosten zum Laden (Dichte-Limitierung)', fontsize=fontsize+2)
plt.grid(True)

### AXIS:
plt.axis([0.25, 3.25, 590, 1700])

##################### SAVE & SHOW
plt.tight_layout() # to avoid parts of title being cut off
plt.savefig("DensityLimitationSwapLoadCosts.png")
plt.show()