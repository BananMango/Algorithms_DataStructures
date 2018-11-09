# Data Structures
**Python** is a dynamically typed language, as there is no advance declaration associating an identifier with a particular data type. Built-in classes can be divided into mutable and immutable(A class is immutable if each object of that class has a fixed value upon instantiation that cannot subsequently be changed). Mutable classes are: list, set, dict; And immutable: bool, int, float, tuple, str.

* **Bool** class is used to manipulate logic values, and the only two instances of that class are expressed as the literals True and False (default constructor bool(), returns False)
* **Int** class is primary numeric type in Python. The integer constructor int() returns 0 by default. 
* **Float** class is second primary numeric type in Python and is the sole floating-point type. The float constructor returns 0.0 by default
* **List** class is sequence class in Python that stores a sequence of object. It is a referential structure as it stores a sequence of references to its elements. Lists have valuable behaviors, including the ability to dynamically expand and contract their capacities as needed. Python uses [] to delimit a list.
* **Tuple** class is second sequence class in Python, unlike list it is immutable. Python uses () to initialize a tuple.
* **Str** class is third sequence class in Python that is designed to efficiently represent an immutable sequence of characters.
* **Set** class represents the mathematical notion of a set, namely a collection of elements, without duplicates, and without an inherent order to those elements. The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set.This is based on a data structure known as a hash table. However, there are two important restrictions due to the algorithmic underpinnings. The first is that the set does not maintain the elements in any particular order. The second is that only instances of immutable types can be added to a Python set. **Frozenset** class is an immutable form of the set type, so it is legal to have a set of frozensets.
* **Dict** class represents a dictionary, or mapping, from a set of distinct keys to associated values.
______________________________________________________________________________________________________________________________
* **Array** is a low-level concept of various “sequence” classes, namely the built-in list, tuple, and str classes. There is significant commonality between these classes, most notably: each supports indexing to access an individual element of a sequence, using a syntax such as seq[k]
  * Although a list has a particular length when constructed, the class allows us to add elements to the list, with no               
  apparent limit on the overall capacity of the list. To provide this abstraction, Python relies on an algorithmic sleight of 
  hand known as a **dynamic array**.
       - **Implementation of dynamic array**
       
           1.Allocate a new array B with larger capacity.
           
           2.Set B[i] = A[i], for i = 0,...,n−1, where n denotes current number of items. 
           
           3.Set A = B, that is, we henceforth use B as the array supporting the list.
           
           4.Insert the new element in the new array.



* **Stack**: a collection of objects that are inserted and removed according to the last-in, first-out (LIFO) principle. Formally, a stack is an abstract data type (ADT) such that an instance S supports the following methods:
    - .push(item): Add element item to the top of stack.
    - .pop(): Remove and return the top element from the stack; an error occurs if the stack is empty.
    - .top(): Return a reference to the top element of stack, without removing it; an error occurs if the stack is empty.
    - .is_empty(): Return True if stack does not contain any elements.
    - len(Stack): Return the number of elements in stack.

______________________________________________________________________________________________________________________________
# Sorting Algorithms

* **Insertion sort**: the algorithm proceeds as follows for an array- based sequence. We start with the first element in the array. One element by itself is already sorted. Then we consider the next element in the array. If it is smaller than the first, we swap them. Next we consider the third element in the array. We swap it leftward until it is in its proper order with the first two elements. We then consider the fourth element, and swap it leftward until it is in the proper order with the first three. We continue in this manner with the fifth element, the sixth, and so on, until the whole array is sorted. 
