# Background for the Pont mini-project 

You should read this *before* working through the Point 
mini-project. You may be quizzed about these concepts in 
lecture. 

## Main concepts 

The main concepts you need to understand to finish the 
Pont mini-project are

* Classes:  This is how we create new data types in Python
* Objects: Data values are objects.  Each object 
  is an *instance* of a class. 
* Test cases:  A test case is code that checks other 
  code by executing it. 
*  Test suites:  A test suite is a collection of test 
  cases.  In CIS 211, our test suites will be Python 
  files like `test_point.py`. 
  
## Classes and Objects

A class is how we create new data types in Python.  
The data types you are already familiar with, 
like *int* and *list*, are also classes. Individual 
values that belong to a class are called *objects*.  

In the Point project you will build a class to 
represent points as (x,y) pairs 
in a Cartesian coordinate system.  

### Methods 

The operations we can perform on an object are 
called the *methods* of the class.  They are similar to 
functions except that they are defined within a class, and 
they always take the object as the first argument.
For example, `append` is a *method* of class *list*. 
When we write `l.append(x)`, if `l` is an object with 
class `list`, we actually call `list.append(l,x)`.  

In this project you will define a class `Point` 
with a method `move`.  You will define `move` like a 
function within the Point class, e.g., 

```python
class Point:
    """A Point is a pair (x,y) denoting a point
    on the cartesion plane.  We use integer coordinates.
    """
    
    # ... 
    def move(self, dx: int, dy: int):
        """Move to (x+dx, y+dy)"""
        # ... 
```

You should never write `Point.move(pt, 3, 5)`.  You should 
always use *method dispatch* to call the `move` method, 
e.g., `pt.move(3, 5)`.  Using method dispatch allows us 
to make use of *polymorphism* in which we may 
call `pt.move(3,5)` without knowing or caring whether 
`pt` is a *Point* object or some more specialized kind of 
object that also provides a `move` method.  We'll make 
extensive use of polymorphism in subsequent projects. 

### Magic methods 

I said that the operations we can perform on objects 
are called *methods*, but you have been using operations 
like `+` and `*` on objects of class *int*.  `+` 
doesn't look like a method call, but actually it is.  

Python lets  you write `z * x + y` 
instead of the less readable 
`z.__mul__(x.__add__(y))`.  It simply interprets 
`a * b` as `a.__mul__(b)`, for any expressions *a* and 
*b*, and likewise interprets `a + b` as `a.__add__(b)`. 
Methods like `__add__` and `__mul__` are officially 
termed *special methods*, but everyone calls them 
*magic methods*, perhaps because it's such a 
neat trick it's almost magic. 

You will create two magic methods for *Point* objects 
in this mini-projects.  The `==` operation, which 
compares two objects for equality, is implemented 
by a magic method `__eq__`.  You'll write an `__eq__` 
method to determine whether two *Point* objects have 
the same `x` and `y` coordinates.  The second 
magic method you'll write is `__str__`, which is 
called when we print an object.  

### Constructors 

Every class has a magic method `__init__` that 
describes how to create an object of that class. 
These are called *constructors* because they describe 
how we *construct* a value for some new kind of object 
from values of other, known types.  For the Point 
mini-project, you'll create a *constructor* `__init__`
that creates a *Point* object from two *int* values, 
the x and y coordinate of the *Point*.  

### Self

In methods, we refer to the current object as `self`. 
These values will be initially set in a particular 
object by the constructor.  For example, the `__init__` 
method of `Point` will save the x and y coordinate 
in `self.x` and `self.y`, respectively.  The `move` 
method will be able to access or modify those values 
by referring to `self.x` and `self.y`.   

## Test Cases 

We will use test cases to check each part of the code 
as we write it.  Our test cases will  be Python code. 
For example, after we have written the magic `__eq__`
method for the *Point* class, we can check it with 
a pair of test cases:  One to make sure that it returns 
`True` when points do have the same `x` and `y` 
parts, and one to make sure that it returns `False` 
when they don't. 

You will not be required to write test cases in this 
mini-project, but later in the term you will.  Here is 
what two test cases for the `__eq__` magic method look like: 

```python
class T2_EqualMeansIdentical(unittest.TestCase):
    """The __eq__ method of Point should equate
    Point objects that have the same x and y
    cooredinates.
    """
    def test_identical_points_are_equal(self):
        p1 = point.Point(7, 12)
        p2 = point.Point(7, 12)
        self.assertEqual(p1, p2)

    def test_different_points_arent_equal(self):
        p1 = point.Point(9,13)
        p2 = point.Point(9,20)
        p3 = point.Point(10,13)
        self.assertNotEqual(p1, p2)
        self.assertNotEqual(p1, p3)
        self.assertNotEqual(p2, p3)
```

As you can see, test cases make use of classes and 
objects in Python.  They also make use of 
*inheritance*, which you will encounter very soon. 
I have provided the test 
case code for you so that you can use them 
before you understand inheritance. 

## Test Suites 

A test suite is just a collection of test cases. 
In this mini-project, file `test_point.py` is 
a test suite. 

The key feature of a test suite like `test_point.py` is 
that it is just a program that we can execute easily 
and as often as we wish.  This is essential to 
incremental development of complex software systems. 
In fact, a common practice called *test driven 
development* or *TDD* is to write test cases for a new 
software feature *before* writing code to implement 
that feature.  In TDD, test cases are used as a kind of
specification and to-do list for software under 
development.  Passing all the test cases does not 
guarantee the code is correct, as it is generally 
impossible to write a test suite that catches all 
possible errors, but a good test suite
makes a very useful gauge of 
progress as well as a simple, effective check to 
make sure we haven't broken that code when we 
enhance it later. 

## Bonus aside: Why test suites are never perfect

When I say "it is generally impossible to write 
a test suite that catches all possible errors",
I really mean it.  In fact, I can prove it as a 
simple corollary to Alan Turing's proof that the
*halting problem* is undecidable (which is a close 
cousin to Gödel's incompleteness theorem).  

One of the two gargoyles
on the south side of the computer science building, 
Deschutes Hall, is of Alan Turing.  
