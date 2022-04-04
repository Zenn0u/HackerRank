class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method
        new_nd = Node(data)
        
        if head != None:
            prev = head
            
            while prev.next:
                prev = prev.next
                
            prev.next = new_nd
            
            return head
        
        else:
            return new_nd

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  