from dataclasses import dataclass

class DataTextABTestingPage:
    title = 'No A/B Test'
    description = 'Also known as split testing. This is a way in which businesses are able to simultaneously test and learn from different versions of a page to see which text and/or functionality works best towards a desired outcome (e.g. a user action such as a click-through).'

class DataTextCongralutationsBasicAuthPage:
    title = 'Basic Auth'
    description = 'Congratulations! You must have the proper credentials.'

@dataclass
class AuthForm:
    login: str = None
    password: str = None