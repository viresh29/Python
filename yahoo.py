from urllib import request

googUrl = 'www.google.com'
def downloadStockData(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csvStr = str(csv)
    lines = csvStr.split("\\n")
    destUrl = r'goog.csv'
    fx = open(destUrl,"w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()


downloadStockData(googUrl)
