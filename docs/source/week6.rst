Week 6: Navigation, Part 1
==========================

Summary
-------

We covered the shortest path algorithms and navigation through search.
Specifically, we start from how to select actions and worked our way through
to A* search. We made it to just before A* got fully developed. However, we did cover the development of a bot that had the following qualities:

1. Calculate the position of a move applied to a location
2. Determine the distance from that location to the food
3. Rank the possible moves according to how close they are to the food
4. Explore several moves in the future using a greedy policy
5. Keep track of where the last move came from.
6. After finding a move that reaches the food, backtrack to find the best move.

There are a bunch of issues it runs into.  The homework will have you look at that.


Resources
---------

1. `Red Blob (Amit Patel)'s Fantastic tutorial <http://www.redblobgames.com/pathfinding/a-star/introduction.html>`_
2. `Sebastian Lague's Youtube video <https://www.youtube.com/watch?v=-L-WgKMFuhE>`_

Homework
--------

Using the Worm Wars code (you can find it `here <https://github.com/braingineer/AI-games>`_ or on in the course github repository), run the AwesomeBot and figure out what is going on.  Why does it lose?  You should be prepared to talk about why you think it fails.

Additionally, you should go through the code and comment each line in AwesomeBot, so that you can explain how the algorithm is working.  You should use the Red Blob site and the slides for reference.

Lecture Slides
--------------

.. raw:: html

    <iframe src="https://docs.google.com/presentation/d/1Lt9fkJwkOdsSEzd4Ruih4Ka-TbeIdI3ZdQwLd6v5jZg/embed?start=false&loop=false&delayms=3000" frameborder="0" width="480" height="299" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
