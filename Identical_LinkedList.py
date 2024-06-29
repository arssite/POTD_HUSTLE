'''Given the two singly Linked Lists respectively. The task is to check whether two linked lists are identical or not. 
Two Linked Lists are identical when they have the same data and with the same arrangement too. If both Linked Lists are identical then return true otherwise return false.'''


'''
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
'''

#Function to check whether two linked lists are identical or not.
def areIdentical(head1, head2):
    # Code here
    while head1!=None and head2!=None:
        flag=1
        if head1.data!=head2.data:
            flag=0
            return flag
        head1,head2=head1.next,head2.next
        
    return head1==None and head2==None


