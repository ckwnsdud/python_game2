import pygame
import os
import sys

# 대사 데이터를 정의한다냥 (배경, 캐릭터, 이름, 대사)
dialogues = [
    {"backgrounds": "black_background.png", "cha": "what.png", "name": "차준영",
     "dialogue": "하아... 너무 힘들다... 아 파이썬 왜 이리 어려운거지"},
    {"backgrounds": "black_background.png", "cha": "default.png", "name": "차준영",
     "dialogue": "(터벅... 터벅...)"},
    {"backgrounds": "black_background.png", "cha": "what.png", "name": "차준영",
     "dialogue": "에휴..."},
    {"backgrounds": "way.png", "cha": "default.png", "name": "차준영",
     "dialogue": "..."},
    {"backgrounds": "way1.png", "cha": "default.png", "name": "차준영",
     "dialogue": "(힐끗)"},
    {"backgrounds": "way2.png", "cha": "default.png", "name": "차준영",
     "dialogue": "(힐끗)"},
    {"backgrounds": "way.png", "cha": "default.png", "name": "차준영",
     "dialogue": "...아무도 없겠지?"},
    {"backgrounds": "way.png", "cha": "default.png", "name": "차준영",
     "dialogue": "후우... 자 그럼..."},
    {"backgrounds": "cha.png", "cha": "default.png", "name": "차준영",
     "dialogue": "(털석)"},
    {"backgrounds": "cha.png", "cha": "default.png", "name": "차준영",
     "dialogue": "(부시럭.. 부시럭...)"},
    {"backgrounds": "cha.png", "cha": "default.png", "name": "차준영",
     "dialogue": "어디에 뒀더라? 음... 여긴가... 설마, 박스가 깔린건... "},
    {"backgrounds": "black_background.png", "cha": "happy.png", "name": "차준영",
     "dialogue": "아, 찾았다 !"},
    {"backgrounds": "black_background.png", "cha": "shy.png", "name": "차준영",
     "dialogue": "오... 오오오 ! 나, 나의....."},
    {"backgrounds": "wow.png", "cha": "lovelove.png", "name": "차준영",
     "dialogue": "상명대 설립 86주년 특별 기획 리미티드 에디션- 수뭉이 탄생 3주년 기념 초회 한정판...!!!"
                 "처음 공개되는 핑크 수뭉이 버전으로 오직 10개만 생산되며"},
    {"backgrounds": "wow.png", "cha": "lovelove.png", "name": "차준영",
     "dialogue": "수뭉이 생일 6개월 전부터 치밀한 예약 전쟁이...! 크흑...! 아x묭 콘서트 잡기보다 어려웠다고! "
                 "선착순 10명에게만 제공되는 이 선배송의 혜택...!"},
    {"backgrounds": "wow.png", "cha": "lovelove.png", "name": "차준영",
     "dialogue": "쓰읍... 하아. 킁킁... 이 영롱한 자태... 너무 아름다워...! "
                 "학교로 밖에 배송되지 않아서 고민했는데, 사길... 잘했다!"},
    {"backgrounds": "wow.png", "cha": "verycry.png", "name": "차준영",
     "dialogue": "아아... 너무 아름다워서 눈물이 날 것만 같아..."},
    {"backgrounds": "black_background.png", "name":" ",
     "dialogue": "웅성... 웅성..."},
    {"backgrounds": "ele.png","name":" ",
     "dialogue": "띵 !"},
    {"backgrounds": "ele2.png","name":" ",
     "dialogue": "저벅... 저벅..."},
    {"backgrounds": "ele2.png", "min": "angry.png", "name": "민경록",
     "dialogue": "...아니 들어보라고. 아 진짜, 아... 진짜 어떻게 나즈나보다 사기가 어렵냐? 하"},

]

# 대사 줄바꿈 처리 함수
def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = []

    for word in words:
        current_line.append(word)
        # 현재 라인의 길이를 계산
        width, _ = font.size(' '.join(current_line))
        if width > max_width:
            # 줄이 너무 길면 마지막 단어를 다음 줄로 넘김
            current_line.pop()
            lines.append(' '.join(current_line))
            current_line = [word]

    lines.append(' '.join(current_line))
    return lines

def start_intro(screen):
    # 기본 설정
    pygame.init()
    font = pygame.font.Font(os.path.join('assets', 'pont','Galmuri14.ttf'), 20)

    # 대화창 이미지 불러오기
    dialogue_box_image = pygame.image.load(os.path.join('assets', 'images', 'dialogue_box.png'))

    # 현재 대사와 상황
    dialogue_index = 0
    current_letter = 0
    show_all_text = False  # 한 번에 다 보여주기 위한 플래그
    clock = pygame.time.Clock()

    while dialogue_index < len(dialogues):
        screen.fill((0, 0, 0))  # 화면 초기화

        portrait_image = None

        # 대화 상황 불러오기
        current_dialogue = dialogues[dialogue_index]
        background_image = pygame.image.load(os.path.join('assets', 'images','backgrounds',  'stage1_intro',current_dialogue['backgrounds']))
        if 'cha' in current_dialogue:
            portrait_image = pygame.image.load(
                os.path.join('assets', 'images', 'portrait', 'cha', current_dialogue['cha']))
        elif 'min' in current_dialogue:
            portrait_image = pygame.image.load(
                os.path.join('assets', 'images', 'portrait', 'min', current_dialogue['min']))
        elif 'jeong' in current_dialogue:
            portrait_image = pygame.image.load(
                os.path.join('assets', 'images', 'portrait', 'jeong', current_dialogue['jeong']))
        elif 'my' in current_dialogue:
            portrait_image = pygame.image.load(
                os.path.join('assets', 'images', 'portrait', 'my', current_dialogue['my']))

        name = current_dialogue['name']
        dialogue = current_dialogue['dialogue']

        # 배경 그리기
        screen.blit(background_image, (0, 0))

        # 대화창과 초상화 그리기
        screen.blit(dialogue_box_image, (0, 365))  # 대화창 위치 설정
        if portrait_image is not None:
            screen.blit(portrait_image, (7, 381))  # 초상화 위치 설정

        # 캐릭터 이름 출력
        name_surface = font.render(name, True, (255, 255, 255))
        screen.blit(name_surface, (240, 415))  # 이름 위치 설정

        # 대사 출력 (줄바꿈 처리)
        max_width = 500  # 대사창 가로 길이에 맞게 설정
        max_lines = 3  # 대화창에 표시될 최대 줄 수

        if not show_all_text:
            current_letter += 1

        wrapped_text = wrap_text(dialogue[:current_letter], font, max_width)

        for i, line in enumerate(wrapped_text[:max_lines]):
            line_surface = font.render(line, True, (255, 255, 255))
            screen.blit(line_surface, (230, 470 + i * 30))  # 대사 위치 (줄마다 Y 위치 변경)

        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                if show_all_text:  # 대사 전체가 이미 출력되었으면 다음 대사로 넘어감
                    dialogue_index += 1
                    current_letter = 0
                    show_all_text = False
                else:
                    show_all_text = True  # 한 번에 대사 전부 출력

        # 대사가 모두 출력되면 대사 넘기기 플래그 설정
        if current_letter >= len(dialogue):
            show_all_text = True

        pygame.display.update()
        clock.tick(40)  # 프레임 속도 조절

    pygame.quit()
