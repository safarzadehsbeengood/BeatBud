import PySimpleGUI as sg
from mutagen.mp3 import MP3
from pygame import mixer

play_image = b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAByElEQVRoge3ZMWsUQRjG8Z8RFSKCgoJp0qSJjVpoZ2clkk8g5CtYpU+TD5DSUkvbVCFNYiM2dhZqY6GFQooEISGai8Xu4HgmcnM3c+su+4fj2L2dmedhb+Z95x16enp6hljBxaZF5OAE7/GoaSGTchJ9tnCrWTnjE0zs19+HWMPlJkWNQzAyh2c4rq+/YBnnmpOWRjASuIfX0f0d3GlAVzLDRmBG9Ta+1r8d4wVuTFdaGqcZCVzFOn7Uz+ziKc5PR1oa/zISWMRm9OxbPCisK5lRjASW8Clqs4H5MrLSSTECs1jFQd3ue319KbewVFKNBBbwMmr/EY8z6kpmXCOBh3gX9dNYdjCpEbigWs326r6OVKvdlQn7TSKHkcCcKt4MNJAd5DQSuI83Ud87uJ15jL8oYYTf2cE3f2YH1wuMhXJGAtdU8+WnwtlBaSOBu3gVjZc9O5iWEapJ/wSf6zEHeI6bZzWYmY6u/4v+rzUirZ/snVh+hwPitpYFxNanKJ1IGk9L4xcz6Eom18bqg5ZtrDqx1Y2LDwPVG2lV8aH15aDWF+jOKpkWi8o5GKWIXTwq56BzxwqdOejpxNFbJw5DO3M83dPT02J+AbN50HbYDxzCAAAAAElFTkSuQmCC'
stop_image = b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAAaklEQVRoge3ZQQqAMAxFwSre/8p6AZFUiXzKzLqLPNJVOwYAvLcVzpztU9Q8zrr/NUW3Y+JsZXsdSjdimY0ISSMkjZA0QtIISSMkjZA0QtIISSMkjZA0QtIISSMkzcxrfMo/ya1lNgIAX1zq+ANHUjXZuAAAAABJRU5ErkJggg=='

song = MP3("./307_-_veronica_prodby47.mp3")
length_in_secs = int(song.info.length)
print(f'{song.info.sample_rate} Hz')

mixer.init()
sound = mixer.music.load("./307_-_veronica_prodby47.mp3")
paused = None

# All the stuff inside your window.
layout = [  [sg.Text("BeatBud", font="JetBrainsMono")],
            [sg.ProgressBar(max_value=length_in_secs, key="-PROGRESS_BAR-"), sg.Button(key="-PLAY_PAUSE-", image_data=play_image)],
            [sg.Button('Exit')] ]

# Create the Window
window = sg.Window('BeatBud', layout) 

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == "-PLAY_PAUSE-":
        if paused == None:
            mixer.music.play()
            paused = False
            continue
        if paused:
            mixer.music.unpause()
        else:
            mixer.music.pause()
        paused = not paused

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    window["-PROGRESS_BAR-"].update(mixer.music.get_pos() // 1000)

window.close()

