import pandas as pd 
import statistics
import csv

df = pd.read_csv("StudentsPerformance.csv")
readingList = df["reading score"].to_list()
writingList = df["writing score"].to_list()

#Mean 
readingMean = statistics.mean(readingList)
writingMean = statistics.mean(writingList)

#median
readingMedian = statistics.median(readingList)
writingMedian = statistics.median(writingList)

#Mode
readingMode = statistics.mode(readingList)
writingMode = statistics.mode(writingList)

#standard deviation
rd_std_dev = statistics.stdev(readingList)
wr_std_dev = statistics.stdev(writingList)

# print ("Mean , Median and Mode of reading is {} , {} and {}".format(readingMean,readingMedian,readingMode))
# print ("Mean , Median and Mode of writing is {} , {} and {}".format(writingMean,writingMedian,writingMode))

# first 

rd_first_std_dev_start , rd_first_std_dev_end = readingMean - rd_std_dev , readingMean + rd_std_dev
wr_first_std_dev_start , wr_first_std_dev_end = writingMean - wr_std_dev , writingMean + wr_std_dev

rd_list_of_data_within_1_std_dev = [result for result in readingList if result > rd_first_std_dev_start and result < rd_first_std_dev_end]
wr_list_of_data_within_1_std_dev = [result for result in writingList if result > wr_first_std_dev_start and result < wr_first_std_dev_end]

print("{} % of data for reading lies within 1 standard deviation".format(len(rd_list_of_data_within_1_std_dev) * 100 / len(readingList)))
print("{} % of data for writing lies within 1 standard deviation".format(len(wr_list_of_data_within_1_std_dev) * 100 / len(writingList)))

# second

rd_second_std_dev_start , rd_second_std_dev_end = readingMean - rd_std_dev , readingMean + rd_std_dev
wr_second_std_dev_start , wr_second_std_dev_end = writingMean - wr_std_dev , writingMean + wr_std_dev

rd_list_of_data_within_2_std_dev = [result for result in readingList if result > rd_second_std_dev_start and result < rd_second_std_dev_end]
wr_list_of_data_within_2_std_dev = [result for result in writingList if result > wr_second_std_dev_start and result < wr_second_std_dev_end]

print("{} % of data for reading lies within 2 standard deviation".format(len(rd_list_of_data_within_2_std_dev) * 100 / len(readingList)))
print("{} % of data for writing lies within 2 standard deviation".format(len(wr_list_of_data_within_2_std_dev) * 100 / len(writingList)))
# third

rd_third__dev_start , rd_third__dev_end = readingMean - rd_std_dev , readingMean + rd_std_dev
wr_third__dev_start , wr_third__dev_end = writingMean - wr_std_dev , writingMean + wr_std_dev

rd_list_of_data_within_3_std_dev = [result for result in readingList if result > rd_third__dev_start and result < rd_third__dev_end]
wr_list_of_data_within_3_std_dev = [result for result in writingList if result > wr_third__dev_start and result < wr_third__dev_end]

print("{} % of data for reading lies within 3 standard deviation".format(len(rd_list_of_data_within_3_std_dev) * 100 / len(readingList)))
print("{} % of data for writing lies within 3 standard deviation".format(len(wr_list_of_data_within_3_std_dev) * 100 / len(writingList)))