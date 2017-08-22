def binary_search(array,item):
    low=0;
    high=len(array)-1;
    while low<=high:
        mid=(high+low);
        guess=array[mid];
        if guess== item:
            return mid;
        if guess > high:
            high=mid-1;
        else:
            low=mid+1;
    return None;

array=[1,4,5,7,11,13,20];

print binary_search(array,15); # this will return None
print binary_search(array,7);  # This will return 3.

