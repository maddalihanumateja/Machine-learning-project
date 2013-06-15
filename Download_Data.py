import ystockquote
import csv

Names = [];
Tickers = [];
with open('SP_Constituants.csv', 'rb') as csvfile:
    CSVReader = csv.reader(csvfile);
    for row in CSVReader:
        Names.append(row[1]);
        Tickers.append(row[2]);

