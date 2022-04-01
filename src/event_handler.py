import pygame
import sys

class Events:

    def check_event(self, event, info):
        self.info = info
        self.event = event
        if self.event.type == pygame.MOUSEBUTTONDOWN:
            self.check_clicks()
        if self.event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    def check_clicks(self):
        # Menu
        if self.info.game_stage == 0:
            for b in self.info.menu_buttons:
                if self.check_button(b):
                    if b.text == "Play":
                        # game stage = 1
                        print("play")
                        self.info.game_stage = 1
                        pass
        
        # Game tabel
        if self.info.game_stage == 1:
            pass

    def check_button(self, button):
        if self.event.pos[0] >= button.center[0] and self.event.pos[0] <= button.center[0]+button.size[0]:
            if self.event.pos[1] >= button.center[1] and self.event.pos[1] <= button.center[1]+button.size[1]:
                return True
        return False
