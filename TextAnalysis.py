import pyphen

inputFileName = input("Enter the file name (Include .txt): ")
inputFile = open(inputFileName, 'r')

dic = pyphen.Pyphen(lang='en')

superArr = inputFile.readlines()
superStr = ''
for i in superArr:
    superStr = superStr + i
    
superStr = superStr.replace('!','.')
superStr = superStr.replace('?','.')
superStr = superStr.replace(':','.')
superStr = superStr.replace(';','.')

sentenceArr = superStr.split('.')

i = 0
while(i < len(sentenceArr)):
    sentenceArr[i] = sentenceArr[i].replace('\n', ' ')
    sentenceArr[i] = sentenceArr[i].replace('\t', '')
    sentenceArr[i] = sentenceArr[i].replace('(', '')
    sentenceArr[i] = sentenceArr[i].replace(')', '')
    sentenceArr[i] = sentenceArr[i].replace('*', '')
    sentenceArr[i] = sentenceArr[i].replace('&', 'and')
    sentenceArr[i] = sentenceArr[i].replace('%', ' percent')
    sentenceArr[i] = sentenceArr[i].replace('-', ' ')
    sentenceArr[i] = sentenceArr[i].replace('[', '')
    sentenceArr[i] = sentenceArr[i].replace(']', '')
    sentenceArr[i] = sentenceArr[i].replace(',', ' ')
    sentenceArr[i] = sentenceArr[i].replace('/', ' ')
    sentenceArr[i] = sentenceArr[i].replace('  ', ' ')
    
    if (sentenceArr[i] == ''):
        sentenceArr.remove(sentenceArr[i])
    else:
        i += 1      

wordArr = []
for i in sentenceArr:
    wordArr.append(i.split(' '))

wordAmount = 0
for i in wordArr:
    wordAmount += len(i)

ASL = wordAmount / len(wordArr)

syllableArr = []
for i in wordArr:
    for j in i:
        wordSplit = dic.inserted(j)
        splitArr = wordSplit.split('-')
        for k in splitArr:
            syllableArr.append(k)
        
print(syllableArr)

i = 0
while (i < len(syllableArr)):
    if (syllableArr[i] == ''):
        syllableArr.remove(syllableArr[i])
    else:
        i += 1

ASW = len(syllableArr) / wordAmount

RE = 206.385 - (1.015 * ASL) - (84.6 * ASW)
print('The Readability Index of Text File - ' + inputFileName + ' - is ' + str(round(RE, 2)))
if (RE >= 90):
    print('This passage is very easy to read')
elif (RE >= 80):
    print('This passage is easy to read')
elif (RE >= 70):
    print('This passage is fairly easy to read')
elif (RE >= 60):
    print('This passage is standard')
elif (RE >= 50):
    print('This passage is fairly difficult to read')
elif (RE >= 30):
    print('This passage is difficult to read')
else:
    print('This passage is very confusing')
