from pywinauto import Desktop, Application



def start_app(appName):
    app = Application(backend="uia").start(appName)

def start_app1(appName):
    app = Application().start(appName)
def app_connection(appTitle):
    if appTitle == 'Calculator':
        dlg = Desktop(backend="uia").Calculator
    if appTitle == 'Notepad':
            dlg = Application().connect(title_re=".*Notepad", class_name="Notepad")
    return dlg
def send_keys_strokes (dlg,keyTitle):
    dlg.type_keys(keyTitle)
    return dlg
def minimise_app (dlg):
    dlg.minimize()
    return dlg
def retore_app (dlg, appTitle):
    if appTitle == 'Calculator':
        Desktop(backend="uia").window(title='Calculator', visible_only=False).restore()
    return dlg
def close_app (dlg):
    dlg.type_keys('%{F4}')
    return dlg
def app_select_menu(dlg,titile,menu_options):
    dlg[titile].menu_select(menu_options)
def type_words(dlg,titile,words_type):
    dlg[titile].type_keys (words_type)
def click(dlg, titile, button_titile):
        dlg[titile][button_titile].click()