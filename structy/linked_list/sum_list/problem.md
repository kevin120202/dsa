# Sum List

Write a function, `sum_list`, that takes in the head of a linked list containing numbers as an argument. The function should return the total sum of all values in the linked list.

## Examples

### Example 1
```python
a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

# 2 -> 8 -> 3 -> -1 -> 7

sum_list(a) # 19
```

### Example 2
```python
z = Node(100)

# 100

sum_list(z) # 100
```

### Example 3
```python
sum_list(None) # 0
```
