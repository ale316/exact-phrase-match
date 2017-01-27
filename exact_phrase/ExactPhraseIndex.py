class ExactPhraseIndex:
    def __init__(self, phrases):
        self.phrase_tree = PhraseTree(phrases)

    def _match(self, tokens, phrase, result = []):
        if not tokens:
            return result
        elif 

    def match(self, text):
        tokens = text.split(' ')
