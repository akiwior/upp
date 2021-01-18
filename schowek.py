from win32clipboard import *

OpenClipboard()
schowek = str(GetClipboardData())
CloseClipboard()
print(schowek)