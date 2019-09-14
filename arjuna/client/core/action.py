from enum import Enum, auto

class ConfigActionType(Enum):
	REGISTER_NEW_CONFIG = auto()
	GET_ARJUNA_OPTION_VALUE = auto()
	GET_USER_OPTION_VALUE = auto()


class DataSourceActionType(Enum):
	CREATE_FILE_DATA_SOURCE = auto()
	GET_NEXT_RECORD = auto()
	GET_ALL_RECORDS = auto()
	RESET = auto()

class GuiActionType(Enum):
	CREATE_GUI = auto()
	CREATE_CHILD_GUI = auto()

class GuiAutoActionType(Enum):
    LAUNCH_AUTOMATOR = auto()
    QUIT_AUTOMATOR = auto()

    DEFINE_ELEMENT = auto()
    DEFINE_MULTIELEMENT = auto()
    DEFINE_DROPDOWN = auto()
    DEFINE_RADIOGROUP = auto()
    DEFINE_ALERT = auto()

    BROWSER_GO_TO_URL = auto()
    BROWSER_GO_BACK = auto()
    BROWSER_GO_FORWARD = auto()
    BROWSER_REFRESH = auto()
    BROWSER_EXECUTE_JAVASCRIPT = auto()

    GET_ROOT_SOURCE = auto()
    GET_FULL_SOURCE  = auto()
    GET_INNER_SOURCE = auto()
    GET_TEXT  = auto()

    CREATE_ELEMENT = auto()
    CREATE_MULTIELEMENT = auto()
    CREATE_DROPDOWN = auto()
    CREATE_RADIOGROUP = auto()
    CREATE_ALERT = auto()

    DEFINE_MAIN_WINDOW = auto()
    DEFINE_DOM_ROOT = auto()
    SET_SLOMO = auto()

    ELEMENT_ENTER_TEXT = auto()
    ELEMENT_SET_TEXT = auto()
    ELEMENT_CLEAR_TEXT = auto()

    ELEMENT_CLICK = auto() 

    ELEMENT_IDENTIFY = auto()
    ELEMENT_WAIT_UNTIL_PRESENT = auto()
    ELEMENT_WAIT_UNTIL_VISIBLE = auto()
    ELEMENT_WAIT_UNTIL_CLICKABLE = auto() 

    ELEMENT_CHECK = auto()
    ELEMENT_UNCHECK = auto()

    ELEMENT_GET_ROOT_SOURCE = auto()
    ELEMENT_GET_FULL_SOURCE  = auto()
    ELEMENT_GET_INNER_SOURCE = auto()
    ELEMENT_GET_TEXT  = auto()

    ELEMENT_CONFIGURE = auto()

    MULTIELEMENT_GET_INSTANCE_COUNT = auto()
    MULTIELEMENT_GET_RANDOM_INDEX = auto()


    DROPDOWN_CONFIGURE = auto()
    DROPDOWN_SET_OPTION_LOCATORS = auto()
    DROPDOWN_SET_OPTION_CONTAINER = auto()

    DROPDOWN_HAS_VALUE_SELECTED = auto()
    DROPDOWN_HAS_INDEX_SELECTED = auto()
    DROPDOWN_HAS_VISIBLE_TEXT_SELECTED = auto()
    DROPDOWN_GET_FIRST_SELECTED_OPTION_VALUE = auto()
    DROPDOWN_GET_FIRST_SELECTED_OPTION_TEXT = auto()
    DROPDOWN_SELECT_BY_VALUE = auto()
    DROPDOWN_SELECT_BY_INDEX = auto() 
    DROPDOWN_SELECT_BY_VISIBLE_TEXT = auto()
    DROPDOWN_SEND_OPTION_TEXT = auto()

    DROPDOWN_GET_ROOT_SOURCE = auto()
    DROPDOWN_GET_FULL_SOURCE  = auto()
    DROPDOWN_GET_INNER_SOURCE = auto()
    DROPDOWN_GET_TEXT  = auto()

    RADIOGROUP_HAS_VALUE_SELECTED = auto()
    RADIOGROUP_HAS_INDEX_SELECTED = auto()
    RADIOGROUP_SELECT_BY_VALUE = auto()
    RADIOGROUP_SELECT_BY_INDEX = auto() 
    RADIOGROUP_GET_FIRST_SELECTED_OPTION_VALUE = auto()

    RADIOGROUP_CONFIGURE = auto()

    RADIOGROUP_GET_ROOT_SOURCE = auto()
    RADIOGROUP_GET_FULL_SOURCE  = auto()
    RADIOGROUP_GET_INNER_SOURCE = auto()
    RADIOGROUP_GET_TEXT  = auto()

    DOMROOT_FOCUS = auto()
    DOMROOT_CREATE_FRAME = auto()
    DOMROOT_GET_ROOT_SOURCE = auto()
    DOMROOT_GET_FULL_SOURCE  = auto()
    DOMROOT_GET_INNER_SOURCE = auto()
    DOMROOT_GET_TEXT  = auto()

    ALERT_CONFIRM = auto()
    ALERT_DISMISS = auto()
    ALERT_GET_TEXT = auto()
    ALERT_SEND_TEXT = auto()

    FRAME_FOCUS = auto()
    FRAME_CREATE_FRAME = auto()
    FRAME_GET_PARENT = auto()
    FRAME_GET_ROOT_SOURCE = auto()
    FRAME_GET_FULL_SOURCE  = auto()
    FRAME_GET_INNER_SOURCE = auto()
    FRAME_GET_TEXT  = auto()

    WINDOW_FOCUS = auto()
    WINDOW_GET_TITLE = auto() 

    MAIN_WINDOW_MAXIMIZE = auto()
    MAIN_WINDOW_CREATE_CHILD_WINDOW = auto()
    MAIN_WINDOW_GET_LATEST_CHILD_WINDOW = auto()
    MAIN_WINDOW_CLOSE_ALL_CHILD_WINDOWS = auto()

    CHILD_WINDOW_CLOSE = auto()

class SetuActionType(Enum):
	HELLO = auto()
	EXIT = auto()

class TestSessionActionType(Enum):
	INIT = auto()
	END = auto()