import pygame
import time

# Start the PyGame
pygame.mixer.init()

# Import the music file
pygame.mixer.music.load("HarvestDawn.wav")


# Functions of playing the music
def play_music():
    pygame.mixer.music.play()


def pause_music():
    pygame.mixer.music.pause()


def unpause_music():
    pygame.mixer.music.unpause()


def stop_music():
    pygame.mixer.music.stop()


# Commands
while True:
    print("\nControls of Music Player:")
    print("1. Play the music")
    print("2. Pause the music")
    print("3. Resume the music")
    print("4. Stop the music")
    print("5. Exit")

    choice = input("Make your choice please: ")

    if choice == '1':
        play_music()
    elif choice == '2':
        pause_music()
    elif choice == '3':
        unpause_music()
    elif choice == '4':
        stop_music()
    elif choice == '5':
        print("You are exiting...")
        stop_music()
        break
    else:
        print("Invalid choice,please try again.")

    time.sleep(2)
