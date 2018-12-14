# Problem: https://leetcode.com/problems/merge-two-sorted-lists/


class SinglyLinkedList:
    def __init__(self):
        self.root = None
        self.last = self.root

    def add_node(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.root is None:
            self.last = self.root = ListNode(num)
        else:
            self.last.next = ListNode(num)
            self.last = self.last.next

    def add_from_array(self, nums):
        """
        :param nums: array
        :rtype: None
        """
        for num in nums:
            self.add_node(num)

    @staticmethod
    def print_list(root):
        """
        :param root: ListNode
        :return: None
        """
        if root is None:
            print(None)
            return

        node_string = str(root.val)
        root = root.next
        while root:
            node_string += f"->{root.val}"
            root = root.next

        print(node_string)


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2

        if not l2:
            return l1

        current = root = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                current.next = ListNode(l2.val)
                current = current.next
                l2 = l2.next
            else:
                current.next = ListNode(l1.val)
                current = current.next
                l1 = l1.next

        if l1:
            current.next = l1

        if l2:
            current.next = l2

        return root.next


# Test Data
l1 = SinglyLinkedList()
l1.add_from_array([1, 2, 4, 5])

l2 = SinglyLinkedList()
l2.add_from_array([1, 3, 4, 6])

solution = Solution()
result = solution.mergeTwoLists(l1.root, l2.root)

print("input:")
SinglyLinkedList.print_list(l1.root)
SinglyLinkedList.print_list(l2.root)

# Output result
print("Output:")
SinglyLinkedList.print_list(result)


