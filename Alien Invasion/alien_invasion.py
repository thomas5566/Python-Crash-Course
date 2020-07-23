import pygame
import game_functions as gf

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats

def run_game():
    # Initialize pygame, settings, and screen object
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    ) # create a game window 1200 pixels wide by 800 pixels high

    pygame.display.set_caption("Alien Invasion")

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)

    # Make a shipship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Make a cloud
    # cloud = Cloud(ai_settings.cloud_height, ai_settings.bullet_width, screen)

    # Set the background color
    bg_color = (230, 230, 230)

    # Make an alien
    # alien = Alien(ai_settings, screen)

    # Start the main loop for the game
    while True:
        # game_functions
        gf.check_events(ai_settings, screen, ship, bullets) # checks for player input

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()