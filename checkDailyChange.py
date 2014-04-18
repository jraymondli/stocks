#
import sys, traceback



def main():
    print sys.argv
    min_change = 0.02
    if (len(sys.argv) > 1):
        min_change = float(sys.argv[1])
    print "min_change", min_change

    column = -1 
    if (len(sys.argv) > 2):
        column = int(sys.argv[2])
    print "column", column 
 
    dailySecurityInfoFile = open('./dailySecurityInfo.txt', 'r');

    for line in dailySecurityInfoFile:
        line2 = line.rstrip()
        infoItems = line2.split(',')
        ticker = infoItems[0]
        price = float(infoItems[2])
        change = float(infoItems[4])
        #print ticker, price, change
        if (abs(change/price) > min_change):
            if column == 1:
                print ticker
            elif column == 2:
                print change/price *100, "%"
            else:
                print ticker, change/price *100, "%"

if __name__ == "__main__":
    main()
 
