import win32gui

def get_full_window():
    w = win32gui
    return w.GetWindowText(w.GetForegroundWindow())

def beautify_window_name(window_name):
    # split window text by dashes, often the norm.
    window_name_list = window_name.split(" - ", 1)

    window_dict = {}
    try:
        window_dict['primary'] = window_name_list[-1]
        window_dict['secondary'] = window_name_list[-2]
        window_dict['full'] = window_name
    except IndexError:
        pass
    
    return window_dict