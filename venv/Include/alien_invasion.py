import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from button import Button
import game_functions as gf

def run_game():
    # Initialize game, settings, and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the play button
    play_button = Button(ai_settings, screen, "Play")

    # Make a ship, group of bullets, and group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Create an instance to store statistics and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Set the background color
    bg_color = (230, 230, 230)

    # Start the main loop for the game
    while True:

        # Check for events in game
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            # Updates ship
            ship.update()
            # Updates bullets
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            # Updates aliens
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        # Redraw the screen during each pass through the loop
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()