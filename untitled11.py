class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtBegin(self,data):
        new_node=Node(data)
        if self.head is Node:
            self.head=new_node
            return
        else:
            new_node.next=self.head
            self.head=new_node 
    def insertAtIndex(self,data,index):
        new_node=Node(data)
        current_node=self.head
        position=0
        if position == index:
            self.insertAtBegin(data)
        else:
            while(current_node != None and position+1 != index):
                position=position+1
                current_node=current_node.next
            if current_node !=None:
                new_node.next=current_node.next
                current_node.next=new_node
            else:
                print("index not present")
                
    def insertAtEnd(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        current_node=self.head 
        while(current_node.next):
            current_node=current_node.next
        current_node.next=new_node 
    def remove_first_node(self):
        if(self.head == None):
            return
        self.head = self.head.next 
    def remove_last_node(self):
        if self.head is None:
            return
        current_node=self.head
        while(current_node.next.next):
            current_node=current_node.next
            if current_node.next:
                current_node.next=None
            else:
                self.head=None
    def remove_node(self,data):
        current_node=self.head 
        if current_node.data == data:
            self.remove_first_node()
            return
        while current_node is not None and current_node.next.data != data:
            current_node = current_node.next
        if current_node is None:
            return
        else:
            current_node.next=current_node.next.next 

            
            
            
            
            
            
            
            
            
            
            
            
            
                
    
                
                
                
                
                
                
                
                