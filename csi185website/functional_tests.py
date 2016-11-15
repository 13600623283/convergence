# My computer history web site as an example

# Boiler Plate


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import os

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        if os.name=='nt':
            self.browser = webdriver.Chrome()
        else:
            self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()


    #####################
    # END OF BOILER PLATE
    #####################

    def test_home_page(self):
        """

        The character Sherlock Holmes in the movie The Abominable Bride
        exhibits behavior that leads to the convergence of 21st century
        emotionalism and Victorian rationalism. This project situates this
        convergence within a psychological perspective saying that emotions
        are judgments. And this convergence is symptomatic of the reality as
        well.

        """

        self.browser.get('http://localhost:8000/index.html')

        # there is a page title defined by <title></title> on the home page
        # check it

        self.assertIn('Convergence of Emotionalism and Rationalism',self.browser.title)

        # You will have an image for your home page I am assuming.
        # Put the name of your image here in place of homebrew.png
        # In general this is how we check for images on a page.

        # The user sees a image of bridge.

        m=self.browser.find_element_by_tag_name('img')
        self.assertIn('connection.jpg',m.get_attribute('src'))

        # We check here for the title of your home page.
        # uncomment the next lines and change the text when you set your title.
        # put your title in place of "The Title of My Home Page"

        h=self.browser.find_element_by_css_selector('h1')
        self.assertIn("Convergence of Emotionalism and Rationalism",h.text)

        a=self.browser.find_element_by_id("principle")
        a.click()

        self.assertIn('principle', self.browser.title)


if __name__=="__main__":
        unittest.main(warnings="ignore")
