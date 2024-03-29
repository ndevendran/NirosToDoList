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
        self.browser.get(self.live_server_url)

        self.get_item_input_box().send_keys(Keys.ENTER)
        # The browser intercepts the request, and does not load
        # The list page
        self.wait_for(lambda: self.browser.find_elements_by_css_selector('#id_text:invalid'))

        # She starts typing some text for the new item and the error disappears
        self.get_item_input_box().send_keys('Buy milk')
        self.wait_for(lambda: self.browser.find_elements_by_css_selector(
                '#id_text:valid'
            ))

        # And she can submit it successfully
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Perversely, she now decides to submit a second
        # blank list item
        self.get_item_input_box().send_keys(Keys.ENTER)

        # Again, the browser will not comply
        self.wait_for_row_in_list_table('1: Buy milk')

        self.wait_for(lambda: self.browser.find_elements_by_css_selector(
                '#id_text:invalid'
            ))

        # And she can correct it by filling some text in
        self.get_item_input_box().send_keys('Make tea')

        self.wait_for(lambda: self.browser.find_elements_by_css_selector(
                '#id_text:valid'
            ))

        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')
        self.fail('write me!')
    




# Edith wonders whether the site will remember her list. Then she sees
# the site has generated a unique URL for her --
# there is some explanatory text to that effect.
# She visits that URL - her to-do list is still there
if __name__ == '__main__':
    unittest.main()