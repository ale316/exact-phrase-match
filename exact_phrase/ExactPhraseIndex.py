from PhraseTree import *

class ExactPhraseIndex:
    def __init__(self, phrases):
        self.phrase_tree = PhraseTree(phrases)

    def _find_matches(self, tokens):
        phrase = []
        result = []

        while tokens or phrase:
            if phrase:
                has_phrase = self.phrase_tree.has(phrase)

                if has_phrase == 1:
                    result.append(' '.join(phrase))
                    phrase.append(tokens.pop(0))
                elif has_phrase == -1:
                    phrase.pop(0)
                elif has_phrase == 0 and tokens:
                    phrase.append(tokens.pop(0))
            else:
                phrase.append(tokens.pop(0))

        return result

    def matches(self, text):
        tokens = text.lower().split(' ')
        return self._find_matches(tokens)
