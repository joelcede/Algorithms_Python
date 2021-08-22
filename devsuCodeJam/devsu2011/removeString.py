# Given two strings S1 and S2. Delete from S1 all those characters which occur in S2. 
# Returna clean S1 with the relevant characters deleted. 
# Any character deletes both uppercase andlowercase.

def delLetters(s: str, t: str) -> str:
    messageN: str = ""
    for i in s:
        if i.lower() not in t.lower():
            messageN += i
    return messageN

print(delLetters("DevsuCodeJam is just great!", "I am here! :)"))
