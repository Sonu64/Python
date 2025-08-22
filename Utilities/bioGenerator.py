name = input("Name: ").strip()
profession = input("Profession: ").strip()
passion = input("One-Liner Passion or Goal: ").strip()
favEmoji = input("Favorite Emoji: ").strip()
website = input("Website or Handle: ").strip()

print("\nChoose a Bio Style: ")
print("1. Simple Lines")
print("2. Vertical Flair")
print("3. Emoji Sandwich")

style = 0
while style != 1 and style != 2 and style != 3:
    style = int(input("Enter style number: "))

def generateBio(style):
    if style==1:
        if website:
            return f"{favEmoji} {name}  | 💡 {profession}\n 🚀 {passion}\n🌎 {website}"
        else: 
            return f"{favEmoji} {name}  | 💡 {profession}\n 🚀 {passion}"
    elif style==2:
        if website:
            return f"{favEmoji} {name}  | ⚡️ {profession}\n🔥 {passion}\n🌎 {website}"
        else:
            return f"{favEmoji} {name}  | ⚡️ {profession}\n🔥 {passion}"
    elif style==3:
        if website:
             return f"{favEmoji*10}\n {name}  | 💡 {profession}\n🚀 {passion}\n🌎 {website}\n{favEmoji*10}"
        else:
            return  f"{favEmoji*10}\n{name}  | 💡 {profession}\n {passion}\n{favEmoji*10}"          

bio = generateBio(style)
print("*"*50)
print(bio)
print("*"*50)

choice = input("Do you want to save this into a file ? (y/n): ").lower()
while choice != "y" and choice != "n":
    choice = input("Please enter a valid choice ? (y/n): ").lower()

if (choice == "y"):
    filename = f"{name.lower().replace(" ", "_")}_bio.txt"
    with open(filename, "w", encoding = "utf-8") as file:
        file.write(bio)
    print("File Saved ! \n Goodbye !")
else:
    print("Goodbye !")