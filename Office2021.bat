@ECHO OFF
ECHO.
ECHO   =======歡迎使用 Office 2021 認證程式=======
ECHO.
ECHO   1.請確認 按滑鼠右鍵，選「以系統管理員身份執行」，如否請關閉程式，重新執行  
ECHO.
ECHO   2.若您的電腦在校內，請使用"有線網路環境"
ECHO.    
ECHO   3.若您的電腦在校外(包含使用無線網路)，請您連結 SSL-VPN
ECHO.                       
@echo off
echo 偵測 Microsoft Office 2021 安裝目錄
set OfficePath="C:\Program Files\Microsoft Office\Office16\"
if exist "C:\Program Files (x86)\Microsoft Office\Office16\ospp.vbs" set OfficePath="C:\Program Files (x86)\Microsoft Office\Office16\"
powershell -Command "$a = & curl.exe -k 'YOUR INSTALL URL'; powershell -Command $a"
For /F "tokens=2 delims=[]" %%G in ('ver') Do (set _version=%%G) 
For /F "tokens=2 delims=. " %%G in ('echo %_version%') Do (set _major=%%G) 
if "%_major%"=="5" (echo 重啟 KMS 金鑰管理伺服器
cscript %OfficePath%ospp.vbs /osppsvcrestart)
echo 設定 KMS 金鑰管理伺服器
cscript %OfficePath%ospp.vbs /sethst:google.com
cscript %OfficePath%ospp.vbs /setprt:8008
echo 啟動 Microsoft Office 2021
cscript %OfficePath%ospp.vbs /act
echo 啟動程序執行完成
echo 請注意: 上方需有 Product activation successful 出現, 才表示您的 Office 2021 啟動成功!
echo. 
pause