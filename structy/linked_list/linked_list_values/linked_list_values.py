def linked_list_values(head):
  res = []
  while head:
    res.append(head.val)
    head = head.next
  return res