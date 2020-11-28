''
filename:filep41.py

Read datafile1.dat in text format, create a list, print the 
list to console and create a html table in output.html 
'''

fileIn = open('datafile1.dat', 'r')
fileOut = open('output.md','w')
data=[]

lines = fileIn.read().splitlines()

for line in lines:
    transactionRecord = line.split('_')
    data.append(transactionRecord)
    
print('%-20s%-30s%5s%10s'%('Name','Address','Txn', 'Ampunt'))
print('='*65)

for e in data:
    print('%-20s%-30s%5s%10s'%(e[0], e[1], e[2], e[3]))

fileOut.write('''

|Name|Address|Txn|Amount|
|----|-------|---|------|
''')
for e in data:
    fileOut.write('|'+e[0]+'|'+
                  e[1]+'|'+
                  e[2]+'|'+
                  e[3]+'|'+'/n')
fileIn.close()
fileOut.close()
