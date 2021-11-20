import xml.dom.minidom

def parse_book_xml(path):
    dom1 = xml.dom.minidom.parse(path)
    groups = dom1.documentElement

    book_list = groups.getElementsByTagName("book")
    for book in book_list:
        print("ID: " + book.getAttribute("id"))
        print("Author: " + book.getElementsByTagName("author")[0].childNodes[0].data)
        print("Title: " + book.getElementsByTagName("title")[0].childNodes[0].data)
        print("Genre: " + book.getElementsByTagName("genre")[0].childNodes[0].data)
        print("Price: " + book.getElementsByTagName("price")[0].childNodes[0].data)
        print("Publish Date: " + book.getElementsByTagName("publish_date")[0].childNodes[0].data)
        print("Description: " + book.getElementsByTagName("description")[0].childNodes[0].data)
        print("\n")

    return None


def modify_xml(path):
    dom1 = xml.dom.minidom.parse(path)
    groups = dom1.documentElement

    book_list = groups.getElementsByTagName("book")
    book_list[0].getElementsByTagName("description")[0].childNodes[0].nodeValue = "TestDescription"

    dom1.writexml(open("C:/Users/Kacper/Desktop/AGH/7Semester/Python/LAB6/books2.xml", 'w'))

    return None

path = "C:/Users/Kacper/Desktop/AGH/7Semester/Python/LAB6/books.xml"
parse_book_xml(path)
modify_xml(path)
