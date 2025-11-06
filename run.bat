@echo off
setlocal
cd /d "%~dp0"

rem 使用无控制台的脚本宿主启动，避免黑框闪现
if exist "%SystemRoot%\System32\wscript.exe" (
  wscript //nologo run.vbs
) else (
  cscript //nologo run.vbs
)

exit /b
