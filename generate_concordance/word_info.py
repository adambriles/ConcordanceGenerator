from typing import List


class WordInfo:
    """
    A class to hold how many times a word has appeared in a text string, and in which sentences a word appeared.

    Attributes
    ----------
    word_frequency : int
        The number of times a word has appeared in user provided text.
    word_appearances : List[str]
        A list of sentences -- where each sentence is represented by its numerical order in the provided text's
        sentences -- in which a word appeared.
    """

    def __init__(self, word_frequency: int, word_first_appearance: str):
        """
        Parameters
        ----------
        word_frequency : int
            Times a word has appeared in text.
        word_first_appearance : str
            The first sentence in which a word occurred. Stored as a string so that it can easily be used in format
            string when generating lines of the concordance.
        """

        self.word_frequency: int = word_frequency
        self.word_appearances: List[str] = list([word_first_appearance])

    # Only used in Unit Tests
    def __eq__(self, other):
        equal = False

        if isinstance(other, WordInfo):
            if self.word_frequency == other.word_frequency:
                if self.word_appearances == other.word_appearances:
                    equal = True

        return equal
