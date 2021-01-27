comment = "one " \
          "two " \
          "three"

multiline_comment = """
four
five
six
"""

print(comment)
print(multiline_comment)

name = "Jamila"
email = """"
hello {},
how are you?
"""
print(email.format(name))

last_name = "Smith"
mail = f"""
    hi {last_name},
    Nice to meet you!
    Age: {7 + 13}
"""

print(mail)


