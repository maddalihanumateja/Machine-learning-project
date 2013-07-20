import csv
import sys
import os

combine_dir = 'E:\\GitHub\\maddalihanumateja\\Machine-learning-project.git\\CombineData\\'

## Set up for 4 days
data_4 = []
for filename in os.listdir(combine_dir):
    with open(combine_dir+filename,'rb') as csvfile:
        CSVReader = csv.reader(csvfile);
        r2write = [];
        CSVReader.next();
        for row in CSVReader:
            r2write.append(float(row[1])-1);
            r2write.append(float(row[2])-1);
            r2write.append(float(row[3])-1);
            r2write.append(float(row[4]));
        data_4.append(r2write);
with open('data_4_back_raw.csv','w') as csvfile:
    CSVWriter = csv.writer(csvfile);
    CSVWriter.writerow(['Close Change n','Low Change n','High Change n','Twitter n','Close Change n-1','Low Change n-1','High Change n-1','Twitter n-1','Close Change n-2','Low Change n-2','High Change n-2','Twitter n-2','Close Change n-3','Low Change n-3','High Change n-3','Twitter n-3','Close Change n-4','Low Change n-4','High Change n-4','Twitter n-4'])
    for row in data_4:
        CSVWriter.writerow(row);
with open('data_4_back_classes.csv','w') as csvfile:
    CSVWriter = csv.writer(csvfile);
    CSVWriter.writerow(['Class','Close Change n','Low Change n','High Change n','Twitter n','Close Change n-1','Low Change n-1','High Change n-1','Twitter n-1','Close Change n-2','Low Change n-2','High Change n-2','Twitter n-2','Close Change n-3','Low Change n-3','High Change n-3','Twitter n-3','Close Change n-4','Low Change n-4','High Change n-4','Twitter n-4'])
    for row in data_4:
        r2write = [];
        if (row[0] < -0.01):
            r2write.append('(-inf:-1.0%)')
        elif (row[0] < -0.007):
            r2write.append('[-1.0%:-0.7%)')
        elif (row[0] < -0.004):
            r2write.append('[-0.7%:-0.4%)')
        elif (row[0] < -0.001):
            r2write.append('[-0.4%:-0.1%)')
        elif (row[0] < 0.001):
            r2write.append('[-0.1%:0.1%)')
        elif (row[0] < 0.004):
            r2write.append('[0.1%:0.4%)')
        elif (row[0] < 0.007):
            r2write.append('[0.4%:0.7%)')
        elif (row[0] < 0.01):
            r2write.append('[0.7%:1.0%)')
        else:
            r2write.append('[1.0%:inf)')
        r2write = r2write+row;
        CSVWriter.writerow(r2write);
## Set up for 3 days

data_3 = []
for filename in os.listdir(combine_dir):
    with open(combine_dir+filename,'rb') as csvfile:
        CSVReader = csv.reader(csvfile);
        r2write = [];
        CSVReader.next();
        for row in CSVReader:
            r2write.append(float(row[1])-1);
            r2write.append(float(row[2])-1);
            r2write.append(float(row[3])-1);
            r2write.append(float(row[4]));
        data_3.append(r2write[0:-4]);
        data_3.append(r2write[4:]);
with open('data_3_back_raw.csv','w') as csvfile:
    CSVWriter = csv.writer(csvfile);
    CSVWriter.writerow(['Close Change n','Low Change n','High Change n','Twitter n','Close Change n-1','Low Change n-1','High Change n-1','Twitter n-1','Close Change n-2','Low Change n-2','High Change n-2','Twitter n-2','Close Change n-3','Low Change n-3','High Change n-3','Twitter n-3'])
    for row in data_3:
        CSVWriter.writerow(row);
with open('data_3_back_classes.csv','w') as csvfile:
    CSVWriter = csv.writer(csvfile);
    CSVWriter.writerow(['Class','Close Change n','Low Change n','High Change n','Twitter n','Close Change n-1','Low Change n-1','High Change n-1','Twitter n-1','Close Change n-2','Low Change n-2','High Change n-2','Twitter n-2','Close Change n-3','Low Change n-3','High Change n-3','Twitter n-3'])
    for row in data_3:
        r2write = [];
        if (row[0] < -0.01):
            r2write.append('(-inf:-1.0%)')
        elif (row[0] < -0.007):
            r2write.append('[-1.0%:-0.7%)')
        elif (row[0] < -0.004):
            r2write.append('[-0.7%:-0.4%)')
        elif (row[0] < -0.001):
            r2write.append('[-0.4%:-0.1%)')
        elif (row[0] < 0.001):
            r2write.append('[-0.1%:0.1%)')
        elif (row[0] < 0.004):
            r2write.append('[0.1%:0.4%)')
        elif (row[0] < 0.007):
            r2write.append('[0.4%:0.7%)')
        elif (row[0] < 0.01):
            r2write.append('[0.7%:1.0%)')
        else:
            r2write.append('[1.0%:inf)')
        r2write = r2write+row;
        CSVWriter.writerow(r2write);

