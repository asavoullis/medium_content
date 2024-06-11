import re






text = "Example text: Python_3.8"
matches = re.findall(r'\w+', text)

print(matches)
# Output: ['Example', 'text', 'Python_3', '8']

"""
As you can see, \w+ matches "Example", "text", "Python_3", and "8". 
It does not include spaces, punctuation, or other non-word characters. 
The underscore _ is considered a word character and is included in the match that contains "Python_3".

In regular expressions, the + is a quantifier that means "one or more" of the preceding element. 
When you use \w+ in a regex pattern, it tells the regex engine to match sequences of one or 
more word characters (\w), which include letters, digits, and underscores (_).

Here's a breakdown of how this works:

\w matches a single word character.
\w+ extends this match to sequences of word characters without any upper limit on their length, as long as 
there's at least one word character in the sequence.
This is very useful for extracting whole words or alphanumeric identifiers from a text, because it allows 
the regex to capture entire contiguous strings of word characters. Without the +, the regex \w 
would only match one word character at a time.

"""
