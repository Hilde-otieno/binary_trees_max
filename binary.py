class Node:  
    def __init__(self,data):  
        self.data = data;  
        self.left = None;  
        self.right = None;  
   
class LargestNode:  
    def __init__(self):  
        self.root = None;  
          
    def largestElement(self, temp):  
        if(self.root == None):  
            print("Tree is empty");  
            return 0;  
              
        else:      
            maximum = temp.data;  
                
            if(temp.left != None):  
                leftMax = self.largestElement(temp.left);    
                maximum = max(maximum, leftMax);  
               
            if(temp.right != None):  
                rightMax = self.largestElement(temp.right);  
                maximum = max(maximum, rightMax);  
              
            return maximum;  
   
bt = LargestNode();  
bt.root = Node(25);  
bt.root.left = Node(30);  
bt.root.right = Node(40);  
bt.root.left.left = Node(85);  
bt.root.right.left = Node(65);  
bt.root.right.right = Node(12);  
   
print("Largest element in the binary tree: " + str(bt.largestElement(bt.root))); 