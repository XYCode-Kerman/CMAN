from enum import Enum, auto

class UserInterfaceDisplay(Enum):
    """User Interface Display Enum"""
    Graphics_User_Interface = 'GUI'
    Command_User_Interface = 'CUI'

class Language(Enum):
    """Language Enum"""
    EnglishUnitedStates = 'en_us'
    SimpleChinese = 'zh_cn'
    # TraditionalChinese = 'zh_tw'