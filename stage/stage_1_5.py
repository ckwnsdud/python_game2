import pygame
import sys
import os

pygame.init()

# 화면 설정
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("스테이지 1.5")

# 이미지 불러오기
background = pygame.image.load(os.path.join('assets', 'images', 'backgrounds', 'stage1_5.png'))
dialogue_box_image = pygame.image.load(os.path.join('assets', 'images', 'dialogue_box.png'))


# 폰트 설정 (커스텀 폰트 경로)
font_path = os.path.join('assets', 'fonts', 'Galmuri14.ttf')  # 폰트 파일 경로
font = pygame.font.Font(font_path, 36)

# 대화 상태 변수
is_dialogue_active = False
current_dialogue_index = 0  # 현재 대화의 인덱스
current_object = None  # 현재 클릭된 오브젝트

# 오브젝트 정보 (이미지, 위치, 이벤트)
objects = [
    {"image": pygame.image.load(os.path.join('assets', 'images', 'objects', 'lock.png')), "pos": (297, 230)},
    {"image": pygame.image.load(os.path.join('assets', 'images', 'objects', 'album.png')), "pos": (162, 544)},
    {"image": pygame.image.load(os.path.join('assets', 'images', 'objects', 'album2.png')), "pos": (688, 512)},
    {"image": pygame.image.load(os.path.join('assets', 'images', 'objects', 'calendar.png')), "pos": (308, 510)},
    {"image": pygame.image.load(os.path.join('assets', 'images', 'objects', 'calendar2.png')), "pos": (450, 550)},
    {"image": pygame.image.load(os.path.join('assets', 'images', 'objects', 'nazna.png')), "pos": (450, 500)},
    {"image": pygame.image.load(os.path.join('assets', 'images', 'objects', 'memo.png')), "pos": (610, 328)}
]


def dialogue_lock():
    dialogues = [
        {"name": "차준영", "portrait": "char1.png", "dialogue": "음 비밀번호를 입력하면 문이 열릴 것 같은데..."},
        {"name": "차준영", "portrait": "char3.png", "dialogue": "단서를 찾아보자"}
    ]
    return dialogues


def dialogue_album():
    dialogues = [
        {"name": "", "dialogue": "민경록의 앨범이다"},
        {"name": "차준영", "portrait": "char3.png", "dialogue": "으... 보기 싫어"},
        {"name": "차준영", "portrait": "char3.png", "dialogue": "음? 이게 뭐지..."},
        {"name": "", "dialogue": "민경록이 나즈나, 수뭉이와 찍은 사진이다"},
        {"name": "차준영", "portrait": "char3.png", "dialogue": "우웨엑..."}
    ]
    return dialogues


def dialogue_album2():
    dialogues = [
        {"name": "", "dialogue": "수뭉이의 앨범이다"},
        {"name": "차준영", "portrait": "char3.png", "dialogue": "역시 수뭉이는 귀여웟...!"}
    ]
    return dialogues


def dialogue_calendar():
    dialogues = [
        {"name": "", "dialogue": "민경록이 쓰는 달력이다."},
        {"name": "", "dialogue": "9월 1일에 동그라미가 쳐져있다"},
        {"name": "차준영", "portrait": "char3.png", "dialogue": "생일 따위 알고싶지 않아..."}
    ]
    return dialogues


def dialogue_calendar2():
    dialogues = [
        {"name": "차준영", "portrait": "char1.png", "dialogue": "이건..."},
        {"name": "", "portrait": "char3.png", "dialogue": "민경록이 만든 수뭉이 전용 달력이다..."},
        {"name": "차준영", "portrait": "char1.png", "dialogue": "진짜 극혐"},
        {"name": "", "portrait": "char1.png", "dialogue": "수뭉이의 생일인 11월 28일에 동그라미가 쳐져있다"},
        {"name": "", "portrait": "char1.png", "dialogue": "...다른 페이지에는 알 수 없는 곳에 하트가 쳐져있다"}

    ]
    return dialogues


