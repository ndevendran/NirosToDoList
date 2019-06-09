from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common.exceptions import WebDriverException
from unittest import skip
import time
import unittest
import os
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # An empty list item. She hits Enter on the empty input box
        # The home page refreshes, and there is an error message saying
        # That list items cannot be blank
        # She tries again with some text for the item, which now works
        # Perversely, she now decides to submit a second blank list item
        # And she can correct it by filling some text in
        self.fail('write me!') 




# Edith wonders whether the site will remember her list. Then she sees
# the site has generated a unique URL for her --
# there is some explanatory text to that effect.
# She visits that URL - her to-do list is still there
if __name__ == '__main__':
    unittest.main()