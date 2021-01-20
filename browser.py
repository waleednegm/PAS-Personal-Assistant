import webbrowser

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
def open_web_com(website):
    webbrowser.get(chrome_path).open_new_tab(website+".com")

