class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowPointer = head
        fastPointer = head

        while fastPointer != None and fastPointer.next != None:  # Correct the condition here
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next

            if slowPointer == fastPointer:  # Fix typo here (slowpoiter -> slowPointer)
                return True

        return False
        