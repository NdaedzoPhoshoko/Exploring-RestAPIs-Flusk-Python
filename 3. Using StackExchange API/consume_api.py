'''Install:
    pip install requests | this package allows us to make requests to webpages
'''
import requests

# get questions from api.stackexchange.com webpage
response = requests.get("https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")

# print(response) # response [200] shows that its working
# print(response.url) # rveals the url of the data
# t(response.json()) # reveal the json data in response
# print('Display all tags of questions:\n', response.json()['items']) # shows the item list that was found in the json data
# print('There are still more question: ', response.json()['has_more'])

# Display a list of questions in the api data and whether they are answered or not
count = 0
for each_item in response.json()['items']:
    count += 1
    print('Question ', str(count) + " : "+ each_item['title'], '\nIs answered: ', each_item['is_answered'], end='\n') # prints the question

print()
# Display those questions which are unanswered, count them individually
count = 0
for each_item in response.json()['items']:
    if each_item['answer_count']==0:
        count+=1
        print("Question "+ str(count) + ": ", each_item['title'], "\n")
print("There are", count, "question unanswered.")

