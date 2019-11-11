#   Ian Norris



from tree_node import TreeNode

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0
        self.maxheight = 0
    
    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def current_height(self):
        # Start of height code: starts heightHelper with root node of BST
        # print('Search tree: ', self, 'Left Child: ', self.root.leftChild)
        # if self.root.leftChild:
        #     return 1 + self.root.leftChild.height()
        # elif self.root.rightChild:
        #     return 1 + self.root.rightChild.height()
        # else:
        #     return 0

        #Does not work very well
        if self.root:
            return self.root.getHeight()
        else:
            return 0

    def __str__(self):
        """Returns a string representation of the tree
           rotated 90 degrees counter-clockwise"""

        def strHelper(root, level):
            resultStr = ""
            if root:
                resultStr += strHelper(root.rightChild, level+1)
                resultStr += "| " * level
                resultStr += str(root.key) + "\n"
                resultStr += strHelper(root.leftChild, level+1)                
            return resultStr
                

        return strHelper(self.root, 0)
    

    def __contains__(self,key):
        if self._get(key,self.root):
            return True
        else:
            return False

    def get(self,key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)

    def __getitem__(self,key):
        return self.get(key) 

    def __setitem__(self,k,v):
        self.insert(k,v)

    def insert(self,key,val):
        if self.root:
            self._insert(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
            self.maxheight += 1
        self.size = self.size + 1

    def _insert(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._insert(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,
                                          parent=currentNode)

                # Keep track of max height
                if currentNode.rightChild:
                    pass
                else:
                    self.maxheight += 1
        elif key > currentNode.key:
            if currentNode.hasRightChild():
                self._insert(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,
                                          parent=currentNode)
                #Keep track of max height
                if currentNode.leftChild:
                    pass
                else:
                    self.maxheight += 1
        else:
            currentNode.payload = val
            self.size -= 1

    def delete(self,key):
      if self.size > 1:
          nodeToRemove = self._get(key,self.root)
          if nodeToRemove:
              self.remove(nodeToRemove)
              self.size = self.size-1
          else:
              raise KeyError('Error, key not in tree')
      elif self.size == 1 and self.root.key == key:
          self.root = None
          self.size = self.size - 1
      else:
          raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
        self.delete(key)


    def remove(self,currentNode):
      if currentNode.isLeaf(): #leaf
        if currentNode == currentNode.parent.leftChild:
            currentNode.parent.leftChild = None
        else:
            currentNode.parent.rightChild = None
      elif currentNode.hasBothChildren(): #interior
        succ = currentNode.findSuccessor()
        succ.spliceOut()
        currentNode.key = succ.key
        currentNode.payload = succ.payload

      else: # this node has one child
        if currentNode.hasLeftChild():
          if currentNode.isLeftChild():
              currentNode.leftChild.parent = currentNode.parent
              currentNode.parent.leftChild = currentNode.leftChild
          elif currentNode.isRightChild():
              currentNode.leftChild.parent = currentNode.parent
              currentNode.parent.rightChild = currentNode.leftChild
          else:
              currentNode.replaceNodeData(currentNode.leftChild.key,
                                 currentNode.leftChild.payload,
                                 currentNode.leftChild.leftChild,
                                 currentNode.leftChild.rightChild)

        else:
          if currentNode.isLeftChild():
              currentNode.rightChild.parent = currentNode.parent
              currentNode.parent.leftChild = currentNode.rightChild
          elif currentNode.isRightChild():
              currentNode.rightChild.parent = currentNode.parent
              currentNode.parent.rightChild = currentNode.rightChild
          else:
              currentNode.replaceNodeData(currentNode.rightChild.key,
                                 currentNode.rightChild.payload,
                                 currentNode.rightChild.leftChild,
                                 currentNode.rightChild.rightChild)

    def max_height(self):
        return self.maxheight

    def traverse_inorder(self, node=None, isRoot=True):
        if isRoot:
            node = self.root
            isRoot = False
        if not node:
            return
        self.traverse_inorder(node.leftChild, False)
        print(node.key)
        self.traverse_inorder(node.rightChild, False)

    def traverse_inorder(self, node=None, isRoot=True):
        if isRoot:
            node = self.root
            isRoot = False
        if not node:
            return
        self.traverse_inorder(node.leftChild, False)
        print(node.key)
        self.traverse_inorder(node.rightChild, False)

    def traverse_preorder(self, node=None, isRoot=True):
        if isRoot:
            node = self.root
            isRoot = False
        if not node:
            return
        print(node.key)
        self.traverse_preorder(node.leftChild, False)
        self.traverse_preorder(node.rightChild, False)

    def traverse_postorder(self, node=None, isRoot=True):
        if isRoot:
            node = self.root
            isRoot = False
        if not node:
            return
        self.traverse_postorder(node.leftChild, False)
        self.traverse_postorder(node.rightChild, False)
        print(node.key)


# def main():
#     t = BinarySearchTree()
#     t.insert(5,5)
#     t.insert(3,3)
#     t.insert(8,8)
#     t.insert(10, 10)
#     t.insert(7,7)
#     print(t)
#     print("Height:",t.height())
#     return t
#
# if __name__ == "__main__": t = main()


