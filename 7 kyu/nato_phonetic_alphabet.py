letters = {'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta',
           'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel',
           'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima',
           'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa',
           'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
           'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray',
           'Y': 'Yankee', 'Z': 'Zulu'}


def nato(word):
    return ' '.join(letters[a] for a in word.upper())

assert nato("babble") == "Bravo Alpha Bravo Bravo Lima Echo"
