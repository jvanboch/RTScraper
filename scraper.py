from bs4 import BeautifulSoup
import requests
r = requests.get('https://www.rottentomatoes.com/')
soup = BeautifulSoup(r.text, "html.parser")

def name_to_rt_search(name):#replaces spaces with underscore, to format for RT url
  name = name.replace(' ', '_')
  return name.lower()

def get_movie_url(user_input):#provides RT url with desired movie
  name = name_to_rt_search(user_input)
  return 'https://www.rottentomatoes.com/m/{}'.format(name)


def get_movie_rating(user_input): #returns [audience score, critic score]
  url = get_movie_url(user_input)
  r = requests.get(url)
  soup = BeautifulSoup(r.text, "lxml")
  return [soup.find("score-board").attrs["audiencescore"],soup.find("score-board").attrs["tomatometerscore"]]

##tests
print('expect {} to equal dead_pigs'.format(test_name_1))
print('expect {} to equal https://wwww.rottentomatoes.com/m/dead_pigs'.format(get_movie_url('Dead Pigs')))
print(get_movie_rating('Dead Pigs'))