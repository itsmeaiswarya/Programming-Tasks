class DoubleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        return

    def list_length(self):
        count=0
        current_node=self.head

        while current_node is not None:
            count=count+1
            current_node=current_node.next
        return count

    def output_list(self):
        current_node=self.head
        while current_node is not None:
            print(current_node.data)
            current_node=current_node.next
        return

    def  unordered_search(self,value):
        current_node = self.head
        node_id = 1
        results = []
        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)
            current_node = current_node.next
            node_id = node_id + 1

        return results