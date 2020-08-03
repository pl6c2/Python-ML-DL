f = open("words", "r")   # opening a file
data = f.read()           # reading file
print(data.split( ))
data1=data.split( )           # split the data

counts = dict()             # create a dictionary

for word in data1:
    if word in counts:        # check if the word is already in dict
        counts[word] += 1      # incrementing the count of the word
    else:
        counts[word] = 1       # if the word in new assign count as 1

print(counts)


f1 = open("output", "w")
f1.write(str(counts))
f1.close()
