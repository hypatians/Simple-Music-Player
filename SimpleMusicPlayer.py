import pygame
import time

pygame.mixer.init()

# Load the music file with error handling
try:
    pygame.mixer.music.load("HarvestDawn.wav")
except pygame.error as e:
    print(f"Error loading music file: {e}")
    exit(1)
    
def play_music():
    print("Playing music...")
    pygame.mixer.music.play()

def pause_music():
    print("Pausing music...")
    pygame.mixer.music.pause()

def unpause_music():
    print("Resuming music...")
    pygame.mixer.music.unpause()

def stop_music():
    print("Stopping music...")
    pygame.mixer.music.stop()

def stop_music_and_exit():
    print("Stopping music and exiting...")
    pygame.mixer.music.stop()
    exit(0)

# Map user input to functions
selection_map = {
    '1': play_music,
    '2': pause_music,
    '3': unpause_music,
    '4': stop_music,
    '5': stop_music_and_exit,
}

# Function to handle user selection, 
def handle_selection(choice):
    action = selection_map.get(choice)
    if action:
        return action()  
    else:
        print("Invalid choice, please try again.")

def music_player():
    while True:
        print("\nControls of Music Player:")
        print("1. Play the music")
        print("2. Pause the music")
        print("3. Resume the music")
        print("4. Stop the music")
        print("5. Exit")

        choice = input("Make your choice, please: ")

        running = handle_selection(choice)

        time.sleep(2)

if __name__ == "__main__":
    music_player()
