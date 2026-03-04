import random
random.seed(0)

def bucket_sort(mylist):
    # initialize the buckets
    mydict = {}
    for i in mylist:
        number=i//10
        if not str(number) in mydict:
            mydict[str(number)]=[]
        mydict[str(number)].append(i)
        
    def insertion_sort(lst):
        for i in range (1, len(lst)):
            v=lst[i]
            j=i-1
            while j>=0 and lst[j]>v:
                lst[j+1]=lst[j]
                j-=1
            lst[j+1]=v
        return lst
    
    for abucket in mydict:
        mydict[abucket]=insertion_sort(mydict[abucket])
    
    
    
    

    # sort each bucket 
    
    result = []
    for i in range(10):
        result.extend(mydict[str(i)])
        
    return result

def main():
    """ this is not exactly relevant, but the following 4 lines of
    code can be replaced by one line:
    list_a = [random.randint(0, 99) for i in range(100)]
    """
    list_a = []
    for i in range(100):
        list_a.append(random.randint(0,99))
    print(list_a)

    list_a = bucket_sort(list_a)
    print("SORTED:", list_a)    

main()
