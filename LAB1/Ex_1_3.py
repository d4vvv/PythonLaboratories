def get_code(code):
    input_code = input("Please enter the code: ")
    if code == input_code:
        print("Welcome")
    else:
        print("Wrong Code")

get_code("123")