# selenium explicit wait

```
from selenium.webdriver.support.wait import WebdriverWait

from selenium.webdriver.suppport import expected_condition

ww=WebdriverWait(<driver obj>,<no_of_sec>)

ww.until(expected_condition.<all possible wait>(By.<locator>,"<value>"))

```

```
###### all_possible_wait are ########

- alert_is_present
- element_is_selected
- element_is_clickable
- new_window_opened
- element_located_to_be_selected
- presence_of_element_located
- presence_of_all_element_located
- NoAlertPresentException
- NoSuchElementException
- invisiblity_of_element
- invisibility_of_element_located

```
