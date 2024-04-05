def count_words_and_sentences(file_path: str) -> tuple[int, int]:
    """
    Count the number of words and sentences in a text file.

    Args:
    file_path (str): The path to the text file.

    Returns:
    tuple[int, int]: A tuple containing the number of words and sentences.
    """
    with open(file_path, 'r') as file:
        text = file.read()

    # Counting words
    words = text.split()
    num_words = len(words)

    # Counting sentences
    sentence_endings = ('.', '!', '?', '...')
    num_sentences = sum(text.count(end) for end in sentence_endings)

    return num_words, num_sentences
