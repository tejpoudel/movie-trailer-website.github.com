import fresh_tomatoes #import fresh_tomatoes.py file to make the program responsive.
import media #import the media class which has been created outside of this page.

#Define and assign the value for the favorite movies.
titanic = media.Favorite_Movies("Titanic", #Movie title.
                      " American epic romance-disaster film.", #Movie description.
                      "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg", #Movie image or cover photo.
                      "https://youtu.be/kVrqfYjkTdQ") #Movie url to get trailer for the trailer website.

sully = media.Favorite_Movies("Sully",
                              "American biographical drama film.",
                              "https://upload.wikimedia.org/wikipedia/en/8/82/Sully_xxlg.jpeg",
                              "https://www.youtube.com/watch?v=mjKEXxO2KNE&t=1s")
                              
boss_baby = media.Favorite_Movies("Boss Baby",
                                 "A 2017 American computer-animated comedy film.",
                                 "https://upload.wikimedia.org/wikipedia/en/0/0e/The_Boss_Baby_poster.jpg",
                                 "https://youtu.be/wfvxTyFJOiU")

pashupati_prasad = media.Favorite_Movies("Pashupati Prasad",
                                       "A tipical Nepali Movie",
                                       "https://upload.wikimedia.org/wikipedia/en/f/f9/Pashupatiprasadposter.jpg",
                                       "https://www.youtube.com/watch?v=O3GRxW9IkTg")

school_of_rock = media.Favorite_Movies("Schol of Rock",
                                     "Using rock music to learn",
                                     "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                                     "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Favorite_Movies("Ratatouille",
                                  "A rat is a chef in Paris",
                                  "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                                  "https://www.youtube.com/watch?v=1yKqLNnxGZw")

midnight_in_paris = media.Favorite_Movies("MidNight in Paris",
                                        "Going back in time to meet authors",
                                        "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                        "https://www.youtube.com/watch?v=dtiklALGz20")

the_ramayana = media.Favorite_Movies("The Ramayana",
                                     "The Hundu's Regious Movie.",
                                     "https://upload.wikimedia.org/wikipedia/en/7/7c/Ramayana%2C_The_Legend_of_Prince_Rama.jpg",
                                     "https://youtu.be/_anVRcdashk")

on_the_way_to_school = media.Favorite_Movies("On The Way to School",
                                             "A documentary follows four kids heading to school in four corners of the globe.",
                                             "https://static01.nyt.com/images/2015/02/06/arts/06ONTHEWAY/ONTHEWAY-master1050.jpg",
                                             "https://www.youtube.com/watch?v=eIsQ0B43Q9Y")
                                
#Make a list of favorite movies which have already defined and assign values.
favorite_movies = [titanic, sully, boss_baby, pashupati_prasad, the_ramayana, on_the_way_to_school, school_of_rock, ratatouille, midnight_in_paris]
#open the movies lists. 
fresh_tomatoes.open_movies_page(favorite_movies)
