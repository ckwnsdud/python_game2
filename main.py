import pygame
import sys
from menu.main_menu import main_menu  # main_menu 함수 불러오기

def main():
    # Pygame 초기화
    pygame.init()

    # 화면 설정
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("민경록, 내 수뭉이 피규어 돌려줘!")

    # 메인 메뉴 함수 호출
    main_menu(screen)  # screen 객체 전달

if __name__ == "__main__":
    main()
