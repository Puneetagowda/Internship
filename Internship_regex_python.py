#!/usr/bin/env python
# coding: utf-8

# In[25]:


#question 1 
def replace_text(input_string):
    for character in [' ', ',', '.']:
        input_string = input_string.replace(character,':')
    return input_string
    
sample_input = 'Python Exercises, PHP exercises.'
output = replace_text(sample_input)
print(output)


# In[157]:


#question2
import pandas as pd
import re

#provided dict
test = {'SUMMARY': ['hello,world!','XXXXX test', '123four,five,six...']}

#create a dict
df = pd.DataFrame(test)


#to eliminate the unwanted symbols in the given dictionary
#now we shall create a function

def eliminate(symbols):
    eliminate = symbols.apply(lambda x:re.sub(r'[^a-zA-Z\s]|X+','',x))
    
    return eliminate

#after the unwanted symbols are removed they will be amended back to the dataframe or thesummary column
df['SUMMARY'] = eliminate(df['SUMMARY'])

print(df)


# In[159]:


#question 3
import re

#define a function to find the length of atleast four word
def length_word(string):
    #write a regex pattern
    pattern = re.compile(r'\b\w{4,}\b')
    
    #using findall to fetch all the matching words
    len_words = pattern.findall(string)
    
    return len_words

#give the input string

ip_txt = "this is the code to find out atleast four consecutive words"
output = length_word(ip_txt)
print(output)


# In[160]:


#question 4
#i am writing this code just to extract the words with the 
#length of onlyy 3,4 or 5 characters and excluding the rest
import re
def len_words(input_word):
    #the regex pattern to find 3,4 or 5 characters 
    pattern = re.compile(r'\b\w{3,5}\b')
    
    match_words = pattern.findall(input_word)
    return match_words

#giving the example

sample_txt = 'This is the code to find the three,four or five characters only in the sample string'
output = len_words(sample_txt)
print(output)


# In[59]:


#question 5
#i have removed the just parenthesis and the space before the parenthesis
#and not the owrd inside the parenthesis
import re
def eliminate_parenthesis(strings):
    pattern = re.compile(r'\(([^)]*)\)')
    
    final = [pattern.sub(r'\1',string).strip() for string in strings]
    return final

input_txt= ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]

output = eliminate_parenthesis(input_txt)

for line in output:
    print(line)


# In[63]:


#question 6
import re

#read the text from the sample file
file_path = 'insample.txt'
with open(file_path, 'r') as file:
    in_sample_text = file.readlines()

#define a function to remove parenthesis using regex
def exclude_parenthesis(texts):
    pattern = re.compile(r'\(([^)]*)\)')
    result = [pattern.sub('', text).strip() for text in texts]
    return result

#put the sample txt file given in the above defined function to get the desired output
output = exclude_parenthesis(in_sample_text)
print(output)


# In[65]:


#question 7
import re

#input text 
input_text = "ImportanceOfRegularExpressionsInPython"

#in order to split the text into uppercase with regular expression

output = re.findall(r'[A-Z][a-z]*',input_text)

print(output)


# In[67]:


#question 8
import re
def include_spaces(string):
    pattern = re.compile(r'(?<=[a-zA-z])(\d)')
    
    output = pattern.sub(r' \1', string)
    return output

Sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"

#applying the sample text given to the defined function 
result = include_spaces(Sample_text)
print(result)
    


# In[72]:


#question 9 
import re

def include_spaces(string):
    
    pattern = re.compile(r'(?<=[a-z0-9])([A-Z0-9])')
    
    output = pattern.sub(r' \1', string)
    
    return output

sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"

result = include_spaces(sample_text)
print(result)


# In[74]:


#question10
import pandas as pd

#given github link for the csv file
given_github_link = "https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv"

#create the dataframe by extracting/reading the given csv file
df = pd.read_csv(given_github_link)

#extract the first 5 letters from each of the given country and store it as a new column
df['first_five_letters'] = df['Country'].str[:6]

# print the new data frame created
print(df.head())


# In[83]:


#question 11
import re

def match_a_string(input_text):
    pattern = re.compile(r'[a-zA-Z0-9_]+')
    matches = pattern.match(input_text)
    
    if matches:
        print(f'the given text matches the specified pattern.')
    else:
        print(f'the given text doesnt match the pattern')
    

example1 = "Datatrained"
example2 = "$#@%^&!"

match_a_string(example1)
match_a_string(example2)


