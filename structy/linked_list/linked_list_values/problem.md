# Linked List Values

Write a function, `linked_list_values`, that takes in the head of a linked list as an argument. The function should return a list containing all values of the nodes in the linked list.

## Examples

### Example 1
```python
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

linked_list_values(a) # -> [ 'a', 'b', 'c', 'd' ]
```

### Example 2
```python
x = Node("x")
y = Node("y")

x.next = y

# x -> y

linked_list_values(x) # -> [ 'x', 'y' ]
```

### Example 3
```python
q = Node("q")

# q

linked_list_values(q) # -> [ 'q' ]
```

### Example 4
```python
linked_list_values(None) # -> [ ]
```
