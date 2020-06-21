#https://realpython.com/regex-python-part-2/

"""
The available regex functions in the Python re module fall into the following three categories:

Searching functions
Substitution functions
Utility functions
"""
"""
Searching Functions
Searching functions scan a search string for one or more matches of the specified regex:

Function	Description
re.search()	Scans a string for a regex match
re.match()	Looks for a regex match at the beginning of a string
re.fullmatch()	Looks for a regex match on an entire string
re.findall()	Returns a list of all regex matches in a string
re.finditer()	Returns an iterator that yields regex matches from a string
As you can see from the table, these functions are similar to one another. But each one tweaks the searching functionality in its own way.
"""


if __name__ == "__main__":
    """
    re.search(<regex>, <string>, flags=0)

    Scans a string for a regex match.
    """

    import re

    print(re.search(r'(\d+)', 'fool123bar'))
    print(re.search(r'[a-z]+', '123FOO456', re.IGNORECASE))
    print(re.search(r'\d+', 'foo.bar'))
          
    """
    re.match(<regex>, <string>, flags=0)

Looks for a regex match at the beginning of a string.

This is identical to re.search(), except that re.search() returns a match if <regex> matches anywhere in <string>, whereas re.match() returns a match only if <regex> matches at the beginning of <string>
    """

    print(re.match(r'\d+', '123foobar'))

    #but then
    print(re.search(r'\d+', '123foobar'))
    print(re.search(r'\d+', 'foo123bar'))

    """
    if <string> contains embedded newlines, then the MULTILINE flag causes re.search() to match the caret (^) anchor metacharacter either at the beginning of <string> or at the beginning of any line contained within <string>
    """

    s = 'foo\nbar\nbaz'

    print(re.search('^foo', s))
    print(re.search('^bar', s, re.MULTILINE))

    #but Even with the MULTILINE flag set, re.match() will match the caret (^) anchor only at the beginning of <string>, not at the beginning of lines contained within <string>.
    
    print(re.match('^foo', s))
    print(re.match('^bar', s, re.MULTILINE))


    """
    Even with the MULTILINE flag set, re.match() will match the caret (^) anchor only at the beginning of <string>, not at the beginning of lines contained within <string>.
    """

    print(re.fullmatch(r'\d+', '123foobar'))
    print(re.fullmatch(r'\d+', 'foo123'))
    print(re.fullmatch(r'\d+', 'foo123bar'))
    print(re.fullmatch(r'\d+', '123'))
    print(re.search(r'^\d+$', '123'))

    """
    re.findall(<regex>, <string>, flags=0)

Returns a list of all matches of a regex in a string.

re.findall(<regex>, <string>) returns a list of all non-overlapping matches of <regex> in <string>. It scans the search string from left to right and returns all matches in the order found:
    """
    print(re.findall(r'\w+', '...foo,,,,bar:%$baz//|'))
    print(re.findall(r'#(\w+)#', '#foo#.#bar#.#baz#'))


    print(re.findall(r'(\w+),(\w+)', 'foo,bar,baz,qux,quux,corge'))


    print(re.findall(r'(\w+),(\w+),(\w+)', 'foo,bar,baz,qux,quux,corge'))

    """
    re.finditer(<regex>, <string>, flags=0)

Returns an iterator that yields regex matches.

re.finditer(<regex>, <string>) scans <string> for non-overlapping matches of <regex> and returns an iterator that yields the match objects from any it finds. It scans the search string from left to right and returns matches in the order it finds them
    """

    for i in re.finditer(r'\w+', '...foo,,,,bar:%$baz//|'):
        print(i)

    """
    re.findall() and re.finditer() are very similar, but they differ in two respects:

re.findall() returns a list, whereas re.finditer() returns an iterator.

The items in the list that re.findall() returns are the actual matching strings, whereas the items yielded by the iterator that re.finditer() returns are match objects
    """



    """
    Substitution Functions
Substitution functions replace portions of a search string that match a specified regex:

Function	Description
re.sub()	Scans a string for regex matches, replaces the matching portions of the string with the specified replacement string, and returns the result
re.subn()	Behaves just like re.sub() but also returns information regarding the number of substitutions made

    Both re.sub() and re.subn() create a new string with the specified substitutions and return it. The original string remains unchanged. (Remember that strings are immutable in Python, so it wouldnt be possible for these functions to modify the original string.)

re.sub(<regex>, <repl>, <string>, count=0, flags=0)

Returns a new string that results from performing replacements on a search string.
    re.sub(<regex>, <repl>, <string>) finds the leftmost non-overlapping occurrences of <regex> in <string>, replaces each match as indicated by <repl>, and returns the result. <string> remains unchanged.

<repl> can be either a string or a function, as explained below.
    """
    s = 'foo.123.bar.789.baz'

    print(re.sub(r'\d+', '#', s))

    print(re.sub('[a-z]+', '(*)', s))

    """
    re.sub() replaces numbered backreferences (\<n>) in <repl> with the text of the corresponding captured group:
    """
    print(re.sub(r'(\w+),bar,baz,(\w+)',
       r'\2,bar,baz,\1',
       'foo,bar,baz,qux'))

    #same can be done like
    print(re.sub(r'foo,(?P<w1>\w+),(?P<w2>\w+),qux',
       r'foo,\g<w2>,\g<w1>,qux',
       'foo,bar,baz,qux'))

    #same can be done like
    print(re.sub(r'foo,(\w+),(\w+),qux',
       r'foo,\g<2>,\g<1>,qux',
       'foo,bar,baz,qux'))

    """
    suppose you have a string like 'foo 123 bar' and want to add a '0' at the end of the digit sequence.
    """

    #re.sub(r'(\d+)', r'\10', 'foo 123 bar')
    
    print(re.sub(r'(\d+)', r'\g<1>0', 'foo 123 bar'))

    print(re.sub(r'\d+', '/\g<0>/', 'foo 123 bar'))


    """
    If <regex> specifies a zero-length match, then re.sub() will substitute <repl> into every character position in the string
    """

    print(re.sub('x*', '-', 'foo'))

    """
    In the example above, the regex x* matches any zero-length sequence, so re.sub() inserts the replacement string at every character position in the stringbefore the first character, between each pair of characters, and after the last character.
    """







    """
    Utiltiy functions
    There are two remaining regex functions in the Python re module that youve yet to cover:

Function	Description
re.split()	Splits a string into substrings using a regex as a delimiter
re.escape()	Escapes characters in a regex
    """
    print(re.split('\s*[,;/]\s*', 'foo,bar  ;  baz / qux'))
    print(re.split('(\s*[,;/]\s*)', 'foo,bar  ;  baz / qux'))

    """
    If you need to use groups but dont want the delimiters included in the return list, then you can use noncapturing groups:
    """

    string = 'foo,bar  ;  baz / qux'
    regex = r'(?:\s*[,;/]\s*)'
    print(re.split(regex, string))

    """
    If the optional maxsplit argument is present and greater than zero, then re.split() performs at most that many splits. The final element in the return list is the remainder of <string> after all the splits have occurred
    """

    s = 'foo, bar, baz, qux, quux, corge'

    re.split(r',\s*', s)

    print(re.split(r',\s*', s, maxsplit=3))
    







    """
    Compiled Regex Objects in Python
    """


    """
    re.compile(<regex>, flags=0)

    Compiles a regex into a regular expression object.
    

    re_obj = re.compile(<regex>, <flags>)
    result = re.search(re_obj, <string>)
    or
    re_obj = re.compile(<regex>, <flags>)
    result = re_obj.search( <string>)
    or
    result = re.search(<regex>, <string>, <flags>)

    The truth is that the re module compiles and caches a regex when its used in a function call. If the same regex is used subsequently in the same Python code, then it isnt recompiled. The compiled value is fetched from cache instead. So the performance advantage is minimal.

    """

    """
    re_obj.search(<string>[, <pos>[, <endpos>]])
    re_obj.match(<string>[, <pos>[, <endpos>]])
    re_obj.fullmatch(<string>[, <pos>[, <endpos>]])
    re_obj.findall(<string>[, <pos>[, <endpos>]])
    re_obj.finditer(<string>[, <pos>[, <endpos>]])
    
    the search only applies to the portion of <string> indicated by <pos> and <endpos>, which act the same way as indices in slice notation.

    re_obj.split(<string>, maxsplit=0)
    re_obj.sub(<repl>, <string>, count=0)
    re_obj.subn(<repl>, <string>, count=0)
    """


    re_obj = re.compile(r'\d+')
    s = 'foo123barbaz'

    re_obj.search(s)


    print(s[6:9])

    print(re_obj.search(s, 3, 6))


    """
    Regular Expression Object Attributes
    """

    """
    re_obj.flags	Any <flags> that are in effect for the regex
    re_obj.groups	The number of capturing groups in the regex
    re_obj.groupindex	A dictionary mapping each symbolic group name defined by the (?P<name>) construct (if any) to the corresponding group number
    re_obj.pattern	The <regex> pattern that produced this object
    """

    re_obj = re.compile(r'(?m)(\w+),(\w+)', re.I)
    print(re_obj.flags)

    print(re.I|re.M|re.UNICODE)

    print(re_obj.groups)

    print(re_obj.pattern)


    re_obj = re.compile(r'(?P<w1>),(?P<w2>)')
    re_obj.groupindex

    re_obj.groupindex['w1']

    re_obj.groupindex['w2']





    """
    Match Object Methods
    """

    """
    match.group()	The specified captured group or groups from match
    match.__getitem__()	A captured group from match
    match.groups()	All the captured groups from match
    match.groupdict()	A dictionary of named captured groups from match
    match.expand()	The result of performing backreference substitutions from match
    match.start()	The starting index of match
    match.end()	The ending index of match
    match.span()	Both the starting and ending indices of match as a tuple
    """

    m = re.search(r'(\w+),(\w+),(\w+)', 'foo,bar,baz')
    print(m.group(1))

    print(m.group(3))

    print(m.group(1, 3))

    print(m.group(3, 3, 1, 1, 2, 2))


    m = re.match(r'(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)', 'quux,corge,grault')

    
    print(m.group('w1'))

    print(m.group('w2'))
 
    print(m.group('w3', 'w1', 'w1', 'w2'))



    """
    A question mark (?) quantifier metacharacter follows the third group, though, so that group is optional. A match will occur if theres a third sequence of word characters following the second comma (,) but also if there isnt.

In this case, there isnt. So there is match overall, but the third group doesnt participate in it. As a result, m.group(3) is still defined and is a valid reference, but it returns None:

    """
    
    m = re.search(r'(\w+),(\w+),(\w+)?', 'foo,bar,')
    print(m.group(1, 2)    )

    print(m.group(3))

    """
    It can also happen that a group participates in the overall match multiple times. If you call .group() for that group number, then it returns only the part of the search string that matched the last time. The earlier matches arent accessible:

    """

    m = re.match(r'(\w{3},)+', 'foo,bar,baz,qux')
    print(m.group(1))
    print(m.group())
    print(m.group(0))



    """
    obj[n]  is equivalent to obj.__getitem__(n)
    The syntax obj[n] is only meaningful if a .__getitem()__ method exists for the class or type to which obj belongs. Exactly how Python interprets obj[n] will then depend on the implementation of .__getitem__() for that class.

    When a programming language provides alternate syntax that isnt strictly necessary but allows for the expression of something in a cleaner, easier-to-read way, its called syntactic sugar. For a match object, match[n] is syntactic sugar for match.group(n)
    """

    m = re.search(r'(\w+),(\w+),(\w+)', 'foo,bar,baz')

    print(m.__getitem__(2))
    print(m.group(2))

    


    
