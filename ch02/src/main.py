from book import Book
from catalogue import Catalogue


def fill(catalogue):
    catalogue.add("Life of Pi", "Martel", "Yann")
    catalogue.add("The Call of the Wild", "London", "Jack")
    catalogue.add("To Kill a Mockingbird", "Lee", "Harper")
    catalogue.add("Little Women", "Alcott", "Louisa May")
    catalogue.add("The Adventure of Sherlock Holmes", "Doyle", "Arthur Conan")
    catalogue.add("And Then There Were None", "Christie", "Agatha")
    catalogue.add("Carrie", "King", "Stephen")
    catalogue.add("It: A Novel", "King", "Stephen")
    catalogue.add("Frankenstein", "Shelley", "Mary")
    catalogue.add("2001: A Space Odyssey", "Clarke", "Arthur C.")
    catalogue.add("Ender's Game", "Card", "Orson Scott")


def search(catalogue, target):
    print()
    print("Find ", end="")
    print(target)

    matches = catalogue.find(target)

    if len(matches) == 0:
        print("No matches found.")
    else:
        print("Matches found:")
        for book in matches:
            print("  ", end="")
            print(book)


def test(catalogue):
    print("Testing catalogue...")

    target = Book("Life of Pi", "Martel", "Yann")
    search(catalogue, target)
    target = Book("", "King", "")
    search(catalogue, target)
    target = Book("1984", "Orwell", "George")
    search(catalogue, target)
    target = Book("", "", "")
    search(catalogue, target)


def main():
    catalogue = Catalogue()
    fill(catalogue)
    test(catalogue)


if __name__ == "__main__":
    main()
