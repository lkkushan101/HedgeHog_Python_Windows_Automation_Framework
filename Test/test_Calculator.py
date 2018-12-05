from ScreenObjects.Reusable_Commands import start_app, send_keys_strokes, app_connection, minimise_app, retore_app, close_app
import time

start_app('calc.exe')
time.sleep(1)
dlg = app_connection('Calculator')
dlg = send_keys_strokes(dlg, '3')
time.sleep(1)
dlg = send_keys_strokes(dlg, '*')
time.sleep(1)
dlg = send_keys_strokes(dlg, '4')
time.sleep(1)
dlg = send_keys_strokes(dlg, '=')

dlg = minimise_app(dlg)
dlg = retore_app(dlg,'Calculator')
time.sleep(4)
dlg - close_app(dlg)