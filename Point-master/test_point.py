"""
This is a set of "unit tests" for the file point.py, which
you will write.  We will use this style of testing extensively
in CIS 211.  You should use the provided unit tests to check
your progress frequently as you work through a project.

If you work for an hour or more writing code without testing it,
you are doing it wrong.  Code a little, test a little.
Always.

Writing test cases before you write the code to be tested is
part of a method called "test-driven development", or "TDD".
It is widely used in industry.  You should practice not only
using pre-written tests to gauge your progress, but also
writing your own test cases as part of your planning.  In
larger projects it is especially important to be able to
gauge your progress at intervals, and testability becomes
an important heuristic for devising an overall system
design and development plan.

Overall design and planning is an advanced skill, and I don't
expect you to become expert in it overnight, but now is the
time to start learning.  Find a path through your development
that enables you to test at each step along the way, even if
it requires you to write some "scaffolding" code and
experimental code that will not be part of
the finished project.
"""

import unittest
import point


class T0_CanConstructPoint(unittest.TestCase):
    """This test should pass when you have defined the
    Point class with an __init__ method that initializes
    its x and y instance variables.
    """
    def test_build_a_point(self):
        pt = point.Point(42,89)
        self.assertEqual(pt.x, 42)
        self.assertEqual(pt.y, 89)

class T1_CanMovePoint(unittest.TestCase):
    """The 'move' method modifies the coordinates of a point."""
    def test_move_point(self):
        pt = point.Point(13,22)
        pt.move(17,38)
        self.assertEqual(pt.x, 30)
        self.assertEqual(pt.y, 60)

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

class T3_string_rep(unittest.TestCase):
    """A point should have a nice string representation
    as (x, y).
    """
    def test_pt_str(self):
        pt = point.Point(18, 34)
        pt_str = str(pt)
        self.assertEqual(pt_str, "(18, 34)")


if __name__ == '__main__':
    unittest.main()
