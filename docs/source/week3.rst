Week 3: Searching for Solutions
===============================

Summary
^^^^^^^

Snow storms!

This week, we didn't meet because of snow storms.  To compensate for not meeting, you should read through the slides.   There are two things you should take away from the slides:

1. Python-Fu: list comprehensions
2. Different ways to search

It would be good if you also watch the video below.  You should have completed the algorithm for solving the missionaries and cannibals problem.  If you haven't, you should email me immediately.  Before next Sunday, you should play with different the code in `Searcher` class.  You should know the terms 'breadth-first' and 'depth-first' search from the slides and the video.

Let's look at the following code in the `Searcher` class:

.. code-block:: python
   :linenos:
   :emphasize-lines: 7,17

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

There are two parts to a search stack: taking items off the stack and putting it onto the stack.  Pop takes the furthest right item off the stack.  Extend adds the children one by one onto the right side.  What does this mean for exploration?  Is this breadth first or depth first?  How could you implement the other style?  Be prepared to answer these two questions in the next class.

Homework
^^^^^^^^

Answer the two questions from above:
  1. What style of uninformed search is currently implemented in the searcher?
  2. How could the other style of uninformed search be implemented?

Video to watch
^^^^^^^^^^^^^^

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/0ZKn8ggP5pA?list=PLASB3XZaQHuTa-ggdvIHGClpatf7NS0pX" frameborder="0" allowfullscreen></iframe>


Lecture Slides
^^^^^^^^^^^^^^
.. raw:: html

    <iframe src="https://docs.google.com/presentation/d/1SYj-q9dPVyXtQQEcqaN-3YYETEKqKEAnUdIR6tMwjz0/embed?start=false&loop=false&delayms=60000" frameborder="0" width="480" height="299" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
