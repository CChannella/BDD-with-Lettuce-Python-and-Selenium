from lettuce import before, world,after
from selenium import webdriver

@before.all
def setup_browser():
  world.browser = webdriver.Firefox()

@after.all
def tear_down(total):
      print "Total %d of %d scenarios passed!" % ( total.scenarios_ran, total.scenarios_passed)
      world.browser.quit()