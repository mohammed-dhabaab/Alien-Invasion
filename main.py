import pygame
import game_functions
from settings import Settings 
from ship import Ship
from game_stats import GameStats

def run_game():
    # Initialize pygame, settings, and screen object.:-
    pygame.init()
    ai_settings = Settings()

    # Screen proprties:
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) # Setting the width and height of the screen
    pygame.display.set_caption("Alien Invasion") # Setting the title of the window

    # Make a ship, a group of bullets, and a group of aliens:
    ship = Ship(ai_settings, screen)
    bullets = pygame.sprite.Group()   
    aliens = pygame.sprite.Group()

    # Create the fleet of aliens.
    game_functions.create_fleet(ai_settings, screen, ship, aliens)

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)

    # Start the main loop for the game.
    while True:
        game_functions.check_events(ai_settings, screen, ship, bullets)
        
        if stats.game_active:
            ship.update()
            bullets.update()
            game_functions.update_bullets(ai_settings, screen, ship,  aliens, bullets)
            game_functions.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        game_functions.update_screen(ai_settings, screen, ship, bullets, aliens)

    
        
print("\n\n" + "~" * 99)

if __name__ == "__main__":
    run_game()