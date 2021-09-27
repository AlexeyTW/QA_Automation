import time, math, os, unittest


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_abs1():
	assert abs(-42) == 42, 'Assertion 1'

def test_abs2():
	assert abs(-42) == -42, 'Assertion 2'