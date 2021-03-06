#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from selenium.webdriver.common.by import By

from pages.page import Page


class Paginator(Page):

    #Numbering
    _page_number_locator = (By.CSS_SELECTOR, 'nav.paginator .num >a:nth-child(1)')

    #Navigation
    _first_page_locator = (By.CSS_SELECTOR, 'nav.paginator .rel a:nth-child(1)')
    _prev_locator = (By.CSS_SELECTOR, 'nav.paginator .rel a.prev')
    _next_locator = (By.CSS_SELECTOR, 'nav.paginator .rel a.next')
    _last_page_locator = (By.CSS_SELECTOR, 'nav.paginator .rel a:nth-child(4)')

    #Position
    _start_item_number_locator = (By.CSS_SELECTOR, 'nav.paginator .pos b:nth-child(1)')
    _end_item_number_locator = (By.CSS_SELECTOR, 'nav.paginator .pos b:nth-child(2)')
    _total_item_number = (By.CSS_SELECTOR, 'nav.paginator .pos b:nth-child(3)')

    @property
    def page_number(self):
        return int(self.selenium.find_element(*self._page_number_locator).text)

    def click_first_page(self):
        self.selenium.find_element(*self._first_page_locator).click()

    def click_prev_page(self):
        self.selenium.find_element(*self._prev_locator).click()

    @property
    def is_prev_page_disabled(self):
        return 'disabled' in self.selenium.find_element(*self._prev_locator).get_attribute('class')

    def click_next_page(self):
        self.selenium.find_element(*self._next_locator).click()

    @property
    def is_next_page_disabled(self):
        return 'disabled' in self.selenium.find_element(*self._next_locator).get_attribute('class')

    def click_last_page(self):
        self.selenium.find_element(*self._last_page_locator).click()

    @property
    def start_item(self):
        return int(self.selenium.find_element(*self._start_item_number_locator).text)

    @property
    def end_item(self):
        return int(self.selenium.find_element(*self._end_item_number_locator).text)

    @property
    def total_items(self):
        return int(self.selenium.find_element(*self._total_item_number).text)
