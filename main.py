class test():
    print("hello class")
    
class DatBoi():
    print("he a comin")
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# "3" -> "7" -> "10"
node1 = DatBoi("3")
node2 = DatBoi("7")
node3 = DatBoi("10")

node1.next = node2 #node 1 is pointing to node 2, 3 points to 7
node2.next = node3 #node 2 points to node 3, 7 points to 10

currentNode = node1
while True:
    print(currentNode.value, "->", end=" ")
    if currentNode.next is None:
        print("None")
        break
    currentNode = currentNode.next





print("hello world")
print("poop")
print("poo")
print("doodoo")
#sup brah