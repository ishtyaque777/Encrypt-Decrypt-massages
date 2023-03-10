password = "I am a dog"
input_Password = input("Enter the Password:- ")
if input_Password == password:
  select_option = input("Enter 'E' for Encryption and 'D' for Decryption. ")
  if select_option == 'e':
    massage = input("Enter a massage:- ")
    massage = massage.lower()
    len_mass = len(massage)
    print("Your Encrypted Massage is:- ")
    new_massage = ""
    while len_mass > 0:
      len_mass -= 1
      masschar = massage[len_mass]
      if masschar == "a":
        masschar = "~"
      elif masschar == "b":
        masschar = "!"
      elif masschar == "c":
        masschar = "@"
      elif masschar == "d":
        masschar = "#"
      elif masschar == "e":
        masschar = "$"
      elif masschar == "f":
        masschar = "%"
      elif masschar == "g":
        masschar = "^"
      elif masschar == "h":
        masschar = "&"
      elif masschar == "i":
        masschar = "*"
      elif masschar == "j":
        masschar = "("
      elif masschar == "k":
        masschar = ")"
      elif masschar == "l":
        masschar = "_"
      elif masschar == "m":
        masschar = "-"
      elif masschar == "n":
        masschar = "+"
      elif masschar == "0":
        masschar = "="
      elif masschar == "p":
        masschar = "{"
      elif masschar == "q":
        masschar = "["
      elif masschar == "r":
        masschar = "}"
      elif masschar == "s":
        masschar = "]"
      elif masschar == "t":
        masschar = "|"
      elif masschar == "u":
        masschar = ","
      elif masschar == "v":
        masschar = "<"
      elif masschar == "w":
        masschar = ">"
      elif masschar == "x":
        masschar = "?"
      elif masschar == "y":
        masschar = ":"
      elif masschar == "z":
        masschar = "/"
      new_massage = new_massage + masschar
    print(new_massage)
  elif select_option == "d":
    massage = input("Enter a decryption massage:- ")
    massage = massage.lower()
    len_mass = len(massage)
    print("Your Encrypted Massage is:- ")
    new_massage = ""
    while len_mass > 0:
      len_mass -= 1
      masschar = massage[len_mass]
      if masschar == "~":
        masschar = "a"
      elif masschar == "!":
        masschar = "b"
      elif masschar == "@":
        masschar = "c"
      elif masschar == "#":
        masschar = "d"
      elif masschar == "$":
        masschar = "e"
      elif masschar == "%":
        masschar = "f"
      elif masschar == "^":
        masschar = "g"
      elif masschar == "&":
        masschar = "h"
      elif masschar == "*":
        masschar = "i"
      elif masschar == "(":
        masschar = "j"
      elif masschar == ")":
        masschar = "k"
      elif masschar == "_":
        masschar = "l"
      elif masschar == "-":
        masschar = "m"
      elif masschar == "+":
        masschar = "n"
      elif masschar == "=":
        masschar = "0"
      elif masschar == "{":
        masschar = "p"
      elif masschar == "[":
        masschar = "q"
      elif masschar == "}":
        masschar = "r"
      elif masschar == "]":
        masschar = "s"
      elif masschar == "|":
        masschar = "t"
      elif masschar == ",":
        masschar = "u"
      elif masschar == "<":
        masschar = "v"
      elif masschar == ">":
        masschar = "w"
      elif masschar == "?":
        masschar = "x"
      elif masschar == ":":
        masschar = "y"
      elif masschar == "/":
        masschar = "z"
      new_massage = new_massage + masschar
    print(new_massage)
else:{
    print("Fuck Off")
  }