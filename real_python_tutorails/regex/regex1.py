#https://realpython.com/regex-python/








if __name__ == "__main__":
    s = 'foo123bar'
    print('123' in s)

    print(s.find('123'))

    print(s.index('123'))


    #using re

    import re
    print(re.search('123', s))

    if re.search('123', s):
        print('found')
    else:
        print('not found')

    #python regex metacharacters

    print(re.search('[0-9][0-9][0-9]', 'foo123bar'))

    #The dot (.) metacharacter matches any character except a newline, so it functions like a wildcard

    print(re.search('1.3', 'foo123bar'))

    print(re.search('1.3', 'foo13bar'))

    print(re.search('ba[artz]', 'foobarqux'))

    print(re.search('[a-z]', 'FOObar'))

    #[0-9a-fA-F] matches any hexadecimal digit character:

    print(re.search('[0-9a-fA-f]', '--- a0 ---'))


    #You can complement a character class by specifying ^ as the first character, in which case it matches any character that isnt in the set. In the following example, [^0-9] matches any character that isnt a digit:


    print(re.search('[^0-9]', '12345foo'))

    #If a ^ character appears in a character class but isnt the first character, then it has no special meaning and matches a literal '^' character

    

    print(re.search('[#:^]', 'foo^bar:baz#qux'))


    #What if you want the character class to include a literal hyphen character? You can place it as the first or last character or escape it with a backslash (\)


    print(re.search('[-abc]', '123-456'))
    print(re.search('[abc-]', '123-456'))
    print(re.search('[ab\-c]', '123-456'))


    #If you want to include a literal ']' in a character class, then you can place it as the first character or escape it with backslash:

    print(re.search('[]]', 'foo[1]'))

    print(re.search('[ab\]cd]', 'foo[1]'))


    #Other regex metacharacters lose their special meaning inside a character class

    print(re.search('[)*+|]', '123*456'))

    print(re.search('[)*+|]', '123+456'))

    #The . metacharacter matches any single character except a newline

    print(re.search('foo.bar', 'fooxbar'))

    print(print(re.search('foo.bar', 'foobar')))

    print(re.search('foo.bar', 'foo\nbar'))

    #\w matches any alphanumeric word character. Word characters are uppercase and lowercase letters, digits, and the underscore (_) character, so \w is essentially shorthand for [a-zA-Z0-9_]:

    print(re.search('\w', '#(.a$@&'))

    print(re.search('[a-zA-Z0-9_]', '#(.a$@&'))


    #\W is the opposite. It matches any non-word character and is equivalent to [^a-zA-Z0-9_]:

    print(re.search('\W', 'a_1*3Qb'))

    print(re.search('[^a-zA-Z0-9_]', 'a_1*3Qb'))

    #\d is essentially equivalent to [0-9], and \D is equivalent to [^0-9].

    print(re.search('\d', 'abc4def'))

    print(re.search('\D', '234Q678'))


    #\s matches any whitespace character. unlike the dot wildcard metacharacter, \s does match a newline character. \S is the opposite of \s. It matches any character that isnt whitespace:

    print(re.search('\s', 'foo\nbar baz'))

    print(re.search('\S', '  \n foo  \n  '))

    #The character class sequences \w, \W, \d, \D, \s, and \S can appear inside a square bracket character class as well:

    print(re.search('[\d\w\s]', '---3---'))

    print(re.search('[\d\w\s]', '---a---'))

    print(re.search('[\d\w\s]', '--- ---'))

    #'\' Removes the special meaning of a metacharacter.

    print(re.search('.', 'foo.bar'))

    print(re.search('\.','foo.bar'))

    s =   r'foo\bar'
    
    print(re.search(r'\\', s))

    #Anchors

    #When the regex parser encounters ^ or \A, the parser s current position must be at the beginning of the search string for it to find a match.


    print(re.search('^foo', 'foobar'))

    print(re.search('\Afoo', 'foobar'))


    #When the regex parser encounters $ or \Z, the parser s current position must be at the end of the search string for it to find a match. Whatever precedes $ or \Z must constitute the end of the search string:


    print(re.search('bar$', 'foobar'))

    print(re.search('bar\Z', 'foobar'))

    print(re.search('bar$', 'foobar\n'))



    #\b asserts that the regex parser s current position must be at the beginning or end of a word. A word consists of a sequence of alphanumeric characters or underscores ([a-zA-Z0-9_]), the same as for the \w character class.


    print(re.search(r'\bbar', 'foo bar'))

    print(re.search(r'\bbar', 'foo.bar'))

    print(re.search(r'\bbar', 'foobar'))

    print(re.search(r'foo\b', 'foo bar'))

    print(re.search(r'foo\b', 'foo.bar'))

    print(re.search(r'foo\b', 'foobar'))


    #Using the \b anchor on both ends of the <regex> will cause it to match when it s present in the search string as a whole word:

    print(re.search(r'\bbar\b', 'foo bar baz'))

    print(re.search(r'\bbar\b', 'foo(bar)baz'))

    print(print(re.search(r'\bbar\b', 'foobarbaz')))



    #\B does the opposite of \b. It asserts that the regex parser s current position must not be at the start or end of a word:

    print(re.search(r'\Bfoo\B', 'foo'))

    print(re.search(r'\Bfoo\B', '.foo.'))

    print(re.search(r'\Bfoo\B', 'barfoobaz'))


    #quantifiers are *  + , ?

    #a* matches zero or more a's
    #a+ matches one or more a's
    #a  matches zero or one a.

    print(re.search('foo.*bar', '# foo $qux@grault % bar #'))


    #When used alone, the quantifier metacharacters *, +, and ? are all greedy, meaning they produce the longest possible match.

    print(re.search('<.*>', '%<foo> <bar> <baz>%'))

    #If you want the shortest possible match instead, then use the non-greedy metacharacter sequence *?:

    print(re.search('<.*?>', '%<foo> <bar> <baz>%'))

    print(re.search('<.+>', '%<foo> <bar> <baz>%'))

    print(re.search('<.+?>', '%<foo> <bar> <baz>%'))

    print(re.search('ba?', 'baaaa'))

    print(re.search('ba??', 'baaaa'))


    #{m} Matches exactly m repetitions of the preceding regex.

    print(re.search('x-{3}x', 'x--x'))

    print(re.search('x-{3}x', 'x----x'))


    #{m,n}, {,n}, {m,}, {,}

    #{} matches just the literal string '{}'

    print(re.search('x{}y', 'x{}y'))


    #{m,n} will match as many characters as possible, and {m,n}? will match as few as possible

    print(re.search('a{3,5}', 'aaaaaaaa'))

    print(re.search('a{3,5}?', 'aaaaaaaa'))

    #grouping

    #(<regex>) defines a subexpression or group

    print(re.search('(bar)', 'foo bar baz'))

    print(re.search('bar', 'foo bar baz'))

    #treating a group as a unit

    #A quantifier metacharacter that follows a group operates on the entire subexpression specified in the group as a single unit.

    print(re.search('(bar)+', 'foo bar baz'))

    print(re.search('(bar)+', 'foo barbar baz'))

    print(re.search('(bar)+', 'foo barbarbarbar baz'))

    print(re.search('(ba[rz]){2,4}(qux)?', 'bazbarbazqux'))

    print(re.search('(ba[rz]){2,4}(qux)?', 'barbar'))

    print(re.search('(foo(bar)?)+(\d\d\d)?', 'foofoobar'))

    print(re.search('(foo(bar)?)+(\d\d\d)?', 'foofoobar123'))

    print(re.search('(foo(bar)?)+(\d\d\d)?', 'foofoo123'))


    #m.groups return tuple containing all the captured groups from a regex match.

    m = re.search('(\w+),(\w+),(\w+)', 'foo,quux,baz')

    print(m)

    print(m.groups())


    #m.group(n) Returns a string containing the <n>th captured match.

    print(m.group(1))

    print(m.group(2))
    
    print(m.group(3))    


    print(m.group(2,3))

    print(m.group(3,1,2))


    #\n Matches the contents of a previously captured group.The sequence \<n>, where <n> is an integer from 1 to 99, matches the contents of the <n>th captured group

    regex = r'(\w+),\1'

    m = re.search(regex, 'foo,foo')

    print(m.group(1))

    m = re.search(regex, 'foo,qux')

    print(m)


    #(?P<name><regex>)  Creates a named captured group. The difference in this case is that you reference the matched group by its given symbolic <name> instead of by its number.

    m = re.search('(\w+),(\w+),(\w+)', 'foo,quux,baz')
    print(m.group(1,2,3))

    m = re.search('(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)', 'foo,quux,baz')
    print(m.group('w1','w2','w3'))

    print(m.groups())

    print(m.group(1,2,3))
    
    #(?P=<name> Matches the contents of a previously captured named group.

    m = re.search(r'(\w+),\1', 'foo,foo')
    print(m.group(1))

    m = re.search(r'(?P<word>\w+),(?P=word)', 'foo,foo')
    print(m.groups())

    print(m.group('word'))


    #(?:<regex>) creates noncapturing groups.

    m = re.search('(\w+),(?:\w+),(\w+)', 'foo,quux,baz')

    print(m.groups())

    print(m.group(1))

    print(m.group(2))


    #(?(<n>)<yes-regex>|<no-regex>)  specifies a conditional match

    regex = r'^(###)?foo(?(1)bar|baz)'

    #^(###)? indicates that the search string optionally begins with '###'.
    #If it does, then the grouping parentheses around ### will create a group numbered 1. Otherwise, no such group will exist.The next portion, foo, literally matches the string 'foo'.
    #Lastly, (?(1)bar|baz) matches against 'bar' if group 1 exists and 'baz' if it doesnt.


    print(re.search(regex, '###foobaz'))

    print(re.search(regex, 'foobar'))

    print(re.search(regex, 'foobaz'))


    #(?(<name>)<yes-regex>|<no-regex>)  condional match for named group.

    regex = r'^(?P<ch>\W)?foo(?(ch)(?P=ch)|)$'

    print(re.search(regex, 'foo'))

    print(re.search(regex, '#foo#'))

    print(re.search(regex, '@foo@'))
    print(re.search(regex, '@foo#'))

    print(re.search(regex, 'foo@'))


    #Lookahead and Lookbehind Assertions

    #(?=<lookahead_regex>)  Creates a positive lookahead assertion.

    #The lookahead assertion (?=[a-z]) specifies that what follows 'foo' must be a lowercase alphabetic character. In this case, its the character 'b', so a match is found

    print(re.search('foo(?=[a-z])', 'foobar'))

    #Whats unique about a lookahead is that the portion of the search string that matches <lookahead_regex> isnt consumed, and it isnt part of the returned match object.


    #example illustrating how a lookahead differs from a conventional regex.

    print(re.search('foo([a-z])', 'foobar'))


    #The first portion of the regex, foo, matches and consumes 'foo' from the search string 'foobar'.
    #The next portion, (?=[a-z]), is a lookahead that matches 'b', but the parser doesnt advance past the 'b'.
    #Lastly, (?P<ch>.) matches the next single character available, which is 'b', and captures it in a group named ch.

    m = re.search('foo(?=[a-z])(?P<ch>.)', 'foobar')

    
    print(m.group('ch'))

    #As in the first example, the first portion of the regex, foo, matches and consumes 'foo' from the search string 'foobar'.
    #The next portion, ([a-z]), matches and consumes 'b', and the parser advances past 'b'.
    #Lastly, (?P<ch>.) matches the next single character available, which is now 'a'.
    
    m = re.search('foo([a-z])(?P<ch>.)', 'foobar')

    print(m.group('ch'))


    #(?!<lookahead_regex>)  Creates a negative lookahead assertion. (?!<lookahead_regex>) asserts that what follows the regex parsers current position must not match <lookahead_regex>

    print(re.search('foo(?=[a-z])', 'foobar'))

    print(re.search('foo(?![a-z])', 'foobar'))

    print(re.search('foo(?=[a-z])', 'foo123'))

    #(?<=<lookbehind_regex>)  Creates a positive lookbehind assertion. (?<=<lookbehind_regex>) asserts that what precedes the regex parsers current position must match <lookbehind_regex>
    
    print(re.search('(?<=foo)bar', 'foobar'))

    print(re.search('(?<=qux)bar', 'foobar'))
    
    #Theres a restriction on lookbehind assertions that doesnt apply to lookahead assertions. The <lookbehind_regex> in a lookbehind assertion must specify a match of fixed length.

    #print(re.search('(?<=a+)def', 'aaadef'))

    print(re.search('(?<=a{3})def', 'aaadef'))


    #(?<!<lookbehind_regex>) Creates a negative lookbehind assertion.


    print(re.search('(?<!foo)bar', 'foobar'))

    print(re.search('(?<!qux)bar', 'foobar'))

    
 




    #mislaneous metacharacters

    #(?#...)  specifies comment. This allows you to specify documentation inside a regex in Python, which can be especially useful if the regex is particularly long.

    print(re.search('bar(?#This is a comment) *baz', 'foo bar baz qux'))


    # |  Specifies a set of alternatives on which to match. An expression of the form <regex1>|<regex2>|...|<regexn> matches at most one of the specified <regexi> expressions. The regex parser looks at the expressions separated by | in left-to-right order and returns the first match that it finds. The remaining expressions arent tested, even if one of them would produce a longer match:


    print(re.search('foo|bar|baz', 'bar'))

    print(re.search('foo|bar|baz', 'baz'))

    print(re.search('foo|bar|baz', 'quux'))

    print(re.search('foo|grault', 'foograult'))

    print(re.search('(foo|bar|baz)+', 'foofoofoo'))

    print(re.search('(foo|bar|baz)+', 'bazbazbazbaz'))

    print(re.search('(foo|bar|baz)+', 'barbazfoo'))

    



    #regular expression flags

    #re.I or re.IGNORECASE

    print(re.search('a+', 'aaaAAA', re.I))

    print(re.search('[a-z]+', 'aBcDeF'))

    print(re.search('[a-z]+', 'aBcDeF', re.I))



    #re.M or re.MULTILINE Causes start-of-string and end-of-string anchors to match at embedded newlines. ^ matches at the beginning of the string or at the beginning of any line within the string (that is, immediately following a newline). $ matches at the end of the string or at the end of any line within the string (immediately preceding a newline).


    s = 'foo\nbar\nbaz'

    print(s)

    print(re.search('^foo', s))

    print(re.search('^bar', s))

    print(re.search('^baz', s))

    print(re.search('baz$', s))

    print(re.search('bar$', s))

    print(re.search('bar$', s, re.M))

    print(re.search('baz$', s, re.M))

    print(re.search('foo$', s, re.M))        

    print(re.search('^bar', s, re.M))

    print(re.search('^baz', s, re.M))

    print(re.search('^foo', s, re.M))


    #re.S or re.DOTALL Causes the dot (.) metacharacter to match a newline. Remember that by default, the dot metacharacter matches any character except the newline character. The DOTALL flag lifts this restriction:

    print(re.search('foo.bar', 'foo\nbar'))

    print(re.search('foo.bar', 'foo\nbar', re.DOTALL))







    #re.DEBUG Displays debugging information.


    print(re.search('x[123]{2,4}y', 'x222y', re.DEBUG)

    
    #Combining <flags> Arguments in a Function Call

    #re.search('^bar', 'FOO\nBAR\nBAZ', re.I | re.M)

    

    

    
    

    
        


          
    

    