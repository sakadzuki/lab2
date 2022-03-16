import csv
import requests


def words_filter(anime, category, user_choice):
    add_anime = []
    for current_anime in anime:
        anime_choice = True
        for current_choice in user_choice:
            if int(current_anime[category].split(', ').count(current_choice)) != 1:
                anime_choice = False
        if anime_choice == True:
            add_anime.append(current_anime)
    return add_anime


def numbers_filter(anime, category, user_choice):
    add_anime = []
    for current_anime in anime:
        if current_anime[category] != 'Unknown':
            if float(current_anime[category]) >= float(user_choice[0]):
                add_anime.append(current_anime)
    return add_anime


result_anime = list(dict())
with open("anime.csv", encoding='utf8') as file:
    reader = csv.DictReader(file)
    for current_anime in reader:
        result_anime.append(current_anime)
file.close()

print('Какой тип аниме вас интересует?')
user_choice = input().split(', ')
if user_choice != ['']:
    result_anime = words_filter(result_anime, 'Type', user_choice)

print('Вы хотите чтобы аниме было завершено?')
user_choice = input()
if user_choice == 'Да':
    result_anime = words_filter(result_anime, 'Finished', ['True'])
else:
    result_anime = words_filter(result_anime, 'Finished', ['False'])

print('Аниме какой студии вы хотите посмотреть?')
user_choice = input().split(', ')
if user_choice != ['']:
    result_anime = words_filter(result_anime, 'Studios', user_choice)

print('Какие тэги в описании аниме должны присутствовать(перечислите через запятую)?')
user_choice = input().split(', ')
if user_choice != ['']:
    result_anime = words_filter(result_anime, 'Tags', user_choice)

print('Какой минимальный рейтинг должен быть у аниме?')
user_choice = input()
if user_choice != ['']:
    result_anime = numbers_filter(result_anime, 'Rating Score', user_choice)

with open('result_anime.csv', 'w', encoding='utf8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(('Anime-PlanetID', 'Name', 'Alternative Name', 'Rating Score', 'Number Votes', 'Tags',
                     'Content Warning', 'Type', 'Episodes', 'Finished', 'Duration', 'StartYear', 'EndYear',
                     'Season', 'Studios', 'Synopsis', 'Url'))
    for current_anime in result_anime:
        writer.writerow((current_anime['Anime-PlanetID'], current_anime['Name'], current_anime['Alternative Name'],
                         current_anime['Rating Score'], current_anime['Number Votes'], current_anime['Tags'],
                         current_anime['Content Warning'], current_anime['Type'], current_anime['Episodes'],
                         current_anime['Finished'], current_anime['Duration'], current_anime['StartYear'],
                         current_anime['EndYear'], current_anime['Season'], current_anime['Studios'],
                         current_anime['Synopsis'], current_anime['Url']))
file.close()
print("Список аниме находятся в файле result_anime.csv")