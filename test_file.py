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
