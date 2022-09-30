## Stacks and Queues
Data structures called stacks and queues both store values in linked nodes. Queues employ a LILO data scheme, whereas stacks employ a LIFO data scheme. Because you always work with the node that is on top of the stack, stacks operate as a stack of nodes. In a similar way, queues work like a line of nodes, with you always interacting with the node at the front of the line.

## Challenge
We had to create push, pop, peek, and is_empty methods for both the Stack and Queue class. This allows us to add a new node to the top or rear, remove the top or front node and return its value, look at the value of the top or front node, and check if the Stack or Queue is empty and return the appropriate error.


## Approach & Efficiency
When utilizing the push or enqueue methods, the strategy is to make the new node the top or front of the stack or queue, respectively. We set the value of the top or front equal to the value of the next when removing a value from the stack or queue.

Time Efficiency:
O(1): Because only one step is needed to add or remove a node from the stack or queue, the time efficiency remains constant as the number of items grows.
Space Efficiency:
O(1): The function only needs to add or delete one value from the top or front, regardless of how big the stack or queue is, therefore the space efficiency is likewise constant.

## API
