import ystockquote
import csv
import sys

Names = [];
Tickers = [];
with open('SP_Constituants.csv', 'rb') as csvfile:
    CSVReader = csv.reader(csvfile);
    for row in CSVReader:
        Names.append(row[1]);
        Tickers.append(row[2]);

Tickers.pop(0);

faillog = [];
for row in Tickers:
    try:
        title = 'Pulled Data/';
        title += row.replace(" ", "").replace("/","");
        title += '.csv';
        print title
        Historical=ystockquote.get_historical_prices(row.replace(" ", "").replace("/","."),"2012-07-07","2013-07-14")
        with open(title, 'w') as csvfile:
            CSVWriter = csv.writer(csvfile);
            for row2 in Historical:
                CSVWriter.writerow(row2);
    except:
        print "Fail on "+row;
        faillog.append(row);
        
