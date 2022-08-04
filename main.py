class test():
    print("hello class")
    print("kazu branch test")
    
class DatBoi():
    print("he a comin")
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# "3" -> "7" -> "10"
node1 = DatBoi("he")
node2 = DatBoi("a")
node3 = DatBoi("comin")

node1.next = node2 #node 1 is pointing to node 2, 3 points to 7
node2.next = node3 #node 2 points to node 3, 7 points to 10

currentNode = node1
while True:
    print(currentNode.value, "->", end=" ")
    if currentNode.next is None:
        print("LAWD")
        break
    currentNode = currentNode.next

print("this is a print")

demNotes = open('ur.txt', 'r')
read = demNotes.readlines() #printing read will have '\n' on all outputs
moddedNotes = [] #we create this for the incoming code that will remove '\n'

for line in read:
    if line[-1] == '\n': #if the final character is '\n'
        moddedNotes.append(line[:-1]) #[:-1], : includes all characters, -1 omits the last which was previous stated as '\n'
    else:
        moddedNotes.append(line) #because the final output from the txt file won't have the \n, we need this else statement so it doesn't try to remove anything

print(moddedNotes)




print("hello world")
print("poop")
print("poo")
print("doodoo")
#sup brah