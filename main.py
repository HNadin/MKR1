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

def save_results(file_path: str, words: int, sentences: int):
    """
    Зберігає результати підрахунку слів і речень у файл.

    Args:
        file_path (str): Шлях до файлу, в який записуються результати.
        words (int): Кількість слів.
        sentences (int): Кількість речень.
    """
    with open(file_path, 'w') as file:
        file.write(f"Number of words: {words}\n")
        file.write(f"Number of sentences: {sentences}\n")

if __name__ == "__main__":
    input_file_path = "test.txt"  # Replace with the path to your input text file
    output_file_path = "results.txt"  # Replace with the path to your output text file

    words, sentences = count_words_and_sentences(input_file_path)
    print(f"Number of words: {words}")
    print(f"Number of sentences: {sentences}")

    save_results(output_file_path, words, sentences)
