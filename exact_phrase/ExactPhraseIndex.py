from PhraseTree import *

class ExactPhraseIndex:
    def __init__(self, phrases):
        self.phrase_tree = PhraseTree(phrases)

    def _find_matches(self, tokens, phrase = [], result = []):
        if not tokens and not phrase:
            return result
        elif phrase:
            has_phrase = self.phrase_tree.has(phrase)

            if has_phrase == 1:
                result.append(' '.join(phrase))
                phrase.pop(0)
            elif has_phrase == -1:
                phrase.pop(0)
            elif has_phrase == 0 and tokens:
                phrase.append(tokens.pop(0))
        else:
            phrase.append(tokens.pop(0))

        return self._find_matches(tokens, phrase, result)

    def matches(self, text):
        tokens = text.lower().split(' ')
        return self._find_matches(tokens)

idx = ExactPhraseIndex([
        "I am a pony",
        "I am a human child",
        "I am now a baby",
        "I am not your type",
        "a baby boy"
    ])

print idx.matches("Hi my name is george I am not a pony but I am a human I am now a baby and a baby boy")