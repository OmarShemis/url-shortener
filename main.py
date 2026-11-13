import pyshorteners

url = input("Enter URL: ")
output = pyshorteners.Shortener().tinyurl.short(url)
print(output)