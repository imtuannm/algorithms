def tortoise_and_hare(path: list) -> bool:
    """
    An algorithm for Detecting a Loop in a Singly Linked List. 
    Invented by Robert Floyd who called it "Tortoise and Hare".
    Implemented by hmark.
    The Singly Linked List is implemented as a list of nodes.
    Each node in the list is itself a 2-element list, where
    the first element is the number of the node, and
    the second element is the number of the node it points to.

    .. testcode::
        looped_list = [ [0,1], [1,2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 3], [7, 8] ]
        straight_list = [ [0,1], [1,2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8] ]

        tortoise_and_hare(looped_list)
        tortoise_and_hare(straight_list)

    .. testoutput::
        True
        False
    """
    tortoise = path[0]  # slow pointer, starts at the beginning of the list
    hare = path[0]  # fast pointer, also starts at the beginning of the list
    end = path[-1]  # point to the last node

    while True:
        if hare == end:
            return False
        hare = path[hare[1]]  # move the fast pointer to the next node
        if hare == end:
            return False
        hare = path[hare[1]]  # move the fast pointer to gain twice the speed
        tortoise = path[tortoise[1]]  # move the slow pointer to the next node
        if hare == tortoise:
            return True
