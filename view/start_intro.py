import pygame

def start_intro():
    # Pygame 초기화 및 인트로 화면 처리
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("인트로 화면")

    running = True
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # 엔터를 누르면 인트로 종료
                    running = False

        # 임시 텍스트 표시
        font = pygame.font.SysFont(None, 55)
        text_surface = font.render("인트로 화면입니다", True, (0, 0, 0))
        screen.blit(text_surface, (250, 300))

        pygame.display.update()

    pygame.quit()
