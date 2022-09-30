## Merge Sort

Merge Sort is an algorithm that sorts a list of values by splitting the given list in half and then recursively calling itself to do it again. It continues to split until each half of the list contains only one value, at which point the recursive calls are done and the stack begins to resolve. The values are then actually sorted by the merge function, which compares values and merges them together into one array in ascending order of values.


## Step 1
We begin the first stage by using merge sort on the entire list. Our list is split into the left and right lists. Then, merge sort calls itself repeatedly while passing the newly created left list. Then merge sort is called one more recursively, passing in right. Keep in mind that because of the order in which the recursive calls are made, the left half of the tree resolves before the right half.


## Step 2

Step 2 involves splitting our list of left into separate lists of left and right. Then, using left and then right, we perform another recursive call. The same thing occurs when it is resolved on the stack for right.

## Step 3

Once more, a new left and right are created from our new left. It then makes another recursive call, passing in left and then right. Our right list, which at this time just contains the value 23, no longer divides or performs recursive calls because there is only one item. The lists [42,16] and [15] on the right side follow the same procedure.


## Step 4

We can see in step 4 that each list now only has one value. As a result, the division and recursive calls are complete. We will now begin resolving the call stack. The merge function is called on merge sort's last line, following both recursive calls. This is where the real sorting happens. Based on the values of each item in the list, we begin combining the values of the two lists into one list. With only one value in each list, it is really simple. The value that is lower is added first, followed by the other value, and so on.


## Step 5

Here, one list has two values while the other only contains one. We begin to really filter through some data at this point. We compare the values after iterating over each item in both lists. Since 4 is less than 23 in this instance, it is added to the list. We then contrast 8 and 23. Eight is added to the list since it is smaller. When one list runs out of values, we simply append the last few items from the other list to the end of the first. This implies that regardless of its value, 23 is just appended to the end. When it is resolved on the stack, the entire procedure for [16,42] and [15] takes place.

## Step 6

We loop through two lists that both have several values in this phase. We go over both lists again and compare the values on each list to one another. Given that 4 is less than 15, we start by adding it to the new list. 8 is added to the list once we realize that it is also less than 15, which is 15. Since 23 is now more than 15, 15 is added. Because 23 is likewise bigger than 16, you may also include 16. Since 23 is less than 42, we add it to the list, but now there are no more numbers in the left list. Therefore, the list is simply extended by 42.


## Step 7

The call stack has been resolved, and we now have our finished list. All of the values from our first list are there in this new list, but they are now arranged in ascending order. We finish up by having our function return this new sorted list at this point.
