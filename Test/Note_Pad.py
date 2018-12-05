from ScreenObjects.Reusable_Commands import start_app1,  app_select_menu, app_connection, type_words, click
import time
app = start_app1('notepad.exe')
time.sleep(1)
dlg= app_connection('Notepad')
type_words(dlg,'Untitled Notepad','Kushan {SPACE} Amarasiri')
app_select_menu(dlg,'Untitled Notepad',"File->Save As")
type_words(dlg,'Save As','kushan')
click(dlg,'Save As','Save')
app_select_menu(dlg,'kushan - Notepad',"File->Exit")
