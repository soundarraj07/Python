class node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
class Tree:
    def create(self,value):
        return node(value)
    def insert(self,node,value):
        if node is None:
            return self.create(value)
        if node.data>value:
            node.left=self.insert(node.left,value)
        else:
            node.right=self.insert(node.right,value)
        return node
    def delete1(self,root,key): # uses right min element to replace
        if not root: return None
        if root.data==key:
            if not root.right and not root.left: return None
            if not root.right and root.left: return root.left
            if root.right and not root.left: return root.right
            #if both
            temp=root.right
            while temp.left:temp=temp.left
            root.data=temp.data
            root.right=self.delete(root.right,root.data)
        elif root.data>key:
            root.left=self.delete(root.left,key)
        else:
            root.right=self.delete(root.right,key)
        return root
    def delete2(self,root,key): # uses left max element to replace
        if not root: return None
        if root.data==key:
            if not root.right and not root.left: return None
            if not root.right and root.left: return root.left
            if root.right and not root.left: return root.right
            #if both
            temp=root.left
            while temp.right:temp=temp.right
            root.data=temp.data
            root.left=self.delete2(root.left,root.data)
        elif root.data>key:
            root.left=self.delete2(root.left,key)
        else:
            root.right=self.delete2(root.right,key)
        return root
    def height(self,root):
        if root is None:
            return -1
        return max(self.height(root.left),self.height(root.right))+1
    def display(self,root):  #traverse inorder
        if root is not None:
            self.display(root.left)
            print(root.data)
            self.display(root.right)
    def display2(self,root):  #traverse pre-order
        if root is not None:
            print(root.data)
            self.display2(root.left)
            self.display2(root.right)
    def display3(self,root): #traverse post-order
        if root is not None:
            self.display3(root.left)
            self.display3(root.right)
            print(root.data)
tree=Tree()
root=tree.insert(None,9)
tree.insert(root,2)
tree.insert(root,43)
tree.insert(root,6)
tree.insert(root,28)
tree.insert(root,22)
tree.insert(root,56)
tree.insert(root,98)
tree.insert(root,33)
root=tree.delete2(root,90)
tree.display(root)
print("Height of the tree is : ",tree.height(root))