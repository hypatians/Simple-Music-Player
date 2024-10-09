import pygame
import webbrowser

# Start the pygame
pygame.init()

# Display screen settings
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Music Player")

# Colors
blue = (0, 0, 205)
white = (255, 255, 255)
green = (0, 255, 0)
dark_green = (0, 200, 0)

# Load music
pygame.mixer.music.load("Fikret Kızılok - Ben Gidersem.wav")

# Font types
font_small = pygame.font.Font(None, 20)  # For quote
font_large = pygame.font.Font(None, 40)  # For title


def draw_button(text, x, y, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Calculate the width dynamically based on the text width
    text_surf = font_large.render(text, True, white)
    width, height = text_surf.get_width() + 20, 50  # Add some padding to the width

    # Draw button based on mouse position
    color = green if x + width > mouse[0] > x and y + height > mouse[1] > y else dark_green
    pygame.draw.rect(screen, color, (x, y, width, height))

    if color == green and click[0] == 1 and action is not None:
        action()

    screen.blit(text_surf, (x + (width - text_surf.get_width()) / 2, y + (height - text_surf.get_height()) / 2))


# Music control functions
def play_music():
    pygame.mixer.music.play(-1)  # Play infinite loop


def pause_music():
    pygame.mixer.music.pause()


def unpause_music():
    pygame.mixer.music.unpause()


def stop_music():
    pygame.mixer.music.stop()


def open_youtube():
    url = "https://www.youtube.com/watch?v=BZfG2r9KFb4"
    webbrowser.open(url)


# Main Loop
running = True
while running:
    screen.fill(blue)

    # Draw the buttons
    draw_button('Play', 50, 100, play_music)
    draw_button('Pause', 50, 200, pause_music)
    draw_button('Unpause', 50, 300, unpause_music)
    draw_button('Stop', 50, 400, stop_music)

    # YouTube Button
    draw_button('Click for more information about the artist.', 50, 500, open_youtube)  # YouTube button

    screen.blit(font_large.render("Welcome to the Simple Music Player!", True, white), (350, 100))

    quote = "'Oh Saz when I go you will stay in the world. Please let not my deepest secrets be revealed.' -Aşık Veysel Şatıroğlu"
    text_surface = font_small.render(quote, True, white)
    screen.blit(text_surface,
                (screen_width - text_surface.get_width() - 20, screen_height - text_surface.get_height() - 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
