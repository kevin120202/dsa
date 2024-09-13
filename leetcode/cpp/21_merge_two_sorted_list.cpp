struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* dummy = new ListNode(0);
        ListNode* curr = dummy;
        ListNode* ptr1 = list1;
        ListNode* ptr2 = list2;

        while (ptr1 && ptr2) {
            if (ptr1->val < ptr2->val) {
                curr->next = ptr1;
                ptr1 = ptr1->next;
            }
            else {
                curr->next = ptr2;
                ptr2 = ptr2->next;
            }
            curr = curr->next;
        }

        if (ptr1) {
            curr->next = ptr1;
        }

        if (ptr2) {
            curr->next = ptr2;
        }

        return dummy->next;
    }
};