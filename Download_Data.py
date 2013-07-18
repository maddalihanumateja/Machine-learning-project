import ystockquote
import csv
import sys

Names = [];
Tickers = [];
with open('Top_8.csv', 'rb') as csvfile:
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
        Historical=ystockquote.get_historical_prices(row.replace(" ", "").replace("/","."),"2013-07-13","2013-07-18")
        with open(title, 'w') as csvfile:
            CSVWriter = csv.writer(csvfile);
            Historical.pop(0)
            CSVWriter.writerow(["Close Ratio","High Ratio","Low Ratio"]);
            for row2 in Historical:
                r2write = [];
                r2write.append(float(row2[4])/float(row2[1]));
                r2write.append(float(row2[3])/float(row2[1]));
                r2write.append(float(row2[2])/float(row2[1]));
                CSVWriter.writerow(r2write);
    except:
        print "Fail on ",row," with error:", sys.exc_info()[0];
        faillog.append(row);
        break;
        
