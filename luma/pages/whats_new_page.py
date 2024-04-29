from selene.support.conditions import have, be

from luma.locators.whats_new_page_locators import WhatsNewPageLocators
from luma.pages.base_page import BasePage


class WhatsNewPage(BasePage):
    locators = WhatsNewPageLocators()

    def is_element_text_correct(self, element, text):
        return element.should(have.text(text))

    def is_header_present(self):
        return self.find_element(self.locators.HEADER).should(be.present)
