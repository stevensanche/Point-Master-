# Point project HOWTO

## HOWTO documents in CIS 211 

The repository for each project in CIS 211 will include 
a doc directory (folder) with at least one HOWTO file.  
The HOWTO document contains detailed instructions for 
completing the project.  

These documents will be in 
*markdown* format, e.g., HOWTO-point.md is a HOWTO document
for the *Point* project in markdown format.  You can install 
markdown support in PyCharm to read and edit markdown files. 
Many external editors also support markdown. 

The *doc* directory may contain additional reading that 
you should complete before you begin working on the project, 
and which you may wish to refer back to.  Some of this 
reading should be done before class, and you will be 
asked to answer questions about it in class.  The HOWTO 
document will indicate the order of reading.

## Incremental procedure

The Point project is an introduction to classes 
and objects in Python, and at the same time an 
introduction to the style of incremental 
development and testing we will use in CIS 211. 
In subsequent projects the HOWTO document will provide 
test cases for you (and occasionally require you to 
devise some of your own), and you will build up a test
program like `test_point.py` in tandem with building 
project code in one or more files like `point.py`.  In 
this and some other mini-projects, the test program 
is provided for you, and you will build only 
`point.py`.  

You should create file point.py one step at a time, 
testing after each step. To test, run test_point.py. 
Initially, all the tests will fail, because you 
haven't written code to pass the tests. After each test, 
another test should succeed.

When all the tests succeed, you will see 
something like this:

```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```

But that's not what you'll see at first! 
Initially all the test cases will fail because 
you haven't created the code to be tested:.

```
Traceback (most recent call last):
  File "/Users/michal/Dropbox/19W-211/projects/geometry/test_point.py", line 31, in 
    import point
ModuleNotFoundError: No module named 'point'
```
                
When you create file point.py, you'll get past this 
first error but enounter several failed test cases:

```
.E.FF
======================================================================
ERROR: test_move_point (__main__.T1_CanMovePoint)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/michal/Dropbox/19W-211/projects/geometry/test_point.py", line 48, in test_move_point
    pt.move(17,38)
AttributeError: 'Point' object has no attribute 'move'

======================================================================
FAIL: test_identical_points_are_equal (__main__.T2_EqualMeansIdentical)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/michal/Dropbox/19W-211/projects/geometry/test_point.py", line 60, in test_identical_points_are_equal
    self.assertEqual(p1, p2)
AssertionError:  != 

======================================================================
FAIL: test_pt_str (__main__.T3_string_rep)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/michal/Dropbox/19W-211/projects/geometry/test_point.py", line 77, in test_pt_str
    self.assertEqual(pt_str, "(18, 34)")
AssertionError: '' != '(18, 34)'
- 
+ (18, 34)
```

The first line, `..E.FF`, shows that the third 
test case executed had an error (E) and the fifth 
and sixth test cases failed. An “error” means the 
test case was not able to run at all, and in this 
case we can see from the messages that it tried 
to call a method move that hasn't been written yet. 
A “failure” is a test case that executed but did 
not satisfy the condition specified in an assertion. 
You can see that one of these failures is in the way 
two Point objects are tested for equality.

As you make progress on this mini-project, 
which each successful step you will be able 
to make more and more of the test cases succeed.

## Background

Before proceeding to the detailed steps for 
the point mini-project, read `Background-point.md`.
Refer to it as needed while completing the project. 

## Steps

* Create file point.py. 
* Create class Point, with a constructor (initializer) 
 method that takes two integers, `x` and `y`, and stores 
 them as instance variables `self.x` and `self.y`. 
 When you have completed this step, 
 test case `T0_CanConstructPoint` should succeed.
* Add a method move that takes two integer arguments, 
 `dx` and `dy`. This method should increase `self.x` 
 by `dx` and increase `self.y` by `dy`. 
 (If `dx` or `dy` are negative, the result will be 
 decreasing `self.x` and/or `self.y`.) 
 When you have completed this step, test case 
 `T1_CanMovePoint` should succeed.
* Now test case `T2_EqualMeansIdentical` will be 
  failing because the default meaning of `==`. 
  You can fix this by creating a method with the 
  special name `__eq__` which takes, in addition 
  to `self`, another *Point* object. 
  This method should return a boolean. 
  If the `x` and `y` fields of the self object 
  and the other Point object are equal, 
  `__eq__` should return `True`, and otherwise it
   should return `False`.
* Now  you have defined Point objects that can be created, 
  moved, and compared for equality. 
  But if you print a Point object, you will get a fairly 
  unfriendly representation like 
 `<point.Point object at 0x10b8aabe0>`. 
  Test case `T3_string_rep` expects the string 
  representation of a *Point* object with 
  `x` component 10 and `y` component 12 to look 
  like `(10, 12)`. To accomplish this, you will 
  define another special method 
  called `__str__`. The `__str__` method takes only 
  the self object as an argument, and it returns 
  the preferred string representation of that object. 
  There are many ways you can produce this string, 
  but I suggest using the new f-string facility in 
  recent versions of Python, e.g., 
  `f"({self.x}, {self.y})"`.
  
 When you have completed these steps, all the test 
 cases should succeed. Note that this is not an 
 ironclad guarantee that your code is correct. 
 We will use a few more tests, which we do not share 
 with you, in grading. Our extra tests help ensure 
 that you are really solving the problem and not 
 taking short cuts that provide correct results only 
 for the known tests. 

