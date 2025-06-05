from catalogue import Catalogue
from attributes import Attributes, Genre


def fill(catalogue):
    catalogue.add(Attributes("Life of Pi", "Martel", "Yann", 2003, Genre.ADVENTURE))
    catalogue.add(Attributes("The Call of the Wild", "London", "Jack", 1903, Genre.ADVENTURE))
    catalogue.add(Attributes("To Kill a Mockingbird", "Lee", "Harper", 1960, Genre.CLASSICS))
    # catalogue.add("Little Women", "Alcott", "Louisa May")
    # catalogue.add("The Adventure of Sherlock Holmes", "Doyle", "Arthur Conan")
    # catalogue.add("And Then There Were None", "Christie", "Agatha")
    # catalogue.add("Carrie", "King", "Stephen")
    # catalogue.add("It: A Novel", "King", "Stephen")
    # catalogue.add("Frankenstein", "Shelley", "Mary")
    # catalogue.add("2001: A Space Odyssey", "Clarke", "Arthur C.")
    # catalogue.add("Ender's Game", "Card", "Orson Scott")


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

    target_attrs = Attributes("Life of Pi", "Martel", "Yann", 2003, Genre.ADVENTURE)
    search(catalogue, target_attrs)
    target_attrs = Attributes("", "King", "", 0, Genre.HORROR)
    search(catalogue, target_attrs)
    # target = Book("1984", "Orwell", "George")
    # search(catalogue, target)
    # target = Book("", "", "")
    # search(catalogue, target)


def main():
    catalogue = Catalogue()
    fill(catalogue)
    test(catalogue)


if __name__ == "__main__":
    main()
