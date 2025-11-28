from config.settings import settings


class URL:    
    A_B_TESTING_PAGE = settings.BASE_URL + '/abtest'
    ADD_REMOVE_ELEMENTS = settings.BASE_URL + '/add_remove_elements/'
    BASIC_AUTH = settings.BASE_URL + '/basic_auth'
    BROKEN_IMAGES = settings.BASE_URL + '/broken_images'
    CHALLENGING_DOM = settings.BASE_URL + '/challenging_dom'
    CHECKBOXES = settings.BASE_URL + '/checkboxes'
    CONTEXT_MENU = settings.BASE_URL + '/context_menu'
    DIGEST_AUTHENTICATION = settings.BASE_URL + '/digest_auth'
    DISAPPEARING_ELEMENTS = settings.BASE_URL + '/disappearing_elements'
    DRAG_AND_DROP = settings.BASE_URL + '/drag_and_drop'
    DROPDOWN = settings.BASE_URL + '/dropdown'
    DYNAMIC_CONTENT = settings.BASE_URL + '/dynamic_content'
    DYNAMIC_CONTROLS = settings.BASE_URL + '/dynamic_controls'
    ENTRY_AD = settings.BASE_URL + '/entry_ad'
    
    EXPECTED_URLS = [
    settings.BASE_URL + '/abtest',
    settings.BASE_URL + '/add_remove_elements/',
    settings.BASE_URL + '/basic_auth',
    settings.BASE_URL + '/broken_images',
    settings.BASE_URL + '/challenging_dom',
    settings.BASE_URL + '/checkboxes',
    settings.BASE_URL + '/context_menu',
    settings.BASE_URL + '/digest_auth',
    settings.BASE_URL + '/disappearing_elements',
    settings.BASE_URL + '/drag_and_drop',
    settings.BASE_URL + '/dropdown',
    settings.BASE_URL + '/dynamic_content',
    settings.BASE_URL + '/dynamic_controls',
    settings.BASE_URL + '/dynamic_loading',
    settings.BASE_URL + '/entry_ad'
]