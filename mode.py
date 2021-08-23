import csv
from collections import Counter
with open("data.csv",newline = '') as f:
    reader = csv.reader(f)
    dataList = list(reader)

dataList.pop(0)
newData = []

for i in range(len(dataList)):
    num = dataList[i][1]
    newData.append(float(num))

#calculating mode
data = Counter(newData)
modeRange = {
    "50-60": 0,
    "60-70": 0,
    "70-80": 0
}
for height,occurence in data.items():
    if 50<float(height)<60:
        modeRange["50-60"]+=occurence
    elif 60<float(height)<70:
        modeRange["60-70"]+=occurence
    elif 70<float(height)<80:
        modeRange["70-80"]+=occurence

mode_range, mode_occurence = 0,0

for range,occurence in modeRange.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]),int(range.split("-")[1])], occurence
mode = float((mode_range[0]+mode_range[1])/2)

print("Mode is: " + str(mode))