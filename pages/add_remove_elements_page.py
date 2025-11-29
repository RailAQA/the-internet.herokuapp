from pages.base_page import BasePage
from locators.add_remove_elements_page_locators import AddRemoveElementsPageLocators
from generator.generator import generated_count_clicks_to_add_button
ab_testing_page_locators = AddRemoveElementsPageLocators()


class AddRemoveElementsPage(BasePage):
    
    def click_add_button(self):
        count_clicks = generated_count_clicks_to_add_button()
        self.total = 0 # <- счетчик кликов по кнопке ADD
        for i in range(4, count_clicks + 1):
            self.total += 1
            self.click_to(ab_testing_page_locators.ADD_ELEMENTS_BUTTON_LOCATOR)

    def count_added_delete_buttons(self):
        return self.total
    
    def actual_count_delete_buttons(self):
        return len(self.finds(AddRemoveElementsPageLocators.DELETE_BUTTON_LOCATOR))

    def click_to_delete_button(self):
        self.total_deleted_button = 0  # <- счетчик кликов по кнопке Delete
        index = -1
        for i in range(1, 4):
            self.total_deleted_button += 1
            self.driver.find_elements(*AddRemoveElementsPageLocators.DELETE_BUTTON_LOCATOR)[index].click()
            index -= 1

    def count_deleted_delete_buttons(self):
        return self.total_deleted_button
    
    def actual_count_delete_after_deletion(self):
        return len(self.finds(AddRemoveElementsPageLocators.DELETE_BUTTON_LOCATOR))

    def delete_all_added_buttons(self):
        for i in range(self.total):
            self.click_to(AddRemoveElementsPageLocators.DELETE_BUTTON_LOCATOR)
