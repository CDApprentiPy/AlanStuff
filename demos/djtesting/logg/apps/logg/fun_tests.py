# Functional Tests! wewt!
from selenium import webdriver


# configs-y-things
browser = webdriver.Chrome('/somethings/chromedriver.exe')

# User goes to '/' and sees login and register forms
browser.get('http://localhose:8000')
assert "logreg yo!" in broswer.title
# User can register with validations

# User can login