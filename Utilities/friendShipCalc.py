def calculateFriendship(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    
    score = 0

    LETTER_FACTOR = 20
    VOWEL_FACTOR = 25

    # Intersection of 2 sets, set function creates sets from iterables
    commonLetters = set(name1) & set(name2)
    vowels = ["a", "e", "i", "o", "u"]
    vowelScore = 0
    for letter in commonLetters:
        if letter in vowels:
            vowelScore += 1
    
    # Adding score for common letters
    score += (len(commonLetters) * LETTER_FACTOR)
    # Adding score for common vowels
    score += (vowelScore * VOWEL_FACTOR)

    # Same name
    if name1 == name2:
        return 100
    
    if score > 100:
        return min(score, 100)
    else:
        return score


def giveRemarks(score):
    if score >= 80:
        return f"🥰 You guys are made for each other !"
    elif score >= 50 and score < 80:
        return f"🧐 Hmm.. you seem to get along pretty well !"
    elif score < 50:
        return f"😏 Opposites attract you know na !"


def runApp():
    print()
    print("-"*8 + "🩷🩷\tFriendship Score Calculator\t🩷🩷" + "-"*8)
    name1 = input("Enter 1st friend name: ")
    name2 = input("Enter 2nd friend name: ")
    score = calculateFriendship(name1, name2)
    print(f"Your friendship score is {score} !")
    remarks = giveRemarks(score)
    print(remarks)

runApp()

