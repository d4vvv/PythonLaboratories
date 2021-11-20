from Ex_5_1 import Complex as comp


class Calculator:
    running = False

    def __init__(self):
        self.running = True
        while self.running:
            try:
                print(
                    "Provide first complex number in form of real and imaginary components separated with space. Input q q to quit")
                re1, im1 = input().split()

                if re1 == "q" and im1 == "q":
                    self.running = False
                    break

                print("Provide mathematical action (+ - x /)")
                action = input()
                print("Provide second complex number in form of real and imaginary components separated with space.")
                re2, im2 = input().split()

                try:
                    x = comp(float(re1), float(im1))
                    y = comp(float(re2), float(im2))

                    if action == "+":
                        result = x.add(y)
                        print(result.print())
                    elif action == "-":
                        result = x.subtract(y)
                        print(result.print())
                    elif action == "x":
                        result = x.multiply(y)
                        print(result.print())
                    elif action == "/":
                        result = x.divide(y)
                        print(result.print())
                    else:
                        print("Wrong input. Please try again")
                except:
                    print("Some error have occurred.")
            except:
                print("Wrong input. Please try again")


Calculator()
