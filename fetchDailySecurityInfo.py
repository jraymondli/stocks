import urllib2

securityList = open('securityList.txt', 'r')
dailySecurityInfoFile = open('./dailySecurityInfo.txt', 'w+');

index = 0
for line in securityList:
    index = index + 1
    ticker = line.rstrip()
    if ticker != '':
        url = "http://finance.yahoo.com/d/quotes.csv?s=" + ticker + "&f=sd1l1vc1mn"
        response = urllib2.urlopen(url)
        info = response.read()
        infoItems = info.split(",")
        infoContent = info.rstrip()
        print >> dailySecurityInfoFile, infoContent

