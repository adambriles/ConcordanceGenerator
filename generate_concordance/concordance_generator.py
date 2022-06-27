import math
import string
import spacy
from typing import List, Dict, Optional

from generate_concordance.concordance_empty import ConcordanceEmpty
from generate_concordance.word_info import WordInfo

ASCII_TABLE_OFFSET: int = ord('a')
CHARS_IN_ALPHABET: int = 26


class ConcordanceGenerator:
    """
    A class to generate a concordance from a given string.

    Attributes
    ----------
    __language_processor : spacy.Language
        An instance of a natural language processor used to find tokens and sentences in user provided text.
    __word_to_info : Dict[WordInfo]
        A unique word mapped to a class containing how many times a word has appeared in a text string
         and in which sentences it appeared in.
    __longest_word : int
        The longest word in the user provided text. Used to dynamically generate the size of the word column in
        a line of the concordance.

    Methods
    -------
    __get_concordance_line_prefix(words_processed: int)
        Based off of how many lines of the concordance have already been processed, generate the prefix -- EX: bbbbb. --
        of a line in a concordance.
    __get_concordance_line(word: str, words_processed, prefix_column_length: int):
        Generate one line in the concordance for the given word.
    get_concordance_lines()
        Returns a list of formatted lines in a concordance.
    get_longest_word():
        Gets the longest word in the concordance
    get_word_to_info():
        Gets the dictionary used to build the concordance.
    generate_concordance(text: str)
        Track how many times a word has appeared in text and in what sentences it appeared in using the
        __word_to_info dictionary.
    """

    def __init__(self):
        self.__language_processor: spacy.Language = spacy.load('en_core_web_sm')

        # Set class variables to None to be able to check if generate_concordance has been run before trying to
        #   print a concordance
        self.__word_to_info: Optional[Dict[str, WordInfo]] = None
        self.__longest_word: Optional[int] = None

    def __get_concordance_line_prefix(self, words_processed: int) -> str:
        """Gets the prefix of a concordance line.

        Parameters
        ----------
        words_processed : int
            Number of words in the concordance for which lines have already been generated. Used to determine which
            letter the prefix of a concordance line should be.

        Returns
        -------
        str
            prefix of a concordance line plus whitespace padding
        """

        prefix_column_length: int = math.ceil(len(self.__word_to_info) / CHARS_IN_ALPHABET)
        prefix_length: int = (words_processed // CHARS_IN_ALPHABET) + 1
        char_offset: int = words_processed % CHARS_IN_ALPHABET

        line_prefix_components: List[str] = [chr(ASCII_TABLE_OFFSET + char_offset) for _ in range(prefix_length)]
        line_prefix_components.append(".")

        # Pad the prefix to keep a consistent prefix column length when left aligning the word in the concordance line
        prefix_padding: List[str] = [" " for _ in range(prefix_column_length - prefix_length)]

        line_prefix_components.extend(prefix_padding)

        return "".join(line_prefix_components)

    def __get_concordance_line(self, word: str, words_processed, prefix_column_length: int):
        """Generate a line for a word in the concordance.

        Each row is separated into columns of prefix, word, and word info. Each row component is left aligned
        and the column size is based off the largest string in the column.

        Parameters
        ----------
        word : str
            Word to generate the concordance line for
        words_processed : int
            Number of words in the concordance for which lines have already been generated.
        prefix_column_length :
            Length of the prefix column. Used to a consistent length for the prefix column despite varying prefix size

        Returns
        -------
        str
            line for a word in the concordance
        """

        word_info: WordInfo = self.__word_to_info[word]
        appearance_list: str = ",".join(word_info.word_appearances)
        prefix: str = self.__get_concordance_line_prefix(words_processed=words_processed)
        line: str = f"{prefix:<{prefix_column_length}} {word:<{self.__longest_word}} {{{word_info.word_frequency}:{appearance_list}}}"

        return line

    def get_concordance_lines(self) -> List[str]:
        """Get the lines of a concordance for previously supplied text.

        Each line is composed of the concordance prefix, word, and word occurrences to sentences appeared in.
        Each line does not end with a newline character.

        Returns
        -------
        List[str]
            list of lines in a concordance.

        Raises
        ------
        ConcordanceEmpty
            If the object was initialized but generate_concordance() was never called to create the concordance.

        """
        if self.__word_to_info and self.__longest_word:
            concordance_lines: List[str] = list()

            words_processed: int = 0
            prefix_column_length: int = math.ceil(len(self.__word_to_info) / 26)

            # Sort the __wordToInfo dictionary's keys and iterate through the sorted list to print words alphabetically
            for word in sorted(self.__word_to_info.keys()):
                concordance_lines.append(self.__get_concordance_line(word=word,
                                                                     words_processed=words_processed,
                                                                     prefix_column_length=prefix_column_length))
                words_processed += 1

            return concordance_lines
        else:
            raise ConcordanceEmpty("generate_concordance(<input file>) must be run before attempting to output a "
                                   "concordance.")

    # Currently, only used to check the state of the GenerateConcordance object in Unit Tests.
    def get_longest_word(self) -> Optional[int]:
        """ Gets the longest word in the concordance

        If generate_concordance() is never run, None will be returned.

        Returns
        -------
        int
            Longest word in the concordance
        """
        return self.__longest_word

    # Currently, only used to check the state of the GenerateConcordance object in Unit Tests.
    def get_word_to_info(self) -> Optional[Dict[str, WordInfo]]:
        """ Gets the dictionary used to build the concordance.

        If generate_concordance() is never run, None will be returned.

        Returns
        -------
        Dict[str, WordInfo]
            A dictionary of words in the provided text to an object containing their frequency and a list of what
            sentences a word appeared in.
        """
        return self.__word_to_info

    def generate_concordance(self, text: str) -> None:
        """Generate a concordance for the given text.

        Parameters
        ----------
        text : str
            Text to generate a concordance for.
        """
        # Reset class variables so the same instance of ConcordanceGenerator can be reused.
        self.__word_to_info = dict()
        self.__longest_word = 0
        self.__language_processor = spacy.load('en_core_web_sm')

        # The spacy natural language processor doesn't consider newlines to be word separators, so words at the end
        #   of a line get appended to the front of the first word in the next line. Remove all white space that could
        #   cause issues and replace them with a space for the best results.
        text_no_newlines: str = " ".join(text.split())

        text_document = self.__language_processor(text_no_newlines)

        sentence_count = 1
        for sentence in text_document.sents:
            for token in sentence:
                lowercase_token: str = token.text.lower()
                if lowercase_token not in string.punctuation:
                    if lowercase_token in self.__word_to_info:
                        word_info: WordInfo = self.__word_to_info.get(lowercase_token)
                        word_info.word_frequency += 1
                        word_info.word_appearances.append(str(sentence_count))
                    else:
                        self.__word_to_info[lowercase_token] = WordInfo(word_frequency=1,
                                                                        word_first_appearance=str(sentence_count))

                        # Calculate the longest word present in the set to avoid iterating through the dictionary again
                        #   when the longest word is required to properly format the printed concordance
                        if len(lowercase_token) > self.__longest_word:
                            self.__longest_word = len(lowercase_token)

            sentence_count += 1
