class Solution:
    def reverseBetween(
        self,
        head: Optional[ListNode],
        left: int,
        right: int
    ) -> Optional[ListNode]:

        # Dummy node helps when left = 1
        dummy = ListNode(0)
        dummy.next = head

        # Move prev to the node just before left
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        # Start of the section we want to reverse
        curr = prev.next

        # Reverse the section
        for _ in range(right - left):
            temp = curr.next

            curr.next = temp.next

            temp.next = prev.next

            prev.next = temp

        return dummy.next