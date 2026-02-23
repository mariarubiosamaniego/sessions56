import requests
def download_book(url):
    """
    download a book given a url
    :param url: the url containing the book
    :return: None
    """
    print(url)
    response = requests.get(url)
    print(response.status_code)
    with open("book.txt", "w", encoding="utf-8") as f:
       f.write(response.text)

download_book("https://www.gutenberg.org/cache/epub/1342/pg1342.txt")

def get_5_letter_words(book_file):
    """
       Read contents of the book file and print 3 letter words starting with B
       :param book_file: file name of the book file
       :return: None
       """
    unique_words = []
    special_chars = ",.?!;:"
    with open(book_file, encoding="utf-8") as f:
        for line in f:
            for c in special_chars:
                line = line.replace(c, "")
            words = line.split()
            for word in words:
                if word not in unique_words and len(word)==5 and word[0]== "a":
                    unique_words.append(word)
    print(f"We have {len(unique_words)} unique words")
    print(unique_words)

get_5_letter_words("book.txt")