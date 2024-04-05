import os
import pytest
from main import count_words_and_sentences


@pytest.fixture
def sample_text(tmpdir):
    """
    Fixture that creates a sample text file for testing.
    """
    sample_text = "Hello, world! This is a sample text file. It has three sentences."
    file_path = os.path.join(tmpdir, "test.txt")
    with open(file_path, "w") as file:
        file.write(sample_text)
    return file_path

@pytest.mark.parametrize("input_text, expected_words, expected_sentences", [
    ("Hello, world!", 2, 1),
    ("This is a sample text file.", 6, 1),
    ("It has three sentences.", 4, 1),
])
def test_count_words_and_sentences(tmpdir, input_text, expected_words, expected_sentences):
    """
    Test count_words_and_sentences function with different inputs.
    """
    file_path = os.path.join(tmpdir, "test.txt")
    with open(file_path, "w") as file:
        file.write(input_text)

    words, sentences = count_words_and_sentences(file_path)
    assert words == expected_words
    assert sentences == expected_sentences

def test_count_words_and_sentences_with_fixture(sample_text):
    """
    Test count_words_and_sentences function using a fixture.
    """
    words, sentences = count_words_and_sentences(sample_text)
    assert words == 12
    assert sentences == 3