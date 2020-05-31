class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key


def search(r,key):
    if(r==None):
        return print('Not Found')

    if(r.val==key):
        return print('Found')

    if(r.val < key):
        return search(r.right,key)
    
    return search(r.left,key)


def insert(root,node):
    if(root == None):
        root=node
    
    elif(root.val < node.val):
        if(root.right==None):
            root.right=node
        else:
            insert(root.right,node)
        
    else:
        if(root.left==None):
            root.left=node
        else:
            insert(root.left,node)


def preorder(r):
    if(r):
        print(r.val,end='->')
        preorder(r.left)
        preorder(r.right)

def inorder(r):
    if(r):
        inorder(r.left)
        print(r.val,end='->')
        inorder(r.right)


def postorder(r):
    if(r):
        postorder(r.right)
        postorder(r.left)
        print(r.val,end='->')

r=Node(11)

insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(50))
insert(r,Node(60))
insert(r,Node(10))
insert(r,Node(15))

preorder(r)
print()
inorder(r)
print()
postorder(r)
print()
search(r,10)



        
    

