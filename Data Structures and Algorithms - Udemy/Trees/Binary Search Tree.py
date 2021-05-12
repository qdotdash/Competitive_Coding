class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self):
        self.root = None 

    def insert(self, value):
        newNode = Node(value)
        if(self.root==None):
            self.root = newNode
        else:
            temp = self.root
            flag = 0
            while(1):
                if(value>temp.value):
                    if(temp.right==None):
                        temp.right = newNode
                        break
                    else:
                        temp=temp.right
                else:
                    if(temp.left==None):
                        temp.left = newNode
                        break
                    else:
                        temp=temp.left
    # if root is passed then unecessary overall lookup for inorder can be eliminated in deletion
    def lookup(self, value):
        parentNode = -1 # node to save the parent node
        if(self.root==None):
            print("Not found")
        else:
            temp = self.root
            foundFlag = 0
            while(temp!=None):
                # print("--", temp.value)
                # print(temp.__dict__)
                if(value==temp.value):
                    print(value, " found")
                    foundFlag = 1
                    break
                elif(value>temp.value):
                    parentNode = temp
                    temp = temp.right
                else:
                    parentNode = temp
                    temp = temp.left

            if(foundFlag!=1):
                print("Not found")
                return None
            else:
                return parentNode

    def inorder(self, node, inorderList):

        if(node.left!=None):
            self.inorder(node.left, inorderList)

        inorderList.append(node.value)

        if(node.right!=None):
            self.inorder(node.right, inorderList)

        return inorderList
            

    def preorder(self, node, preorderList):   

        preorderList.append(node.value)

        if(node.left!=None):
            self.preorder(node.left, preorderList)
        

        if(node.right!=None):
            self.preorder(node.right, preorderList)

        return preorderList

    def postorder(self, node, postorderList):
    
        if(node.left!=None):
            self.postorder(node.left, postorderList)
        

        if(node.right!=None):
            self.postorder(node.right, postorderList)

        postorderList.append(node.value)

        return  postorderList


    def returnRoot(self):
        return self.root
    
    def getInorderSuccessor(self, newRoot):
        if(newRoot.left!=None):
            return self.getInorderSuccessor(newRoot.left)
        else:
            return newRoot
        
    def delete(self, value):
        parentNode = self.lookup(value)

        #element not found
        if(parentNode==None):
            return

        # root is the element to be deleted
        if(parentNode==-1):
            targetNode = self.root
            if(targetNode.left==None and targetNode.right==None):
                print(self.root.value, " deleted")
                self.root = None
            # only left subtree
            elif(targetNode.right==None):
                self.root = self.root.left
            # only right subtree
            elif(targetNode.left==None):
                self.root = self.root.right
            else:
                newValueToNode = self.getInorderSuccessor(targetNode.right)
                tempStore = newValueToNode.value
                self.delete(newValueToNode.value)
                targetNode.value = tempStore
            return
        
        # value is in left subtree of parent
        if(value<parentNode.value):
            targetNode = parentNode.left
            # if a leaf node
            if(targetNode.left==None and targetNode.right==None):
                parentNode.left = None
            # only left subtree
            elif(targetNode.right==None):
                parentNode.left = targetNode.left
            # only right subtree
            elif(targetNode.left==None):
                parentNode.left = targetNode.right
            else:
                newValueToNode = self.getInorderSuccessor(targetNode.right)
                tempStore = newValueToNode.value
                self.delete(newValueToNode.value)
                targetNode.value = tempStore
                
        # value is in right subtree of parent
        else:
            targetNode = parentNode.right
            # if a leaf node
            if(targetNode.left==None and targetNode.right==None):
                parentNode.right = None
            # only left subtree
            elif(targetNode.right==None):
                parentNode.right = targetNode.left
            # only right subtree
            elif(targetNode.left==None):
                parentNode.right = targetNode.right
            else:
                newValueToNode = self.getInorderSuccessor(targetNode.right)
                tempStore = newValueToNode.value
                self.delete(newValueToNode.value)
                targetNode.value = tempStore
    

        

bst = BinarySearchTree()
bst.insert(30)
bst.insert(20)
bst.insert(15)
bst.insert(5)
bst.insert(18)
bst.insert(25)
bst.insert(40)
bst.insert(35)
bst.insert(50)
bst.insert(45)
bst.insert(60)
print("\n\n")
print(bst.inorder(bst.returnRoot(), []))
print("\n\n")
print(bst.preorder(bst.returnRoot(), []))
print("\n\n")
print(bst.postorder(bst.returnRoot(), []))
print("\n\n")
bst.delete(20)
bst.delete(30)
bst.delete(45)
bst.delete(60)
bst.delete(45)
bst.delete(15)
bst.insert(15)
bst.insert(3)
bst.delete(5)
print("\n\n")
print(bst.inorder(bst.returnRoot(), []))
print("\n\n")
print(bst.preorder(bst.returnRoot(), []))
print("\n\n")
print(bst.postorder(bst.returnRoot(), []))
print("\n\n")




            