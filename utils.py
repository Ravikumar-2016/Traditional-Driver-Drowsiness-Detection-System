import pygame

def play_alarm(alarm_path):
    pygame.mixer.init()
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load(alarm_path)
        pygame.mixer.music.play(-1)

def stop_alarm():
    if pygame.mixer.get_init() and pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
