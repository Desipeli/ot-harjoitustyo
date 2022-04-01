import pygame
import sys
from button import Button
from card import Card
from load_backs import load_backs
from load_cards import load_cards





class Game:

    def __init__(self):

        # 0 = menu, 1 = game table, 2 =enter highscore, 3 = show highscore
        self.game_stage = 0
        pygame.init()
        self.screen = pygame.display.set_mode([1366,768])
        self.font = pygame.font.SysFont("Corbel", 35)

        # buttonlists
        b1 = Button(self.screen, "Play", (100,60), (self.screen.get_width()/2,self.screen.get_height()/2))
        b2 = Button(self.screen, "Highscores", (150,60), (self.screen.get_width()/2,self.screen.get_height()/2+100))
        b3 = Button(self.screen, "Exit", (100,60), (50,self.screen.get_height()- 30))
        self.menu_buttons = [b1, b2, b3]
        

        self.clock = pygame.time.Clock()

        # Lataustestit
        self.cards = load_cards()
        self.backs = load_backs()
        for b in self.backs:
            print(b.v_hand, b.suit)

        self.start_game()

    def start_game(self):

        while True:
            # Events
            self.events()
            # Screen background color green (0, 81, 44)
            self.screen.fill((0, 81, 44))


            # Menu
            if self.game_stage == 0:
                for b in self.menu_buttons:
                    b.draw()


            # Game stage testing
            text_game_stage = self.font.render(f"Game stage: {self.game_stage}", True, (0,0,0))
            self.screen.blit(text_game_stage, (10,10))

            # cardtest
            #self.screen.blit(self.cards[0].image, (200,200))
            #self.screen.blit(self.backs[0].image, (200,400))
            
            pygame.display.flip()
            self.clock.tick(60)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_click(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


    def mouse_click(self, event):
        if self.game_stage == 0:
            # Play
            if event.pos[0] >= self.menu_buttons[0].center[0] and event.pos[0] <= self.menu_buttons[0].center[0]+self.menu_buttons[0].size[0]:
                if event.pos[1] >= self.menu_buttons[0].center[1] and event.pos[1] <= self.menu_buttons[0].center[1]+self.menu_buttons[0].size[1]:
                    self.game_stage = 1
            # Highscore
            if event.pos[0] >= self.menu_buttons[1].center[0] and event.pos[0] <= self.menu_buttons[1].center[0]+self.menu_buttons[1].size[0]:
                if event.pos[1] >= self.menu_buttons[1].center[1] and event.pos[1] <= self.menu_buttons[1].center[1]+self.menu_buttons[1].size[1]:
                    self.game_stage = 3        
            # Exit
            if event.pos[0] >= self.menu_buttons[2].center[0] and event.pos[0] <= self.menu_buttons[2].center[0]+self.menu_buttons[2].size[0]:
                if event.pos[1] >= self.menu_buttons[2].center[1] and event.pos[1] <= self.menu_buttons[2].center[1]+self.menu_buttons[2].size[1]:
                    pygame.quit() 
                    sys.exit()


if __name__ == "__main__":
    Game()