class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)


    
    def contains_state(self, state):
        """Checks if a state (final state) is the frontier
        
        Inputs:
            state: check if this state in the frontier"""
        return any(node.state == state for node in self.frontier)

    def empty(self):
        """Returns: bool if frontier is empty (True) or not (False) - no inputs"""
        return len(self.frontier) == 0

    def remove(self):
        """Returns: Most recently added node in frontier (i.e. last node in list) and
        removes it from the frontier - No inputs. Last In First Out (LIFO)"""
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            # Remove the most recently added node from the frontier
            self.frontier = self.frontier[:-1]
            # Return the removed node
            return node


class QueueFrontier(StackFrontier):
    """Returns: Oldest added node in frontier (i.e. first node in list) and
    removes it from the frontier - No inputs. First In First Out (FIFO)"""

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
