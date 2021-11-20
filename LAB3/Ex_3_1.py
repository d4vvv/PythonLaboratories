def delete_words(path_, out_file_, words_to_delete_):
    with open(path_) as fileIn, open(out_file_, "w+") as file_out_:
        for line in fileIn:
            for word in words_to_delete_:
                line = line.replace(word,"")
            file_out_.write(line)

path = "C:/Users/Kacper/Desktop/AGH/7Semester/Python/LAB3/text.txt"
out_file = "C:/Users/Kacper/Desktop/AGH/7Semester/Python/LAB3/outText.txt"
words_to_delete = ["words", "to", "delete"]

delete_words(path, out_file, words_to_delete)