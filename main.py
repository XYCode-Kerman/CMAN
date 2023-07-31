import config

if config.UI == config.enums.UserInterfaceDisplay.Command_User_Interface:
    import ui.cui as ui
elif config.UI == config.enums.UserInterfaceDisplay.Graphics_User_Interface:
    import ui.gui as ui

if __name__ == '__main__':
    ui.init()