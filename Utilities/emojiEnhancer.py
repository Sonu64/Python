emojiMap = {
    "love": "❤️",
    "happy": "😊",
    "code": "💻",
    "tea": "🍵",
    "music": "🎵",
    "food": "🍕",
}

keys = emojiMap.keys()

text = input("Enter your text: ");
text = text.split()
newWords = []
newSentence = ""

for word in text:
    if word in keys or word.lower() in keys:
        newWords.append(word + emojiMap[word.lower()] + " ")
    else: 
        newWords.append(word)
print(newWords)

# convert list to string
newSentence = " ".join(newWords)
print(newSentence)

