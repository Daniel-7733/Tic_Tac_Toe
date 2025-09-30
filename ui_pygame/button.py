import pygame
from typing import Optional, Tuple

Color = Tuple[int, int, int]

class Button:
    def __init__(self, screen: pygame.Surface,
        rect: pygame.Rect | Tuple[int, int, int, int],
        text: str,
        font: pygame.font.Font,
        fill: Color = (235, 235, 235),
        text_color: Color = (0, 0, 0),
        border_color: Color = (0, 0, 0),
        border_width: int = 2,
        hover_fill: Optional[Color] = (210, 210, 210)) -> None:

        self.screen = screen
        self.rect = rect if isinstance(rect, pygame.Rect) else pygame.Rect(rect)
        self.text = text
        self.font = font
        self.fill = fill
        self.text_color = text_color
        self.border_color = border_color
        self.border_width = border_width
        self.hover_fill = hover_fill
        self._hovered = False  # internal flag

        # pre-render label once (re-render if text changes)
        self._label = self.font.render(self.text, True, self.text_color)

    def set_text(self, text: str) -> None:
        self.text = text
        self._label = self.font.render(self.text, True, self.text_color)

    def is_hovered(self, mouse_pos: Tuple[int, int]) -> bool:
        return self.rect.collidepoint(mouse_pos)

    def handle_event(self, event: pygame.event.Event) -> bool:
        """Return True if the button was clicked (left mouse)."""
        if event.type == pygame.MOUSEMOTION:
            self._hovered = self.is_hovered(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_hovered(event.pos):
                return True
        return False

    def draw(self) -> None:
        # fill (use hover color if available and hovered)
        fill_color = self.hover_fill if (self._hovered and self.hover_fill) else self.fill
        pygame.draw.rect(self.screen, fill_color, self.rect)
        # border
        if self.border_width > 0:
            pygame.draw.rect(self.screen, self.border_color, self.rect, self.border_width)
        # center text
        label_rect = self._label.get_rect(center=self.rect.center)
        self.screen.blit(self._label, label_rect)
        # update just this area (optional)
        pygame.display.update(self.rect)