def dialogue_nazna():
    dialogues = [
        {"name": "차준영", "portrait": "char1.png", "dialogue": "으아... 이게 뭐야?"},
        {"name": "", "dialogue": "경록이의 최애, 나즈나 인형이다"},
        {"name": "차준영", "portrait": "char1.png", "dialogue": "으 극혐..."},
        {"name": "차준영", "portrait": "char1.png", "dialogue": "엇 뒤에 뭐가 달려있네"},
        {"name": "", "dialogue": "인형 뒤에는 9월 23일 이라 적혀있다"}

    ]
    return dialogues


def dialogue_memo():
    dialogues = [
        {"name": "차준영", "portrait": "char1.png", "dialogue": "흠... 메모가 있네"},
        {"name": "차준영", "portrait": "char3.png", "dialogue": "경..록이가 좋아하는 건..?"},
        {"name": "차준영", "portrait": "char3.png", "dialogue": "뭔, 누가 해둔거야?"}
    ]
    return dialogues


def lock_event():
    print("비밀번호를 입력해야 합니다!")


# 오브젝트 크기 설정
original_sizes = [obj["image"].get_size() for obj in objects]
small_sizes = [(int(size[0] * 0.8), int(size[1] * 0.8)) for size in original_sizes]  # 90% 크기


# 게임 루프
running = True
while running:
    screen.blit(background, (0, 0))  # 배경 그리기

    mouse_pos = pygame.mouse.get_pos()  # 마우스 위치

    for i, obj in enumerate(objects):
        obj_image = obj["image"]
        obj_rect = obj_image.get_rect(topleft=obj["pos"])

        # 마우스가 오브젝트 위에 있으면 작아진 이미지로 그리기
        if obj_rect.collidepoint(mouse_pos):
            resized_image = pygame.transform.scale(obj_image, small_sizes[i])
            resized_rect = resized_image.get_rect(center=obj_rect.center)
            screen.blit(resized_image, resized_rect)
        else:
            screen.blit(obj_image, obj_rect)  # 원래 크기로 그리기

        # 대화창 표시
        if is_dialogue_active and current_object is not None:
            dialogue_info = current_object["dialogues"][current_dialogue_index]

            # 대화창 그리기 (상단으로 이동)
            screen.blit(dialogue_box_image, (0, 0))  # 대화창 상단에 그리기

            # 이름 출력 (상단으로 이동)
            name_text = font.render(dialogue_info["name"], True, (255, 255, 255))
            screen.blit(name_text, (50, 50))  # 이름을 화면 상단에 배치

            # 초상화 출력 (상단으로 이동)
            portrait_image = pygame.image.load(os.path.join('assets', 'images', 'portrait','char', dialogue_info["portrait"]))
            screen.blit(portrait_image, (10, 10))  # 초상화를 상단에 배치

            # 대화 출력 (상단으로 이동)
            dialogue_text = font.render(dialogue_info["dialogue"], True, (255, 255, 255))
            screen.blit(dialogue_text, (50, 100))  # 대사 텍스트 상단에 배치

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for obj in objects:
                    obj_rect = obj["image"].get_rect(topleft=obj["pos"])
                    if obj_rect.collidepoint(mouse_pos):
                        # 오브젝트별로 다르게 처리
                        if obj["event"] == "album":
                            current_object = {"dialogues": dialogue_album()}  # 앨범 대화
                            is_dialogue_active = True
                            current_dialogue_index = 0
                        elif obj["event"] == "calendar":
                            current_object = {"dialogues": dialogue_calendar()}  # 달력 대화
                            is_dialogue_active = True
                            current_dialogue_index = 0
                        elif obj["event"] == "lock":
                            lock_event()  # lock 오브젝트는 특별 행동 실행

            # 스페이스바를 눌러 대화 진행
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and is_dialogue_active and current_object is not None:
                    current_dialogue_index += 1  # 다음 대화로 넘어감

                    # 모든 대화를 출력한 경우 대화 종료
                    if current_dialogue_index >= len(current_object["dialogues"]):
                        is_dialogue_active = False  # 대화창 비활성화
                        current_object = None  # 현재 오브젝트 초기화

        pygame.display.update()