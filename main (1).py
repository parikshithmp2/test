import re

def cleanme(text):
    
    cleaned_text = re.sub(r"[^a-zA-z0-9\s]", "", text)
    return cleaned_text.upper()
    
print(cleanme("Ban'glore'"))
print(cleanme("Are you 28 now?"))