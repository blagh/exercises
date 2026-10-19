# This week's question:
# There's a ghost in your keyboard! It keeps typing weird symbols in your words. Given a string you 
# typed (with the ghost), deletes the last character and ~ duplicates it, if one exists. Return 
# the final text.

# Examples:

# ghostwriter("ghost")
# > "ghost"

# ghostwriter("a#~b")
# > "b"

# ghostwriter("a~#b")
# > "ab"

# ghostwriter("ab#~c")
# > "aac"

# ghostwriter("ab~c#")
# > "abb"

# ghostwriter("a~~~")
# > "aaaa"

# ghostwriter("aaaa####")
# > ""

# ghostwriter("BBB##O~")
# > 'BOO'

SKIP = "#"
DOUBLE = "~"
CONTROLS = [SKIP, DOUBLE]

def ghostwriter(ghost):

    result = []

    for char in ghost:
        if char not in CONTROLS:
            result += char

        if char == SKIP:
            result.pop()

        if char == DOUBLE and result:
            result += result[-1]

    return "".join(result)

print("ghost: " + ghostwriter("ghost") + "\n")  # > "ghost"
print("b: " + ghostwriter("a#~b") + "\n")  # > "b"
print("abb: " + ghostwriter("ab~c#") + "\n")  # > "abb"
print("ab: " + ghostwriter("a~#b") + "\n") # > "ab"
print("aac: " + ghostwriter("ab#~c") + "\n") # > "aac"
print("aaaa: " + ghostwriter("a~~~") + "\n") # > "aaaa"
print("BOO: " + ghostwriter("BBB##O~") + "\n")  # > "BOO"
print("empty: " + ghostwriter("aaaa####") + "\n")
