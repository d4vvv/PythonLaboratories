def delete_words(path_, out_file_, words_to_replace_):
    with open(path_) as fileIn, open(out_file_, "w+") as file_out_:
        for line in fileIn:
            for key in words_to_replace_:
                line = line.replace(key,words_to_replace_[key])
            file_out_.write(line)

path = "C:/Users/Kacper/Desktop/AGH/7Semester/Python/LAB3/text.txt"
out_file = "C:/Users/Kacper/Desktop/AGH/7Semester/Python/LAB3/outReplaceText.txt"
words_to_delete = ["words", "to", "delete"]
words_to_replace = {"words": "is", "to": "great", "delete": "and"}

delete_words(path, out_file, words_to_replace)