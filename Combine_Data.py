import csv
import sys
import os

twitter_dir = 'E:\\GitHub\\maddalihanumateja\\Machine-learning-project.git\\TwitterData\\'
ystock_dir = 'E:\\GitHub\\maddalihanumateja\\Machine-learning-project.git\\Pulled Data\\'
output_dir = 'E:\\GitHub\\maddalihanumateja\\Machine-learning-project.git\\CombineData\\'

for filename in os.listdir(ystock_dir):
    print 'Combining: ' + filename
    twitter = [];
    with open(twitter_dir+filename, 'rb') as csvfile:
        CSVReader = csv.reader(csvfile);
        for row in CSVReader:
            twitter.append(row);
    stock = [];
    with open(ystock_dir+filename, 'rb') as csvfile:
        CSVReader = csv.reader(csvfile);
        for row in CSVReader:
            stock.append(row);
    with open(output_dir+filename,'w') as csvfile:
        CSVWriter = csv.writer(csvfile);
        stock[0].append('Twitter')
        CSVWriter.writerow(stock[0])
        for row in stock[1:]:
            tweet = [x for x in twitter if row[0] in x[0]]
            row.append(tweet[0][1])
            CSVWriter.writerow(row);
        
