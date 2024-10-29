<h2>
  How to Sort a List of Numbers
</h2>

<p>Python lists have a built-in list.sort() method that modifies the list in-place. There is also a sorted() built-in function that builds a new sorted list from an iterable.
In this document, we explore the various techniques for sorting data using Python.</p>

<h3>Multiple Ways to Sort List of Numbers or Integers</h3>
<h4>Method 1: Using the sorted() function</h4>
<p>The sorted() function returns a sorted list of the specified iterable object. You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically. Note: You cannot sort a list that contains BOTH string values AND numeric values.</p>

<h4>Method 2: Using the sort() method:</h4>
<p>The sort function can be used to sort the list in both ascending and descending order. It can be used to sort lists of integers, floating point numbers, strings, and others in Python. Its time complexity is O(NlogN)</p>

<h4>Method 3: Using the [::-1] slicing technique: </h4>
<p>The slicing method is a method of economic analysis used in microeconomics for in-depth study of economic units. In this method, the economy is divided or 'sliced' into smaller units like individual households, individual firms etc.</p>

<h4>Method 4: Using the Lambda Function with sorted()</h4>
<p>You can “lambda sort” a list with both the sort() method and the sorted() function. Let’s look at how to lambda sort with the sort() method first.</p>
<p>lambda name: name.split()[1]</p>
<p>The lambda function splits a name and takes the second part of the name – the second name. The first part is the first name and it would be [0].
You can pass in this lambda function as the key parameter – sorting the names by the second names:</p>

<h4>Method 5: Using heapq module for large lists: </h4>
<p>Heap is a data structure, that is mainly used to represent a priority queue. In Python, it is available by importing the heapq module. Heapq has a property that every time the smallest heap element is popped (min-heap). Each time when an element is pushed or popped the heap structure is maintained.</p>
