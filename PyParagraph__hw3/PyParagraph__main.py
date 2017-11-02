import re
#re.split("(?&lt;=[.!?]) +", paragraph)


pFiction = open('paragraph_1.txt', 'r')

print(pFiction)

pFiction_rd = pFiction.read()

pFiction_array = pFiction_rd.split(" ")

print("Approximate Word Count: " + str(len(pFiction_array)))

#sentences = re.split("[.]|[!]|[?]", pFiction_rd)
sentences = re.split(r'[.!?]+', pFiction_rd)
print(sentences)

print("Approximate Sentence Count: " + str(len(sentences)))

wordCountArray = []
for each in pFiction_array:
    wordCountArray.append(len(each))

totalLetters = 0
for each in wordCountArray:
    totalLetters += each

print("Average Letter Count: " + str(totalLetters/(len(wordCountArray))))

average_sentence_length = len(pFiction_array)/len(sentences)

print("Average Sentence Length: " + str(average_sentence_length))


pFiction.close()


