from pages.base_page import BasePage
from locators.drag_and_drop_page_locators import DragAndDropPageLocators
drag_and_drop_page_locators = DragAndDropPageLocators()


class DragAndDropPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)