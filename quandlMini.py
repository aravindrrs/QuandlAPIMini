API_KEY = 'h5MYw73-zd38CeS_AxqB'

# Frankfurt Stock Exchange
# Company 'Carl Zeiss Meditec' Ticker =' 'AFX_X'
# use Requests, collections and python inbuilt libraries, nothing else to be imported

# the above mentioned stock seems to be premium
# Basilea Pharmaceutica AG (PK5) Adjusted Stock Prices will be used here


import requests
import collections

myUrl = ' https://www.quandl.com/api/v3/datasets/XFRA/PK5/data.json?' + '&start_date=2017-01-01&end_date=2017-12-31' + '&api_key=' + API_KEY

myUrlRequests = requests.get(myUrl)
urlJson = myUrlRequests.json()
# print (urlJson)

# print (len(urlJson['dataset_data']['data']))
# print (type(urlJson['dataset_data']['data']))

# column names =['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adjustment Factor', 'Adjustment Type']
#
# #High
# print (urlJson['dataset_data']['column_names'][2])
# print (urlJson['dataset_data']['data'][49][2])
#
# #low
# print (urlJson['dataset_data']['column_names'][3])
# print ((urlJson['dataset_data']['data'][259][3]))
##print (len((urlJson['dataset_data']['data'][259][3])))#float obj has no length

# highest for the entire day
# highest = 0.0
# hCount=0
# for i in range (0,len(urlJson['dataset_data']['data'])):
#        hCount +=1
#        hValue = urlJson['dataset_data']['data'][i][2]
#        if hValue > highest:
#             highest = hValue

# print (hCount)
# print ("highest in the 2017:",highest)

# Lowest for the entire day
#
# lowest = urlJson['dataset_data']['data'][0][3]
# lCount= 0
# for i in range (0,len(urlJson['dataset_data']['data'])):
#        lCount +=1
#        lValue = urlJson['dataset_data']['data'][i][3]
#        if lValue < lowest:
#             lowest = lValue

# print (hCount)
# print ("lowest in 2017:",lowest)


# Q3
## Highest and lowest based on the open price
# open = urlJson['dataset_data']['column_names'][1] column
# open data = urlJson['dataset_data']['data'][i][1]

totalDays =len(urlJson['dataset_data']['data'])
openHighest = 0.0
openLowest = urlJson['dataset_data']['data'][0][1]
# count = 0

for i in range(0,totalDays ):
    # count+=1

    openPrice = urlJson['dataset_data']['data'][i][1]

    if openPrice >= openHighest:
        openHighest = openPrice

    if openPrice <= openLowest:
        openLowest = openPrice

# print (count)
print("Lowest:", openLowest)
print("Highest:", openHighest)

# Q4
# largest change based on the entire day
change = 0.0
# cCount = 0
for i in range(0, totalDays ):
    # cCount +=1
    high = urlJson['dataset_data']['data'][i][2]
    low = urlJson['dataset_data']['data'][i][3]
    diff = abs(high - low)
    if diff > change:
        change = diff

# print (cCount)
print("Highest change in a given day :{:.6f}".format(change))

# Q5
# Largest change between any two days based on closing price

# close =(urlJson['dataset_data']['column_names'][4])
# Close data = urlJson['dataset_data']['data'][i][4]

closeLowest = urlJson['dataset_data']['data'][0][4]
closeHighest = 0.0

for i in range(0,totalDays ):
    closePrice = urlJson['dataset_data']['data'][i][4]
    if closePrice >= closeHighest:
        closeHighest = closePrice

    if closePrice <= closeLowest:
        closeLowest = closePrice

largestCloseDiff = abs(closeHighest - closeLowest)
print(largestCloseDiff)

#Q6
# Average Volume in the year
#Volume =urlJson['dataset_data']['column_names'][5]
#Volume =urlJson['dataset_data']['data'][i][5]

vol= 0.0
for i in range (0, totalDays ):
    vol+= urlJson['dataset_data']['data'][i][5]

avgVolume = vol/totalDays

print ("Average volume traded for the year:" + str(avgVolume)+"K")


def medianvol(listSize):
    volumeList = []

    for i in range (0,listSize):
        volumeList.append(urlJson['dataset_data']['data'][i][5])
    sortedVol=sorted(volumeList)
    print(volumeList)
    print (sortedVol)

    if listSize %2 !=0 :

        return sortedVol[listSize//2]

    return (sortedVol[listSize//2] + sortedVol[(listSize//2)+1])/2

print( medianvol(totalDays))

