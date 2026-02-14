inputFilePath = "transactions.txt"
outFilePath = "output.txt"

fromIDList = []
toIDList = []
amountList = []
criminalList = []
criminalInfos = {}

inputFile = open(inputFilePath, "r")
lines = inputFile.readlines()

for line in lines:
    transactionParts = line.split("|")
    fromID = transactionParts[0].split(":")[1]
    toID = transactionParts[1].split(":")[1]
    amount = transactionParts[2].split(":")[1].strip()
    
    fromIDList.append(fromID)
    toIDList.append(toID)
    amountList.append(amount)
inputFile.close()

for i in range(100):
    memberFile = open(f"members/member_ID{str(i)}.txt")
    name = memberFile.readline().strip()
    criminalList.append(name)
    memberFile.close()

for name in criminalList:
    criminalInfos[name] = {}
    for name2 in criminalList:
        criminalInfos[name][name2] = []

for i in range(len(fromIDList)):
    fromID = int(fromIDList[i])
    toID = int(toIDList[i])
    amount = int(amountList[i])
    
    criminalFromName = criminalList[fromID]
    criminalToName = criminalList[toID]
    criminalInfos[criminalFromName][criminalToName].append(amount)
criminalList.sort()

infoChart = "SUSPECT\t"
for name in criminalList:
    infoChart+= name + "\t"
infoChart = infoChart.strip() +"\n"
for i in range(100):
    key1 = criminalList[i]
    infoChart+= key1 + "\t"
    
    for j  in range(100):
        criminalName = criminalList[j]
        
        sum = 0
        for num in criminalInfos[key1][criminalName]:
            sum+=num          
        if len(criminalInfos[key1][criminalName]) > 0: 
            avg = sum/len(criminalInfos[key1][criminalName])
        else:
            avg = sum
        infoChart+= f"{avg:.2f}\t"
    infoChart = infoChart.strip() + "\n"
    
infoChart = infoChart.strip()

outFile = open(outFilePath,"w")
outFile.writelines(infoChart)
outFile.close()