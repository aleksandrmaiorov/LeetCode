##Feel free to use this code.
## OpenSource Rulez



class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        def clone_graph(node, indexed = dict()):
            if(not node):
                return None
            
            if(node.val in indexed):
                return indexed[node.val]
            
            indexed[node.val] = Node(node.val)
            for nei in node.neighbors:
                indexed[node.val]\
                .neighbors\
                .append(clone_graph(nei, indexed))
            
            return indexed[node.val]
        
        return clone_graph(node)
