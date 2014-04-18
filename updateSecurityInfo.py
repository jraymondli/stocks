#runs the daily update based on newly fetched daily security information
import sys, traceback

def updateDataForSecurity(infoItems):
    ticker = infoItems[0]
    date = infoItems[1]
    price = infoItems[2]
    volume = infoItems[3]
    range = infoItems[5]
    ticker = ticker[1:-1]
    securityFileName = "./security_data/" + ticker
    securityFileHandle = open(securityFileName, "a+");    
    print >> securityFileHandle, date, price, volume, range 


def main():
    dailySecurityInfoFile = open('./dailySecurityInfo.txt', 'r');
    lastUpdateDateNotChecked = "true"

    for line in dailySecurityInfoFile:
        line2 = line.rstrip()
        infoItems = line2.split(',')
        #print infoItems
        if (lastUpdateDateNotChecked == "true"):
            lastUpdateDateNotChecked = "false"
            print "not checked"
            lastUpdateDate = open("security_data/lastUpdateDate.txt", 'r').read()
            lastUpdateDate = lastUpdateDate.rstrip()
            if (lastUpdateDate != infoItems[1]):
                print >> open("security_data/lastUpdateDate.txt", 'w'), infoItems[1] 
            else: 
                print "already updated"
                sys.exit(0)
        updateDataForSecurity(infoItems)

if __name__ == "__main__":
    main()
 