## Set up for 2 days

data_2 = []
for filename in os.listdir(combine_dir):
    with open(combine_dir+filename,'rb') as csvfile:
        CSVReader = csv.reader(csvfile);
        r2write = [];
        CSVReader.next();
        for row in CSVReader:
            r2write.append(float(row[1])-1);
            r2write.append(float(row[2])-1);
            r2write.append(float(row[3])-1);
            r2write.append(float(row[4]));
        data_2.append(r2write[0:-8]);
        data_2.append(r2write[4:-4]);
        data_2.append(r2write[8:]);
with open('data_2_back_raw.csv','w') as csvfile:
    CSVWriter = csv.writer(csvfile);
    CSVWriter.writerow(['Close Change n','Low Change n','High Change n','Twitter n','Close Change n-1','Low Change n-1','High Change n-1','Twitter n-1','Close Change n-2','Low Change n-2','High Change n-2','Twitter n-2'])
    for row in data_2:
        CSVWriter.writerow(row);
with open('data_2_back_classes.csv','w') as csvfile:
    CSVWriter = csv.writer(csvfile);
    CSVWriter.writerow(['Class','Close Change n','Low Change n','High Change n','Twitter n','Close Change n-1','Low Change n-1','High Change n-1','Twitter n-1','Close Change n-2','Low Change n-2','High Change n-2','Twitter n-2'])
    for row in data_2:
        r2write = [];
        if (row[0] < -0.01):
            r2write.append('(-inf:-1.0%)')
        elif (row[0] < -0.007):
            r2write.append('[-1.0%:-0.7%)')
        elif (row[0] < -0.004):
            r2write.append('[-0.7%:-0.4%)')
        elif (row[0] < -0.001):
            r2write.append('[-0.4%:-0.1%)')
        elif (row[0] < 0.001):
            r2write.append('[-0.1%:0.1%)')
        elif (row[0] < 0.004):
            r2write.append('[0.1%:0.4%)')
        elif (row[0] < 0.007):
            r2write.append('[0.4%:0.7%)')
        elif (row[0] < 0.01):
            r2write.append('[0.7%:1.0%)')
        else:
            r2write.append('[1.0%:inf)')
        r2write = r2write+row;
        CSVWriter.writerow(r2write);

## Set up for 1 days

data_1 = []
for filename in os.listdir(combine_dir):
    with open(combine_dir+filename,'rb') as csvfile:
        CSVReader = csv.reader(csvfile);
        r2write = [];
        CSVReader.next();
        for row in CSVReader:
            r2write.append(float(row[1])-1);
            r2write.append(float(row[2])-1);
            r2write.append(float(row[3])-1);
            r2write.append(float(row[4]));
        data_1.append(r2write[0:-12]);
        data_1.append(r2write[4:-8]);
        data_1.append(r2write[8:-4]);
        data_1.append(r2write[12:]);
with open('data_1_back_raw.csv','w') as csvfile:
    CSVWriter = csv.writer(csvfile);
    CSVWriter.writerow(['Close Change n','Low Change n','High Change n','Twitter n','Close Change n-1','Low Change n-1','High Change n-1','Twitter n-1'])
    for row in data_1:
        CSVWriter.writerow(row);
with open('data_1_back_classes.csv','w') as csvfile:
    CSVWriter = csv.writer(csvfile);
    CSVWriter.writerow(['Class','Close Change n','Low Change n','High Change n','Twitter n','Close Change n-1','Low Change n-1','High Change n-1','Twitter n-1'])
    for row in data_1:
        r2write = [];
        if (row[0] < -0.01):
            r2write.append('(-inf:-1.0%)')
        elif (row[0] < -0.007):
            r2write.append('[-1.0%:-0.7%)')
        elif (row[0] < -0.004):
            r2write.append('[-0.7%:-0.4%)')
        elif (row[0] < -0.001):
            r2write.append('[-0.4%:-0.1%)')
        elif (row[0] < 0.001):
            r2write.append('[-0.1%:0.1%)')
        elif (row[0] < 0.004):
            r2write.append('[0.1%:0.4%)')
        elif (row[0] < 0.007):
            r2write.append('[0.4%:0.7%)')
        elif (row[0] < 0.01):
            r2write.append('[0.7%:1.0%)')
        else:
            r2write.append('[1.0%:inf)')
        r2write = r2write+row;
        CSVWriter.writerow(r2write);
