import pygame

class Button(pygame.sprite.Sprite):
    "A clickable button that has an effect on hover, and touch."
    def __init__(self, group, image, pos, size):
        super(Button, self).__init__(group)
        self.image = image
        self.rect = pygame.Rect(pos, size)
    def is_hover(self, event):
        if self.rect.top < event.pos[1] < self.rect.top + self.rect.height:
            if self.rect.left < event.pos[0] < self.rect.left + self.rect.width:
                return True
        return False
    def is_click(self, event):
        if self.is_hover(event) and event.button:
            return True
        else:
            return False
    def on_update(self):
        if self.is_hover(): self.on_hover()
        if self.is_click(): self.on_click()
    def on_hover(self): pass
    def on_click(self): pass
