# © Voice Assistant- Made by Yuval Simon. For www.bogan.cool

from datetime import datetime

from extentions.schedule import schedule
from extentions.spotify_player import spotify_player
from extentions.funcs import speak, get_audio
from extentions.weather import weather


while True:
    text = get_audio()

    if 'hey Jimmy' in text:
        if 'start Spotify' in text:
            try:
                speak('Starting spotify')
            except:
                pass
            spotify_player('put', 'play')

        elif 'stop Spotify' in text:
            try:
                speak('Stopping spotify')
            except:
                pass
            spotify_player('put', 'pause')

        elif 'play the previous'  in text:
            try:
                speak('Playing the previous song in Spotify')
            except:
                pass
            spotify_player('post', 'previous')

        elif 'play the next' in text:
            try:
                speak('Playing the next song in Spotify')
            except:
                pass
            spotify_player('post', 'next')

        elif 'add to queue' in text:
            try:
                speak('Adding the current song to queue')
            except:
                pass
            spotify_player('get', 'currently-playing')

        elif "I love you" in text:
            speak('I love you too')

        elif "want to be my friend" in text:
            speak("Sure, why not mate?")

        elif 'weather' in text:
            weather()

        elif "today's date" in text:
            try:
                date = datetime.today().strftime('%Y-%m-%d')
                speak(f"Today's date is {date}")
            except:
                print('cant')
                pass

        elif 'time' in text:
            try:
                now = datetime.now()
                time = now.strftime("%H:%M")
                speak(f'The current time is {time}')

            except:
                print('cant')
                pass

        elif 'schedule' in text:
            schedule()

        elif 'close' in text:
            speak("Okey cya")
            break

        else:
            speak('ummmmm, what?')