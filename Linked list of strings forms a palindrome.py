def compute(head): 
    #return True/False
    lst=''
    while head:
        lst=lst+head.data
        head=head.next
    if lst==lst[-1::-1]:
        return True
    else:
        return False
