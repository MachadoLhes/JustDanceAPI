from django.conf import settings
import csv, random

#Threshold fo wheater a current game song is chosen instead of a unlimited song
JD_UNLIMITED_THRESHOLD = 40

def get_random_csv_line(filepath):
    with open(filepath) as f:
        reader = csv.reader(f)
        chosen_row = random.choice(list(reader))
    
    return chosen_row

def get_random_song(isUnlimited):
    if isUnlimited:
        unlimitedProb = random.randint(0,100)
        if unlimitedProb < JD_UNLIMITED_THRESHOLD:
            song = get_random_csv_line(settings.UNLIMITED_SONGS_PATH)
        else:
            song = get_random_csv_line(settings.CURRENT_GAME_SONGS_PATH)
    else:
        song = get_random_csv_line(settings.CURRENT_GAME_SONGS_PATH)
    
    return song

def mount_response_json(song):
    response = {
        'name': song[0],
        'artist': song[1],
        'year': song[2],
        'mode': song[3],
        'game': song[4],
    }

    return response