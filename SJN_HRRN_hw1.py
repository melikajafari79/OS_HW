p = int (input("number of processes:"))
l_pID = []
l_AT = []
l_ET = []
l_ST = []
for i in range (p):
    AT = int (input("AT p{0}:".format(i)))
    ET = int (input("ET p{0}:".format(i)))
    l_pID.append(i)
    l_AT.append(AT)
    l_ET.append(ET)

  
m = min(l_AT)
counter = 0
for i in l_AT:
    l_AT[counter] = i - m
    counter += 1


def HRRN (l_AT, l_ET):
    l_AT_copy = l_AT.copy()
    time = 0
    l_ST = [0]*(len(l_AT))
    queue = []
    x = len(l_AT_copy)
    for j in range(x):
        counter = 0
        ind = []
        target_list = []
        for i in l_AT_copy:
            if i <= time and i >= 0:
                a = ((time - l_AT[counter]+ 1) / l_ET[counter]) 
                target_list.append(a)
                ind.append(counter)
            counter += 1
        max_value = max(target_list)
        a = target_list.index(max_value)
        counter = ind[a]
        l_AT_copy[counter] = float('inf')
        l_ST[counter] = time
        queue.append((counter, time))
        time += l_ET[counter]
        min_value = min(l_AT_copy)
        if time < min_value:
            time = min_value
    print(l_ST)
    return queue
        
      
               
def SJN (l_AT, l_ET):
    time = 0
    l_ST = [0]*(len(l_AT))
    queue = []
    l_AT_copy = l_AT.copy()
    l_ET_copy = l_ET.copy()
    for i in l_AT_copy:
        target_ind = l_AT_copy.index(i)
        for j in range (len(l_AT_copy)):
            if l_AT_copy[j] <= time and l_ET_copy[j] < i:
                target_ind = j
        l_ST[target_ind] = time
        queue.append((target_ind, time))
        time += l_ET[target_ind]
        min_value = min(l_AT_copy)
        if time < min_value:
            time = min_value
        l_AT_copy[target_ind] = float('inf')
        l_ET_copy[target_ind] = float('inf')
    print(l_ST)
    return queue
            
print(HRRN (l_AT, l_ET))
print(SJN (l_AT, l_ET))   