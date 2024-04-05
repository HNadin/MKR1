import re
from typing import Tuple


def count_words_and_sentences(file_path: str) -> Tuple[int, int]:
    """
    Підраховує кількість слів і речень у вказаному файлі.

    Args:
        file_path (str): Шлях до файлу.

    Returns:
        Tuple[int, int]: Кількість слів і речень у файлі.
    """
    with open(file_path, 'r') as file:
        text = file.read()

    word_count = len(text.split())

    # Використання регулярного виразу для підрахунку речень
    sentence_count = len(re.findall(r'[.!?]+', text))

    return word_count, sentence_count


if __name__ == "__main__":
    file_path = "test.txt"  # Replace with the path to your text file
    words, sentences = count_words_and_sentences(file_path)
    print(f"Number of words: {words}")
    print(f"Number of sentences: {sentences}")
