from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
from urllib.request import urlretrieve




if __name__ == "__main__":
    user = ('bob', 'code')

    print(f'{user[0]} is a {user[1]}')

    User = namedtuple('User', 'name role')

    user = User(name='bob', role='coder')

    print(f'{user.name} is a {user.role}')

    challenges_done = [('mike', 10), ('julian', 7), ('bob', 5),
                   ('mike', 11), ('julian', 8), ('bob', 6)]


    challenges = {}
    try:
        for name, challenge in challenges_done:
            challenges[name].append(challenge)
    except KeyError as e:
        print(e)

    challenges = defaultdict(list)    
    for name, challenge in challenges_done:
        challenges[name].append(challenge)

    print(challenges)


    words = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been 
the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and 
scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus
PageMaker including versions of Lorem Ipsum""".split()
    print(words[:5])

    commom_words = {}

    print(Counter(words).most_common(5))

    movie_data = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
    movies_csv = 'movies.csv'
    urlretrieve(movie_data, movies_csv)

    Movie = namedtuple('Movie', 'title year score')

    def get_movies_by_director(data=movies_csv):
        directors = defaultdict(list)
        with open(data, encoding='utf-8') as f:
            for line in csv.DictReader(f):
                try:
                    director = line['director_name']
                    movie = line['movie_title'].replace('\xa0', '')
                    year = int(line['title_year'])
                    score = float(line['imdb_score'])
                except ValueError:
                    continue

                m = Movie(title=movie, year=year, score=score)
                directors[director].append(m)
                
        return directors

    directors = get_movies_by_director()

    print(directors['Christopher Nolan'])

    cnt = Counter()
    for director, movies in directors.items():
        cnt[director] += len(movies)

    print(cnt.most_common(5))




