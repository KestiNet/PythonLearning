#!/usr/bin/env python3

from reaarange import rearrange_name
import unittest

class TestRearange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        excepted = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), excepted)