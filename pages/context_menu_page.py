from pages.base_page import BasePage
from locators.context_menu_page_locators import ContextMenuPageLocators
home_page_locators = ContextMenuPageLocators()



class ContextMenuPage(BasePage):
    
    def right_click_on_box(self):
        self.action_right_click(ContextMenuPageLocators.BOX)

    def right_click_on_empty_space(self):
        self.action_right_click(ContextMenuPageLocators.EMPTY_SPACE)

    def left_click_on_box(self):
        self.action_left_click(ContextMenuPageLocators.BOX)