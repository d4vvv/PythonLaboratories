import xml.sax

class BookHandler(xml.sax.ContentHandler):

    def __init__(self):
        self.current = ""
        self.id = ""
        self.title = ""
        self.author = ""
        self.genre = ""
        self.price = ""
        self.publish_date = ""
        self.description = ""

    def startElement(self, tag, attrs):
        self.current = tag
        if tag == "book":
            print("ID: " + attrs["id"])

    def endElement(self, tag):
        if self.current == "title":
            print("Title: " + self.title)
        elif self.current == "author":
            print("Author: " + self.author)
        elif self.current == "genre":
            print("Genre: " + self.genre)
        elif self.current == "price":
            print("Price: " + self.price)
        elif self.current == "publish_date":
            print("Publish date: " + self.publish_date)
        elif self.current == "description":
            print("Description: " + self.description)
        self.current = ""

    def characters(self, content):
        if self.current == "title":
            self.title = content
        elif self.current == "author":
            self.author = content
        elif self.current == "genre":
            self.genre = content
        elif self.current == "price":
            self.price = content
        elif self.current == "publish_date":
            self.publish_date = content
        elif self.current == "description":
            self.description = content


parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
Handler = BookHandler()
parser.setContentHandler(Handler)
parser.parse("C:/Users/Kacper/Desktop/AGH/7Semester/Python/LAB6/books.xml")