# In[87]:


#question12
import re

def specific_number(input_txt,specific_no):
    pattern = re.compile(f'{specific_no}')
    match = pattern.match(input_txt)
    
    if match:
        print("the given data starts with the given specific number")
    else:
        print("the given data does'nt start with the specific number")
        

example_1 = "431puneeta"
example_2 = 'muffin19'
example_3 = "421namitha"
specific_no = "431"

specific_number(example_1,specific_no)
specific_number(example_2,specific_no)
specific_number(example_3,specific_no)


# In[90]:


#question 13
import re
def leading_zeros_exclude(ip_address):
    pattern = re.compile(r'\b0+(\d+)\b')
    output = pattern.sub(r'\1', ip_address)
    return output

#examples
zeros_in_ip = "172.342.002.300"
zeros_in_ip1 = "241.123.004.008"
zeros_without_ip = leading_zeros_exclude(zeros_in_ip)
zeros_without_ip1 = leading_zeros_exclude(zeros_in_ip1)

print(zeros_without_ip)
print(zeros_without_ip1)


# In[100]:


#question 14
import re
def fetch_date_from_txtfile(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    #below is the regular expression to match the date string    
    pattern = re.compile(r'([A-Za-z]+ \d{1,2})(?:st|nd|rd|th)? (\d{4})')
    
    matches = pattern.findall(data)
    
    if matches:
        string_date_from_txt = f'{matches[0][0]} {matches[0][1]}'
        return string_date_from_txt
    else:
        return None
    
#examples
file_path = 'intern_date.txt'
string_date_from_txt = fetch_date_from_txtfile(file_path)


if string_date_from_txt:
    print(f'The date extracted from the text file is: {string_date_from_txt}')
    
else:
    print('there is no date string in the text file')
    
    



    
        


# In[103]:


#question 15
import re
def find_literals(string, search_texts):
    words = []
    
    for text in search_texts:
        if re.search(re.escape(text),string):
            words.append(text)
    return words


sample_text = 'The quick brown fox jumps over the lazy dog.'

search_texts = ['horse','fox','dog']

output = find_literals(sample_text,search_texts)

print(f' the words found in the sample text: {output}')


# In[106]:


#question 16
import re
def find_literals_location(string, search_texts):
    match = re.search(re.escape(search_texts),string)
    
    if match:
        string_begin_location = match.start()
        string_end_location = match.end()
        return string_begin_location,string_end_location
    else:
        return None
    
sample_text = 'The quick brown fox jumps over the lazy dog.'

search_texts = 'fox'

output = find_literals_location(sample_text, search_texts)

if output:
    string_begin_location, string_end_location = output
    print(f' the given word is found in the sample text from the position {string_begin_location} to {string_end_location}')
    
else:
    print('the word searched in not found in the specified text.')
          


# In[111]:


#question 17
import re
def sub_strings(string, pattern):
    matches = re.finditer(pattern, string)
    
    locations = [(match.start(),match.end()) for match in matches]
    
    return locations

sample_text = 'Python exercises, PHP exercises, C# exercises'

pattern = 'exercises'

output = sub_strings(sample_text,pattern)

if output:
    print(f'The pattern "{pattern}" is found in the given sample text at the position: ')
    for start, end in output:
        print(f' location starts from {start} and ends at {end}')
else:
    print("the substring is not present in the sample text.")


# In[115]:


#question18
import re
def sub_strings_with_locations(string,pattern):
    matches = re.finditer(pattern,string)
    
    repeatations = [(match.group(),match.start(),match.end()) for match in matches]
    return repeatations

sample_text = "I felt happy because I saw the others were happy and because I knew I should feel happy, but I wasn't really happy."

pattern = 'happy'

output = sub_strings_with_locations(sample_text,pattern)

if output:
    print(f' the substring "{pattern}" is found in the sample text at location: ')
    for repeatations, start, end in output:
        print(f' repeatations: {repeatations}, location of the substring: {start} to {end}')
        
else:
    print("the substring is not found in the sample text")
    
          


# In[119]:


#question19
from datetime import datetime
def change_format_of_date(in_date):
    try:
        obj_date = datetime.strptime(in_date, '%Y-%m-%d')
        
        changed_date = obj_date.strftime('%d-%m-%Y')
        
        return changed_date
    except ValueError:
        return None

in_date = '2023-02-04'

output = change_format_of_date(in_date)

if output:
    print(f' the given date {in_date} is in the format of yyyy-mm-yy which is converted to the format {output} of dd-mm-yyyy.')
else:
          print("the entered date format is invalid.")


# In[120]:


#question20
import re
def decimal_numbers(string):
    pattern = re.compile(r'\b\d+\.\d{1,2}\b')
    matches = pattern.findall(string)
    return matches

sample_text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"

output = decimal_numbers(sample_text)

print(f' the precision of 1 or 2 for the given decimal numbers are {output}')


# In[122]:


#question21
import re
def search_nos_positions(text):
    pattern = re.compile(r'\b\d+\b')
    matches = pattern.finditer(text)
    
    output = [(match.group(),match.start(),match.end()) for match in matches]
    return output

sample_txt = "Age of his father is 54, mother's age is 49 and his age is 21."

final_output = search_nos_positions(sample_txt)

print("in the given text the position of the numbers are: ")
for number, start, end in final_output:
    print(f'Number: {number}, Position: {start} to {end}')


# In[123]:


#question22
import re
def fetch_max_value(text):
    nos = re.findall(r'\b\d+\b',text)
    
    if nos:
        value_max = max(map(int, nos))
        return value_max
    else:
        return None

sample_txt = 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'

output = fetch_max_value(sample_txt)

if output is not None:
    print(f'In the sample text given the max numeric value is: {output}')
else:
    print('There is no numeric value in the sample text.')


# In[124]:


#question23
import re
def include_spaces_btw_captial_words(text):
    altered_txt = re.sub(r'(?<=[a-z])([A-Z])',r' \1',text)
    return altered_txt

sample_text = "RegularExpressionIsAnImportantTopicInPython"

output = include_spaces_btw_captial_words(sample_text)

print(f' the altered text with the space: {output}')


# In[125]:


#question24
import re
def search_sequence(text):
    pattern = re.compile(r'[A-Z][a-z]+')
    matches = pattern.findall(text)
    return matches

sample_text = "The given Code is to find Out the Sequence of the sentence."

output = search_sequence(sample_text)

print(f' Sequences of upper case letters from the sentence followed by their respective lower case: {output}')


# In[126]:


#question25
#code is to remove duplicate words from the sentence.
import re
def remove_duplicates(string):
    pattern = re.compile(r'\b(\w+)(?:\s+\1\b)+',re.IGNORECASE)
    output = pattern.sub(r'\1',string)
    return output

sample_txt = "Hello hello world world"

result = remove_duplicates(sample_txt)

print(f' after removing the sentence will be: {result}')


# In[130]:


#question26
import re
def alphanumeric(input_text):
    pattern = re.compile(r'\w$')
    return bool(pattern.search(input_text))

#Samples
examples = ["Hi156","Muffin!","puneeta"]


for example in examples:
    output = alphanumeric(example)
    print(f' the given example "{example}" has the alphanumeric character at end: {output}')


# In[133]:


#question27
import re
def fetch_words_with_hashtags(text):
    pattern = re.compile(r'#\w+')
    hashtags = pattern.findall(text)
    return hashtags

sample_text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""

output = fetch_words_with_hashtags(sample_text)

print(f' the words extracted from the sentece with hashtags: {output}')


# In[134]:


#question28
import re
def exclude_unwanted_symbols(txt):
    pattern = re.compile(r'<U\+[0-9A-Fa-f]+>')
    filtered_text = pattern.sub('',txt)
    return filtered_text

sample_text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"

output = exclude_unwanted_symbols(sample_text)

print(f'filtered text: {output}')


# In[139]:


#question29
import re
def fetch_dates(file_path):
    with open(file_path,'r') as file:
        data = file.read()
    
    pattern = re.compile(r'\b\d{2}-\d{2}-\d{4}\b')
    dates = pattern.findall(data)
    return dates

#sample file
file_path = 'dob_intern.txt'
sample_text = 'Ron was born on 12-09-1992 and he was admitted to school 15-12-1999.'

output = fetch_dates(file_path)

print(f' The dates fetched from the sample text file is : {output}')


# In[141]:


#question30
import re
def eliminate_words_btw_2_to_4(text):
    pattern = re.compile(r'\b\w{2,4}\b')
    output = pattern.sub('',text)
    return output

sample_text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

result = eliminate_words_btw_2_to_4(sample_text)

print(f' the sentence after removing the words from two to fourth position: {result}')


# In[ ]:




