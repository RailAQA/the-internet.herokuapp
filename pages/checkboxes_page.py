from pages.base_page import BasePage
from locators.checkboxes_page_locators import CheckboxesPageLocators
from generator.generator import generated_random_checkbox
home_page_locators = CheckboxesPageLocators()



class CheckboxesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.CHECKBOX = generated_random_checkbox()
    
    
    def check_checkboxes_not_active(self):
        total = 0
        LIST_CHECKBOXES = self.finds(CheckboxesPageLocators.LIST_CHECKBOXES)
        for i in range(len(LIST_CHECKBOXES)):
            if LIST_CHECKBOXES[i].get_attribute('checked') is not None:
                total += 1
        if total:
            return False
        else:
            return True
                
    def click_to_checkbox(self):
        
        if self.find(self.CHECKBOX).get_attribute('checked') is not None:
            self.click_to(self.CHECKBOX)
        self.click_to(self.CHECKBOX)

    def disable_checkbox(self):
        self.click_to(self.CHECKBOX)
        
    def checkbox_is_active(self):
        if self.find(self.CHECKBOX).get_attribute('checked') is not None:
            return True
        else:
            return False
        
    def checkbox_disable(self):
        not self.checkbox_is_active()