On Error Resume Next
Set shell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

' 切到脚本所在目录
cd = fso.GetParentFolderName(WScript.ScriptFullName)
shell.CurrentDirectory = cd

' 依次检测并使用 pyw / pythonw / py / python
If shell.Run("cmd /c where pyw >nul 2>nul", 0, True) = 0 Then
  shell.Run "pyw -3 love_popup.py", 0, False
  WScript.Quit 0
End If

If shell.Run("cmd /c where pythonw >nul 2>nul", 0, True) = 0 Then
  shell.Run "pythonw love_popup.py", 0, False
  WScript.Quit 0
End If

If shell.Run("cmd /c where py >nul 2>nul", 0, True) = 0 Then
  shell.Run "py -3 love_popup.py", 0, False
  WScript.Quit 0
End If

If shell.Run("cmd /c where python >nul 2>nul", 0, True) = 0 Then
  shell.Run "python love_popup.py", 0, False
  WScript.Quit 0
End If

MsgBox "未找到 Python，请先安装 Python 3。", vbExclamation, "启动失败"
