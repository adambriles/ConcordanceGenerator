class ConcordanceEmpty(Exception):
    """
    Class to raise as an exception If the ConcordanceGenerator was initialized but generate_concordance() was never
    called to create the concordance.
    """

    pass
