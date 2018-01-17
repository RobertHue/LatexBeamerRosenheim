from matplotlib import rcParams
import matplotlib.pyplot as plt
import numpy as np
#########################################
### DEFS:
ax = plt.gca()
fontsize=12

##################### TITLE & LABEL-PADDING
plt.xlabel("...", labelpad=20)
plt.ylabel("...", labelpad=20)
ttl = ax.title
ttl.set_position([.5, 1.05])

######## LRU ########
x = np.array([0.5, 1.0, 2.0, 3.0])
y = np.array([99.9996, 99.9996, 99.9998, 99.9999])
plt.plot(x, y, color='b', linestyle='-', marker='x', label='LRU')

######## ARC ########
v = np.array([0.5, 1.0, 2.0, 3.0])
w = np.array([99.9995, 99.9996, 99.9998, 99.9999])
plt.plot(v, w, color='g', linestyle='-', marker='.', label='ARC')
plt.legend()

##################### LEGEND
legend = plt.legend(loc='lower right', fancybox=True, shadow=False, ncol=1, fontsize=12)
legend.get_frame().set_alpha(0.5)

##################### LABELS
plt.xlabel('Cache-Capacity c [kB]', fontsize=fontsize)
plt.ylabel('Hit-Rate [%]', fontsize=fontsize)
plt.title('Comparison of Caching-Strategies LRU and ARC (Feature-Estimation Bunny)', fontsize=fontsize+2)
plt.grid(True)

### AXIS:
plt.axis([0.25, 3.25, 99.999, 100])

##################### SAVE & SHOW
plt.tight_layout() # to avoid parts of title being cut off
plt.savefig("FeatureEstimation.png")
plt.show()