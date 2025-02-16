# The script of the game goes in this file.

# Adding Dongle fonts



init python:
    # Set default font size
    gui.text_size = 40
    # Set default font color
    gui.text_color = "#ffffff"
    # Set default font
    gui.text_font = "fonts/Dongle-Regular.ttf"
    # Set default font size for buttons
    gui.button_text_size = 45
    # Set default font color for buttons
    gui.button_text_color = "#000"
    # Set default font for buttons
    gui.button_text_font = "fonts/Dongle-Regular.ttf"
    # Modify default line spacing
    gui.line_spacing = 0.2

    # Font Replacement Map
    config.font_replacement_map["Dongle-Regular.ttf", False, False] = ("fonts/Dongle-Regular.ttf", False, False)
    config.font_replacement_map["Dongle-Bold.ttf", True, False] = ("fonts/Dongle-Bold.ttf", True, False)
    config.font_replacement_map["Dongle-Light.ttf", False, False] = ("fonts/Dongle-Light.ttf", False, False)

    # Font Name Map
    config.font_name_map["dongle_regular"] = "fonts/Dongle-Regular.ttf"
    config.font_name_map["dongle_bold"] = "fonts/Dongle-Bold.ttf"
    config.font_name_map["dongle_light"] = "fonts/Dongle-Light.ttf"

define e = Character("Eileen")

# Main Characters
define merchant = Character("Merchant")
define son = Character("Son")
define daughter = Character("Daughter")

# Initialize inventory with maximum weight
default inventory = Inventory(max_weight=150)

# The game starts here.

label start:
    e "Welcome to the game!"
    show screen book_menu
    menu:
        "Go to Testing Screen":
            call screen testing_screen()
    return