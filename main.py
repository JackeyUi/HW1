# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
import numpy as np
import timeit
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '108061102.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))
def get_P(item):
   return float(item['PRES'])

# target_data = [('test', 0)]
data = np.array(data)
sum1 = sum2 = sum3 = sum4 = sum5 = 0
cnt1 = cnt2 = cnt3 = cnt4 = cnt5 =0

step1 = list(filter(lambda item: (item['PRES'] != '-99.000' and item['PRES'] != '-999.000'), data))
step2_1 = list(filter(lambda item: item['station_id'] == 'C0A880', step1))
for i in range(len(step2_1)) :
   sum1 += get_P(step2_1[i])
   cnt1 += 1   
mean1 = sum1/cnt1

test2 = [] 
step2_2 = list(filter(lambda item: item['station_id'] == 'C0F9A0', step1))
for i in range(len(step2_2)) :
   sum2 += get_P(step2_2[i])
   cnt2 += 1
   test2.append(get_P(step2_2[i]))
mean2 = sum2/cnt2


test3 = [] 
step2_3 = list(filter(lambda item: item['station_id'] == 'C0G640', step1))
for i in range(len(step2_3)) :
   sum3 += get_P(step2_3[i])
   cnt3 += 1
   test3.append(get_P(step2_3[i]))
mean3 = sum3/cnt3

test4 = [] 
step2_4 = list(filter(lambda item: item['station_id'] == 'C0R190', step1))
for i in range(len(step2_4)) :
   sum4 += get_P(step2_4[i])
   cnt4 += 1
   test4.append(get_P(step2_4[i]))
mean4 = sum4/cnt4

test5 = [] 
step2_5 = list(filter(lambda item: item['station_id'] == 'C0X260', step1))
for i in range(len(step2_5)) :
   sum5 += get_P(step2_5[i])
   cnt5 += 1
   test5.append(get_P(step2_5[i]))
mean5 = sum5/cnt5

mean1 = round(mean1, 2)
mean2 = round(mean2, 2)
mean3 = round(mean3, 2)
mean4 = round(mean4, 2)
mean5 = round(mean5, 2)


target_data = [('C0A880', mean1), ('C0F9A0', mean2), ('C0G640', mean3), ('C0R190', mean4), ('C0X260', mean5)]




#arr1 = list(filter(lambda item: (item['PRES']), step2)
# Retrive ten data points from the beginning.
#target_data = step2[:1]

#=======================================

# Part. 4
#=======================================
# Print result
print(target_data[:])
# print(test2[:])
#========================================