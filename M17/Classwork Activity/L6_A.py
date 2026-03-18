import numpy as np

np.random.seed(42)
#1 represents the puppies with blue eyes, and 0 represents the puppies with hazel eyes
puppies = np.array([1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1])

p = puppies.mean()
print("Mean: ", p)
print("Standard Deviation: ", puppies.std())
#standard deviation is square root of variance
print("Variance: ", puppies.var())
#variance tells us how spread out the data is from the mean
#it measures the average of the square difference from the mean

np.random.choice(puppies, size=(1,5), replace=True)
# a dataset of puppies 1 row and 5 columns will ensure that the data is permanently updated
np.random.choice(puppies, size=(1,5), replace=True).mean()
#mean or average of that 5 random selected data

print("Sampling Distribution with size 5")
sample_props = []
for i in range(10000): #we are repeating sampling for 10000 times
    sample = np.random.choice(puppies, 5, replace=True) #pick 5 random values
    sample_props.append(sample.mean()) #calculate the mean
sample_props = np.array(sample_props) #store all the mean for those 10k iteration into sample props

sm = sample_props.mean()
print("Mean: ", sample_props.mean())
print("Standard Deviation: ", sample_props.std())
print("Variance: ", sample_props.var())

print("Sampling Distribution with size 20")

twenty_sample_props = []
for i in range(10000):
    sample = np.random.choice(puppies, 20, replace=True)
    twenty_sample_props.append(sample.mean())
twenty_sample_props = np.array(twenty_sample_props)

print("New Mean: ", twenty_sample_props.mean())
print("New Standard Deviation: ", twenty_sample_props.std())
print("New Variance: ", twenty_sample_props.var())