#strip(), lstrip() and rstrip()

# strip()

text = " Hello World  "
print(text.strip())       #Output: "Hello World"
print(text.lstrip())      #Output: "Hello World "   
print(text.rstrip())      #Output: " Hello World"

# example 
url = "https://www.praveen.com/"
print(url.strip("https:/"))