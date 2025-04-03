# Write your code here.
# Write your code here.
#Task 1: Hello
#Write a hello function that takes no arguments and returns Hello!. 
#  Now, what matters here is what the function returns. 
#  You can print() whatever you want for debugging purposes, 
# but the tests ignore that, and only check the return value.
print("--------------Task 1------------")
def hello():
    print("Hello!");
hello();


#Task 2: Greet with a Formatted String
#Write a greet function.  It takes one argument, a name, and returns Hello,
#  Name!.  Use a formatted string. 
#  Note that you have to return exactly the right string or the test fails -- 
# but PyTest tells you what didn't match.

print("--------------Task 2------------")

def greet(name):
    print("Hello, " + name);
greet("Shakera!");

#Task 3

# def test_calc():
#     assert a1.calc(5,6) == 30
#     assert a1.calc(5,6,"add") == 11
#     assert a1.calc(20,5,"divide") == 4
#     assert a1.calc(14,2.0,"multiply") == 28.0
#     assert a1.calc(12.6, 4.4, "subtract") == 8.2
#     assert a1.calc(9,5, "modulo") == 4
#     assert a1.calc(10,0,"divide") == "You can't divide by 0!"
#     assert a1.calc("first", "second", "multiply") == "You can't multiply those values!"

print("--------------Task 3------------")

def calc(a,b, operation="multiply"):
    try:     
        if operation == "add":
            return a + b;
        elif operation == "subtract":
            return a - b;
        elif operation == "multiply":
            return a * b;
        elif operation == "divide":
            return a / b if b != 0 else "You can't divide by zero";
        elif operation == "modulo":
            return a % b if b != 0 else "Error: Modulo by zero";
        # elif operation == "int_divide":
        #     return a // b if b != 0 else "Error: You can't divide  by zero"
        elif operation == "power":
            return a ** b
        else:
            return "You can't multiply those values!"
    except TypeError:
        return "You can't multiply those values!"
    
print(calc(5, 6))  
print(calc(5, 6, "add"))  
print(calc(20, 5, "divide")) 
print(calc(14, 2.0, "multiply")) 
print(calc(12.6, 4.4, "subtract")) 
print(calc(9,5 , "modulo"))  
print(calc(10, 0, "divide")) 
print(calc("first","second", "multiply"))

# Task 4
print("--------------Task 4------------")
# test_data_type_conversion():
#     result = a1.data_type_conversion("110", "int")
#     assert type(result).__name__ == "int"
#     assert result == 110
#     result = a1.data_type_conversion("5.5", "float")
#     assert type(result).__name__ == "float"
#     assert result == 5.5
#     result = a1.data_type_conversion(7,"float")
#     assert type(result).__name__ == "float"
#     assert result == 7.0
#     result = a1.data_type_conversion(91.1,"str")
#     assert type(result).__name__ == "str"
#     assert result == "91.1"
#     assert a1.data_type_conversion("banana", "int") == "You can't convert banana into a int."

def data_type_conversion(value, type):
        try:
            if type == "int":
                return int(value);
            elif type == "float":
                return float(value);
            elif type == "string":
                return str(value);
            else:
                return f"Error: Unsupported data type {type}."
        except (ValueError, TypeError):  
            return f"You can't convert {value} into a {type}."

    
print(data_type_conversion("110", "int"));
print(data_type_conversion("5.5", "float"));
print(data_type_conversion(7, "float"));
print(data_type_conversion("91.1", "str"));
print(data_type_conversion("banana", "int"));

#Task 5

print("--------------Task 5------------")

# def test_grade():
#     assert a1.grade(75,85,95) == "B"
#     assert a1.grade("three", "blind", "mice") == "Invalid data was provided."

def test_grade(*args):
    try:
          if not args:
            return "Invalid data was provided"
          
          average = sum(args) / len(args)

          if average >= 90:
              return "A"
          elif average >= 80:
              return "B"
          elif average >= 70:
              return "C"
          elif average >=60:
              return "D"
          else:
              return "F"
          
    except (TypeError, ZeroDivisionError):
        return "Invalid data was provided"
    
print(test_grade(95,92));
print(test_grade(75,85,95));
print(test_grade("three", "blind", "mice"));
    
# Task 6

print("--------------Task 6 ------------")
#def test_repeat():
    #assert a1.repeat("up,", 4) == "up,up,up,up,"

def test_repeat(str1, count):
    for i in range(count):
        return str1 * count;

print(test_repeat("up, ", 4));

# Task 7
print("--------------Task 7------------")
# def test_student_scores():
#     assert a1.student_scores("mean", Tom=75, Dick=89, Angela=91) == (75 + 89 + 91) / 3
#     assert a1.student_scores("best", Tom=75, Dick=89, Angela=91, Frank=50 ) == "Angela"


def student_scores(option, **kwargs):
    if not kwargs:
        return "No student scores available"
    
    if option == "best":
        return max(kwargs, key=kwargs.get)
    elif option == "mean":
        return sum(kwargs.values()) / len(kwargs)
    else:
        return "Invalid option. use 'best' or 'mean'"
    

print(student_scores("mean", Tom=75, Dick=89, Angela=91));
print(student_scores("best", Tom=95, Dick=89, Angela=91, Frank=50 ));
print(student_scores("best"));

#Task 8
print("--------------Task 8------------")
# def test_titleize():
    # assert a1.titleize("war and peace") == "War and Peace"
    # assert a1.titleize("a separate peace") == "A Separate Peace"
    # assert a1.titleize("after on") == "After On"

def titleize(title):
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    words = title.split()

    for i, word in enumerate(words):
        if i == 0 or i == len(words) -1 or word.lower() not in little_words:
            words[i] = word.capitalize()
        else:
            words[i] = word.lower()

    return " ".join(words)
    
print(titleize("war and peace"))
print(titleize("a separate peace"))
print(titleize("after on"))

#Task 9
print("--------------Task 9------------")
# def test_hangman():
#     assert a1.hangman("difficulty","ic") == "_i__ic____"

def hangman(secret, guess):
    return "".join(letter if letter in guess else "_" for letter in secret)

print(hangman("alphabet", "ab"))  
print(hangman("difficulty", "ic")) 

#Test 9
print("--------------Task 10------------")
# def test_pig_latin():
#     assert a1.pig_latin("apple") == "appleay"
#     assert a1.pig_latin("banana") == "ananabay"
#     assert a1.pig_latin("cherry") == "errychay"
#     assert a1.pig_latin("quiet") == "ietquay"
#     assert a1.pig_latin("square") == "aresquay"
#     assert a1.pig_latin("the quick brown fox") == "ethay ickquay ownbray oxfay"
     
def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    pig_latin_words = []

    for word in words:
        if word[0] in vowels:  # Case 1: Starts with a vowel
            pig_latin_words.append(word + "ay")
        elif word.startswith("qu"):  # Case 2: Special case for "qu"
            pig_latin_words.append(word[2:] + "quay")
        else:  # Case 3: Starts with consonants
            for i, letter in enumerate(word):
                if letter in vowels:
                    pig_latin_words.append(word[i:] + word[:i] + "ay")
                    break

    return " ".join(pig_latin_words)

print(pig_latin("apple"))  
print(pig_latin("banana"))  
print(pig_latin("cherry"))  
print(pig_latin("quiet"))  
print(pig_latin("square"))  
print(pig_latin("the quick brown fox")) 