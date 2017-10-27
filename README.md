# Data Structures

## Singly-Linked List
A data structure that links together nodes in one direction, beginning at a head node. This structure is used for keeping
track of sequentially related data where each piece of data only needs to point to the next in the chain and not back to the
previous one. 

push(data): Adds a new node to the head of the list.
Time complexity: O(1)

pop(): Removes node from the head of the list and returns its value. 
Time complexity: O(1)

size(): Returns the length of the list. 
Time complexity: O(1)

search(data): Iterates over the list to find the node containing the data passed as the
argument. Returns the node, if found, otherwise raises a ValueError.
Time complexity: O(n)

remove(data): Iterates over the list to find the node containing the data passed as the
argument. Reassigns the next attribute of the previous node to the next, to remove the reference to the specified node. Returns the value of the removed node. 
Time complexity: O(n)

display(data): Iterates over the entire list and concatenates a string with each node's value, then prints the complete string. 
Time complexity: O(n)

len(list): Overwrites built in len() function to show the same result as the size() function.
Time complexity: O(1)

print(list): Overwrites built in print() and str() functions to show the same result as the
display() function.
Time complexity: O(n)
