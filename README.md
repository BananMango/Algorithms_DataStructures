# Algorithms_DataStructures
**Python** is a dynamically typed language, as there is no advance declaration associating an identifier with a particular data type. Built-in classes can be divided into mutable and immutable(A class is immutable if each object of that class has a fixed value upon instantiation that cannot subsequently be changed). Mutable classes are: list, set, dict; And immutable: bool, int, float, tuple, str.

* **Bool** class is used to manipulate logic values, and the only two instances of that class are expressed as the literals True and False (default constructor bool(), returns False)
* **Int** class is primary numeric type in Python. The integer constructor int() returns 0 by default. 
* **Float** class is second primary numeric type in Python and is the sole floating-point type. The float constructor returns 0.0 by default
* **List** class is sequence class in Python that stores a sequence of object. It is a referential structure as it stores a sequence of references to its elements. Lists have valuable behaviors, including the ability to dynamically expand and contract their capacities as needed. Python uses [] to delimit a list.
* **Tuple** class is second sequence class in Python, unlike list it is immutable. Python uses () to initialize a tuple.
* **Str** class is third sequence class in Python that is designed to efficiently represent an immutable sequence of characters.
* **Set** class represents the mathematical notion of a set, namely a collection of elements, without duplicates, and without an inherent order to those elements. The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set.This is based on a data structure known as a hash table. However, there are two important restrictions due to the algorithmic underpinnings. The first is that the set does not maintain the elements in any particular order. The second is that only instances of immutable types can be added to a Python set. **Frozenset** class is an immutable form of the set type, so it is legal to have a set of frozensets.
* **Dict** class represents a dictionary, or mapping, from a set of distinct keys to associated values.

* **Stack**: implemented using Python list with space usage of O(n) and running time of all operations of O(1)

