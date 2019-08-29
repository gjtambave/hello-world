import matplotlib.pyplot as plt
import numpy as np
np.random.seed(123)
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        clums = np.random.rand(0,1)
        if clums <= 0.001 :
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to Numpy array: np_aw
np_aw = np.array(all_walks)

# Plot np_aw and show
#plt.plot(np_aw)
#plt.show()
# Clear the figure
#plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)

# Plot np_aw_t and show
#plt.plot(np_aw_t)
#plt.show()
# Clear the figure
#plt.clf()

# Select last row from np_aw_t: ends
ends = np_aw_t[-1]
ends = np.array(ends)
# Plot histogram of ends, display plot
#plt.hist(ends, bins=10)
#plt.show()
#Final answer
#odds = ends[ends >= 60]
#print(len(odds)/500)
#print("odds of reaching 60 or more steps is " + str(len(odds)/500) + "%")



