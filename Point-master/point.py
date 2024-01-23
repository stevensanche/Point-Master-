"""
Name: Steven Sanchez-Jimenez
CS 211, Project: Point
January 11, 2023,
Resources: In-class tools
"""

import unittest
import test_point


class Point:
    """A point is a pair (x, y) denoting a point
    on the cartesion plane. We use integer coordinates.
    """
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, dx: int, dy: int):
        """Move to (x+dx, y+dy)"""
        self.x += dx
        self.y += dy

    def __eq__(self, other: "Point") -> bool:
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"







