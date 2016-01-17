"""
Missionaries and Cannibals
"""

from copy import deepcopy
import logging

logging.basicConfig(filename='mc.log',level=logging.DEBUG)


class MCState:
    def __init__(self, specs=None):
        """
            Initialize the specs, which is what I've called the variables here
        """
        if specs == None:
            # the order is missionaries, cannibals
            specs = {"left":(3,3), "right": (0,0), 'boat': 'left'}

        self.specs = specs

        # this could be useful if you want to name the moves and understand
        # what is going on
        self.move = "Initial State"

    def next_states(self):
        """
            Generate all possible next states

            One possible method is to generate every single possible change
                by using all possible movement numbers:
                    (2,0), (1,1), (0,2), (1,0), (0,1)
                and then checking to see if it's a bad move.
                If it's not a bad move, then add it to the state list
        """
        state_list = []
        return state_list


    def translate(self, move, new_spec):
        """
            Translate the state variables into an english description

            If you are keeping track of the move names for prettier printing
            or for debugging, you could use this to translate the move
            information (maybe the (1,1) from above) and the spec into
            a description of what's happening.
        """
        out = "Moved {} Missionaries and {} Cannibals to the {} shore"
        return out


    def apply_move(self, move, spec):
        """
            Create a copy of the specifications and return the updated ones

            Using deepcopy insures that we won't accidentally have variables
            get contaminated.

            Apply the movement information so that the new state variables
            represent the new information
        """
        new_spec = deepcopy(spec)
        return new_spec

    def bad_move(self, spec):
        """
            Test for the move being bad

            Rather than generating only good moves, we could generate all moves
            and then filter out the ones that are bad.  This is the filtering function.
        """
        bounds = False
        bad_left = False
        bad_right = False
        return bad_left or bad_right or bounds

    def is_solution(self):
        """ Returns boolean reflecting whether this is a solution """
        return self.specs["right"] == (3,3)

    def __str__(self):
        """ string representation. """
        mi_left, ca_left = self.specs['left']
        mi_right, ca_right = self.specs['right']
        boat = self.specs['boat']
        return "Left(M={},C={})&Right(M={},C={})&Boat={}".format(mi_left, ca_left,
                                                                 mi_right, ca_right,
                                                                 boat)

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))


class Node:
    def __init__(self, state=None, seen_set=None, back_pointer=None):
        """Encapsulate the search process.

        Args:
            state : The state object for this Node. If no state object is passed,
                    then it defaults to the initial state.

            seen_set : The state objects that proceeded the current state object.
                       If no set is passed, it creates a new set

            back_pointer : The Node object that generated this Node object
                           If none is passed, this Node is assumed to be the
                           original (root) Node.
        """
        self.back_pointer = back_pointer

        if state is None:
            state = MCState()
        self.state = state

        if seen_set is None:
            self.seen_set = set()
        else:
            self.seen_set = deepcopy(seen_set)

        self.seen_set.add(self.state)

    def is_solution(self):
        """ Returns a boolean for whether this is a solution """
        return self.state.is_solution()

    def get_children(self):
        """Return the Nodes that occur after this Node

        Returns:
            all_children : A List of Node objects which contain the MCState objects
                 that are the next steps in the problem solving procedure.
                 No objects that have been seen on this Node's path will be
                 in this list.
        """
        all_children = []
        possible_children = self.state.next_states()
        for child in possible_children:
            if child not in self.seen_set:
                new_node = Node(child, self.seen_set, self)
                all_children.append(new_node)
        return all_children

class Searcher:
    def run(self):
        """Run the problem solving procedure.

        Starting with the initial state, travel through the tree, keeping track
        of all possible paths.

        This simple algorithm also keeps track of the solutions and prints them
        out.
        """
        initial = Node()
        frontier = list()
        frontier.append(initial)

        solutions = list()
        round_counter = 0
        not_stuck_in_loop = True
        while len(frontier) > 0 and not_stuck_in_loop:
            logging.debug("\n\n==round: {}==".format(round_counter))
            round_counter+=1
            not_stuck_in_loop = round_counter < 10**10

            # pop removes the last element from the list and returns it
            cur_node = frontier.pop()
            logging.debug("Current State: {}".format(str(cur_node.state)))

            if cur_node.is_solution():
                solutions.append(cur_node)
                # after we see a solution, we don't expand its children
                # so, we use continue which proceeds to the next loop cycle
                continue

            next_children = cur_node.get_children()
            frontier.extend(next_children)
            for child in next_children:
                logging.debug("Added {} to the frontier".format(str(child.state)))

        print("==== finished ====")
        print("{} solutions".format(len(solutions)))
        for sol in solutions:
            self.print_solution(sol)

    def print_solution(self, sol):
        pass

Searcher().run()
