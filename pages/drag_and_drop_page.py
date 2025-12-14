from pages.base_page import BasePage
from locators.drag_and_drop_page_locators import DragAndDropPageLocators
drag_and_drop_page_locators = DragAndDropPageLocators()


class DragAndDropPage(BasePage):
    
    
    def drag_and_drop_boxes(self):
        BOX_1 = self.find(drag_and_drop_page_locators.BOX_1)
        BOX_2 = self.find(drag_and_drop_page_locators.BOX_2)
        self.drag_and_drop(element_1=BOX_1, element_2=BOX_2)

    def drag_and_drop_by_offset_boxes(self):
        BOX_1 = self.find(drag_and_drop_page_locators.BOX_1)
        self.drag_and_drop_by_offset(element_1=BOX_1, x=100, y=50)

    def get_box_1_text(self):
        return self.find(drag_and_drop_page_locators.BOX_1_TITTLE).text
    
    def get_box_2_text(self):
        return self.find(drag_and_drop_page_locators.BOX_2_TITTLE).text