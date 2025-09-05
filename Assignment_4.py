# Task - 1 : Read a File and Handle Errors
'''
try:
  file_1 = open("Sample.text", 'r')
  read_file = file_1.read()
  print(read_file)
  file_1.close()

except FileNotFoundError:
    print("Error: The file 'Sample.text' was not found")
'''


# Task 2: Write and Append Data to a File

file_2 = open("output.text", 'w')
text_1 = input("Enter text to write to the file: ")
writing_file = file_2.write(text_1 + "\n")
print("Data successfully written to output.text")
file_2.close()

text_2 = input("Enter additional text to append: ")
file_2 = open("output.text", 'a')
appending_file = file_2.write(text_2)
print("Data successfully appended")
file_2.close()


