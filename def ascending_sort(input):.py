def ascending_sort(input):
    if not isinstance(input,list):
        raise TypeError
    # find the smallest one 
    def find_the_smallest(input):
        storage =[input[0],0]
        for i in range(1,len(input)):
            if storage[0]>input[i]:
                storage[0]=input[i]
                storage[1]=i
        return storage
    for j in range(len(input)):
        to_be_processed=input[j:]
        storage=find_the_smallest(to_be_processed)
        index=storage[1]+j
        input[index]=input[j]
        input[j]=storage[0]
    return input


class Item:
    def __init__(self,val,flag):
        self.value=val
        self.flag=flag
        
    

def bubble_sort(input):
    if not isinstance(input,list):
        raise TypeError
    processed=[]
    output=[]
    for i in range(len(input)):
        item=Item(input[i],False)
        processed.append(item)
           
    for n in range(len(input)-1):
        counter=0
        if processed[n].flag or processed[n+1].flag:
            counter+=1
            continue
        
        if processed[n].value>processed[n+1].value:
            processed[n+1].value=processed[n].value
            processed[n].value=processed[n+1].value
            
        if processed[n+1].value-processed[n].value==1:
            processed[n].flag=True
            processed[n+1].flag=True
        
        if counter==len(input)-1:
            return
        
        if n==len(input)-2:
            n=0
    for i in processed:
        output.append(i.value)
    return output
        
        
            
input=[1,3,2,4,6,9,8]
print(bubble_sort(input))