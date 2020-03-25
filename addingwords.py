import fileinput

words = {}
other = {}
for line in fileinput.input():
    line = line.split()
    
    if line[0] == "clear":
        words = {}
        other = {}
    
    if line[0] == "def":
        word = line[1]
        value = int(line[2])
        
        if word in words:
            oldvalue = words[word]
            other.pop(oldvalue, None)
        
        words[word] = value
        other[value] = word
        
    if line[0] == "calc":
        line = line[1:]
        var = line[::2]
        ops = line[1::2]
        
        unknown = False
        
        for variable in var:
            if variable not in words:
                unknown = True
        
        if not unknown:
            total = words[var[0]]
            for i in range(len(ops) - 1):
                if ops[i] == "+":
                    total += words[var[i + 1]]
                if ops[i] == "-":
                    total -= words[var[i + 1]]
            
            if total not in other:
                unknown = True
        
        for i in line:
            print(i, end=" ")
        if unknown:
            print("unknown")
        else:
            print(other[total])