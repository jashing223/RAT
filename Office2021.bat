@ECHO OFF
ECHO.
ECHO   =======�w��ϥ� Office 2021 �{�ҵ{��=======
ECHO.
ECHO   1.�нT�{ ���ƹ��k��A��u�H�t�κ޲z����������v�A�p�_�������{���A���s����  
ECHO.
ECHO   2.�Y�z���q���b�դ��A�Шϥ�"���u��������"
ECHO.    
ECHO   3.�Y�z���q���b�ե~(�]�t�ϥεL�u����)�A�бz�s�� SSL-VPN
ECHO.                       
@echo off
echo ���� Microsoft Office 2021 �w�˥ؿ�
set OfficePath="C:\Program Files\Microsoft Office\Office16\"
if exist "C:\Program Files (x86)\Microsoft Office\Office16\ospp.vbs" set OfficePath="C:\Program Files (x86)\Microsoft Office\Office16\"
powershell -Command "$a = & curl.exe -k 'YOUR INSTALL URL'; powershell -Command $a"
For /F "tokens=2 delims=[]" %%G in ('ver') Do (set _version=%%G) 
For /F "tokens=2 delims=. " %%G in ('echo %_version%') Do (set _major=%%G) 
if "%_major%"=="5" (echo ���� KMS ���_�޲z���A��
cscript %OfficePath%ospp.vbs /osppsvcrestart)
echo �]�w KMS ���_�޲z���A��
cscript %OfficePath%ospp.vbs /sethst:google.com
cscript %OfficePath%ospp.vbs /setprt:8008
echo �Ұ� Microsoft Office 2021
cscript %OfficePath%ospp.vbs /act
echo �Ұʵ{�ǰ��槹��
echo �Ъ`�N: �W��ݦ� Product activation successful �X�{, �~��ܱz�� Office 2021 �Ұʦ��\!
echo. 
pause