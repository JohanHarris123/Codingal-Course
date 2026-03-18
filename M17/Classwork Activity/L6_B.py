#simulate center limit theorem by generating of size 1, 10, and 100 respectively
#and plotting histograms for same


#generate random samples between 1 10 50 100
#calculate their mean
#plotting the histogram to see the distribution changes

import numpy #to create numpy arrays
import matplotlib.pyplot as plt #mathematical plotting just to plot graphs
num = [1, 10, 50, 100] #this is the range or the containers
means = [] #mean is the empty list that will contain the means
for j in num: #we are picking each number like 1 then 10 then 50 and finally 100 one by one in just
    numpy.random.seed(1) #seed ensures consistency in the randomness
    x = [numpy.mean(
        numpy.random.randint(
            -40, 40, j #-40 - 40 is the range to generate numbers
        )
    ) for _i in range(1000)] # 1000 sample means
    means.append(x)
k=0

fig, ax = plt.subplots(2,2, figsize=(6,6))
for i in range(0,2):
    for j in range(0, 2):
        ax[i,j].hist(means[k], 10, density = True)
        ax[i,j].set_title(label = num[k])
        k=k+1
plt.show()