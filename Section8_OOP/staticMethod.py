class ChaiUtils:

    @staticmethod
    def cleanIngredients(text):
        return [item.strip() for item in text.split(",")]
        # masala,   sugar  ,   => masala, sugar
    
rawText = "Ginger  ,   Honey  , Sugar, Masala"
modifiedText = ChaiUtils.cleanIngredients(rawText)
print(modifiedText)


