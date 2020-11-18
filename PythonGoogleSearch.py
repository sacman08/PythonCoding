from selenium import webdriver

# get search input
search_string = input("Input the URL or string to search for:")

#reformat spaces for searching
search_string = search_string.replace(' ', '+')

#Create the web browser to search
browser = webdriver.Chrome("{Path to chromedriver.exe}")

for i in range(1):
    matched_results = browser.get("https://www.google.com/search?q=" + search_string + "&start=" +str(i))
