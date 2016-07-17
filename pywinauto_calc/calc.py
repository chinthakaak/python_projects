# from __future__ import unicode_literals
# from __future__ import print_function

# from pywinauto import application
# from pywinauto.application import Application
# app = Application().start("calc.exe")

# app.Caculator.print_control_identifiers()
# app.Caculator.Button5.ClickInput();




from __future__ import unicode_literals
from __future__ import print_function

from pywinauto import application
from pywinauto.application import Application
app = Application().start(r"D:\data\software\control-panel-sw\control-panel-sw\bin\Xpanel64.exe")
win = app.window_(title_re = ".*XPanel")
win.print_control_identifiers();

win.MenuSelect("Help->About")
app.dialogs.print_control_identifiers();
# win.Dialog.About.OK.Click();

# app.Caculator.print_control_identifiers()
# app.Caculator.Button5.ClickInput();