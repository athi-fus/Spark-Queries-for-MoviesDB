import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

# lists in seconds
local = [10, 4, 12, 18, 4, 19, 15, 25, 30, 19]
virtual1 = [22, 10, 25, 43, 13, 30, 28, 33, 47, 30]
virtual2 = [18, 11, 29, 39, 6, 43, 30, 40, 48, 29]
virtual3 = [24, 10, 31, 60, 6, 56, 35, 38, 60, 37]
livy = [114, 14, 114, 198, 14, 126, 186, 120, 204, 120]


# Python program to get average of a list
def average(lst):
    return sum(lst) / len(lst)


# calculating average
avg_local = average(local)
avg_virtual1 = average(virtual1)
avg_virtual2 = average(virtual2)
avg_virtual3 = average(virtual3)
avg_livy = average(livy)



#define sample data
#data = [12, 12, 13, 13, 15, 16, 17, 22, 23, 25, 26, 27, 28, 28, 29]
y = np.array([avg_local, avg_virtual1, avg_virtual2, avg_virtual3, avg_livy])
print("\n\n")
print(y)
print("\n\n")

#create 95% confidence interval for population mean weight
local_interval = st.t.interval(alpha=0.95, df=len(local)-1, loc=np.mean(local), scale=st.sem(local)) 
virtual1_interval = st.t.interval(alpha=0.95, df=len(virtual1)-1, loc=np.mean(virtual1), scale=st.sem(virtual1)) 
virtual2_interval = st.t.interval(alpha=0.95, df=len(virtual2)-1, loc=np.mean(virtual2), scale=st.sem(virtual2)) 
virtual3_interval =st.t.interval(alpha=0.95, df=len(virtual3)-1, loc=np.mean(virtual3), scale=st.sem(virtual3)) 
livy_interval = st.t.interval(alpha=0.95, df=len(livy)-1, loc=np.mean(livy), scale=st.sem(livy)) 

print(local_interval)
print(virtual1_interval)
print(virtual2_interval)
print(virtual3_interval)
print(livy_interval)

local_interval = np.asarray(local_interval)
virtual1_interval = np.asarray(virtual1_interval)
virtual2_interval = np.asarray(virtual2_interval)
virtual3_interval = np.asarray(virtual3_interval)
livy_interval = np.asarray(livy_interval)

intervals=[local_interval,virtual1_interval,virtual2_interval,virtual3_interval,livy_interval]
print(np.shape(intervals))
print(np.shape(np.transpose(intervals)))


intervals = np.transpose(intervals)
y = np.array([avg_local, avg_virtual1, avg_virtual2, avg_virtual3, avg_livy])

x = ['Local', 'Virtual1', 'Virtual2', 'Virtual3', 'Livy']

for item in y:
    print("y: {} \t type: {}".format(item, type(item)))

for it in intervals:
    print("item: {} \t type: {}".format(it, type(it)))

plt.errorbar(x, y, xerr = None, yerr = intervals, capsize = 5, ecolor = "red")
plt.plot(x, y) #marker='|',
plt.ylabel('Χρόνος Εκτέλεσης (s)')
plt.title('Μέσος Όρος Χρόνου Εκτέλεσης Ερωτήματος')
plt.show()


