import webbrowser

# webbrowser.open("https://www.google.com")
chrome = webbrowser.get(using='windows-default')
chrome.open_new("https://www.python.org")
