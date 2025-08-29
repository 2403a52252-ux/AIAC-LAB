def compute_rations(values):
    results=[]
    for i in range(len(values)):
        for j in range(i,len(values)):
            if values[j] != values[i]:  # Prevent division by zero
                ratio=values[i]/(values[j]-values[i])
                results.append((i,j,ratio))
    return results
num=[5,10,15,20,25]
print(compute_rations(num))        
