import pygame
import random
import json
import os

pygame.init()
pygame.mixer.init()

BASE_PATH = os.path.join('.venv')


class Tetris:
    def __init__(self):
        with open(os.path.join(BASE_PATH, 'config.json'), 'r', encoding='utf-8') as f:
            self.config = json.load(f)

        highscores_path = os.path.join(BASE_PATH, 'highscores.json')
        try:
            with open(highscores_path, 'r', encoding='utf-8') as f:
                self.highscores = json.load(f)
        except FileNotFoundError:
            self.highscores = []
            self.save_highscores()

        self.block_size = self.config['window']['block_size']
        self.grid_width = self.config['window']['grid_width']
        self.grid_height = self.config['window']['grid_height']
        self.screen_width = self.block_size * (self.grid_width + 6)
        self.screen_height = self.block_size * self.grid_height

        self.colors = {name: tuple(rgb) for name, rgb in self.config['colors'].items()}
        self.shapes = self.config['shapes']

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Тетрис')
        self.clock = pygame.time.Clock()
        self.state = 'nick_input'
        self.running = True
        self.menu_items = ['Начать игру', 'Таблица рекордов', 'Справка', 'Выход']
        self.selected_item = 0
        self.nickname = ''
        self.menu_alpha = 0

        self.background_music = pygame.mixer.Sound(os.path.join(BASE_PATH, 'assets', 'music', 'background.mp3'))
        self.drop_sound = pygame.mixer.Sound(os.path.join(BASE_PATH, 'assets', 'sounds', 'drop.wav'))
        self.clear_sound = pygame.mixer.Sound(os.path.join(BASE_PATH, 'assets', 'sounds', 'clear.wav'))
        self.gameover_sound = pygame.mixer.Sound(os.path.join(BASE_PATH, 'assets', 'sounds', 'gameover.wav'))
        self.rotate_sound = pygame.mixer.Sound(os.path.join(BASE_PATH, 'assets', 'sounds', 'rotate.wav'))
        self.background_music.set_volume(0.5)
        self.background_music.play(-1)

    def save_highscores(self):
        try:
            with open(os.path.join(BASE_PATH, 'highscores.json'), 'w', encoding='utf-8') as f:
                json.dump(self.highscores, f, ensure_ascii=False, indent=4)
            print(f"Highscores saved: {self.highscores}")
        except Exception as e:
            print(f"Error saving highscores: {e}")

    def reset_game(self):
        self.grid = [[0 for _ in range(self.grid_width)] for _ in range(self.grid_height)]
        self.current_piece = self.new_piece()
        self.game_over = False
        self.score = 0
        self.fall_time = 0
        self.fall_speed = self.config['levels'][0]['fall_speed']
        self.piece_y_offset = 0
        self.clearing_lines = []
        self.clear_animation_time = 0

    def new_piece(self):
        shape_idx = random.randint(0, len(self.shapes) - 1)
        return {
            'shape': self.shapes[shape_idx]['layout'],
            'color': self.colors[self.shapes[shape_idx]['color']],
            'x': self.grid_width // 2 - len(self.shapes[shape_idx]['layout'][0]) // 2,
            'y': 0
        }

    def valid_move(self, piece, x, y):
        for i in range(len(piece['shape'])):
            for j in range(len(piece['shape'][0])):
                if piece['shape'][i][j]:
                    new_x = x + j
                    new_y = int(y + i)
                    if (new_x < 0 or new_x >= self.grid_width or
                            new_y >= self.grid_height or
                            (new_y >= 0 and self.grid[new_y][new_x])):
                        return False
        return True

    def merge_piece(self):
        for i in range(len(self.current_piece['shape'])):
            for j in range(len(self.current_piece['shape'][0])):
                if self.current_piece['shape'][i][j]:
                    y = int(self.current_piece['y'] + i)
                    x = self.current_piece['x'] + j
                    if 0 <= y < self.grid_height and 0 <= x < self.grid_width:
                        self.grid[y][x] = self.current_piece['color']
        self.drop_sound.play()

    def clear_lines(self):
        self.clearing_lines = []
        for i in range(self.grid_height):
            if all(self.grid[i]):
                self.clearing_lines.append(i)
        if self.clearing_lines:
            self.clear_animation_time = 20
            self.clear_sound.play()
        self.score += len(self.clearing_lines) * self.config['scoring']['points_per_line']

    def finish_clearing(self):
        for i in sorted(self.clearing_lines, reverse=True):
            del self.grid[i]
            self.grid.insert(0, [0 for _ in range(self.grid_width)])
        self.clearing_lines = []

    def rotate_piece(self):
        original_shape = self.current_piece['shape']
        n = len(original_shape)
        m = len(original_shape[0])
        rotated = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            for j in range(m):
                rotated[j][n - 1 - i] = original_shape[i][j]

        old_shape = self.current_piece['shape']
        self.current_piece['shape'] = rotated
        if not self.valid_move(self.current_piece, self.current_piece['x'],
                               self.current_piece['y'] + self.piece_y_offset / self.block_size):
            self.current_piece['shape'] = old_shape
        else:
            self.rotate_sound.play()

    def draw_grid(self):
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                if self.grid[y][x] and y not in self.clearing_lines:
                    pygame.draw.rect(self.screen, self.grid[y][x],
                                     [x * self.block_size, y * self.block_size, self.block_size - 1,
                                      self.block_size - 1])

        if self.clearing_lines and self.clear_animation_time > 0:
            alpha = int(255 * (self.clear_animation_time / 20))
            for y in self.clearing_lines:
                for x in range(self.grid_width):
                    color = list(self.grid[y][x])
                    color.append(alpha)
                    s = pygame.Surface((self.block_size - 1, self.block_size - 1), pygame.SRCALPHA)
                    s.fill(tuple(color))
                    self.screen.blit(s, (x * self.block_size, y * self.block_size))

        for i in range(len(self.current_piece['shape'])):
            for j in range(len(self.current_piece['shape'][0])):
                if self.current_piece['shape'][i][j]:
                    pygame.draw.rect(self.screen, self.current_piece['color'],
                                     [(self.current_piece['x'] + j) * self.block_size,
                                      (self.current_piece['y'] + i) * self.block_size + self.piece_y_offset,
                                      self.block_size - 1, self.block_size - 1])

    def draw_menu(self):
        font = pygame.font.Font(None, 36)
        for i, item in enumerate(self.menu_items):
            color = self.colors['yellow'] if i == self.selected_item else self.colors['white']
            text = font.render(item, True, color)
            text.set_alpha(self.menu_alpha)
            self.screen.blit(text, (self.screen_width // 2 - text.get_width() // 2,
                                    self.screen_height // 2 - 50 + i * 40))

    def draw_help(self):
        font = pygame.font.Font(None, 28)
        lines = self.config['help'].split('\n')
        for i, line in enumerate(lines):
            text = font.render(line, True, self.colors['white'])
            self.screen.blit(text, (20, 20 + i * 30))
        back_text = font.render('Нажмите ESC для возврата', True, self.colors['yellow'])
        self.screen.blit(back_text, (self.screen_width // 2 - back_text.get_width() // 2, self.screen_height - 40))

    def draw_highscores(self):
        font = pygame.font.Font(None, 36)
        title = font.render('Таблица рекордов', True, self.colors['white'])
        self.screen.blit(title, (self.screen_width // 2 - title.get_width() // 2, 50))

        font = pygame.font.Font(None, 30)
        for i, entry in enumerate(sorted(self.highscores, key=lambda x: x['score'], reverse=True)[:5]):
            text = font.render(f"{i + 1}. {entry['name']} - {entry['score']}", True, self.colors['white'])
            self.screen.blit(text, (self.screen_width // 2 - text.get_width() // 2, 100 + i * 40))

        back_text = font.render('Нажмите ESC для возврата', True, self.colors['yellow'])
        self.screen.blit(back_text, (self.screen_width // 2 - back_text.get_width() // 2, self.screen_height - 40))

    def draw_nick_input(self):
        font = pygame.font.Font(None, 48)
        prompt_text = font.render('Введите ваш ник:', True, self.colors['yellow'])
        self.screen.blit(prompt_text,
                         (self.screen_width // 2 - prompt_text.get_width() // 2, self.screen_height // 2 - 100))

        font = pygame.font.Font(None, 36)
        name_text = font.render(self.nickname, True, self.colors['white'])
        pygame.draw.rect(self.screen, self.colors['white'],
                         (self.screen_width // 2 - 100, self.screen_height // 2 + 20, 200, 40), 2)
        self.screen.blit(name_text, (self.screen_width // 2 - name_text.get_width() // 2, self.screen_height // 2 + 25))

        save_text = font.render('Нажмите Enter для продолжения', True, self.colors['green'])
        self.screen.blit(save_text, (self.screen_width // 2 - save_text.get_width() // 2, self.screen_height // 2 + 80))

    def draw_game_ui(self):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Счет: {self.score}', True, self.colors['white'])
        self.screen.blit(score_text, (self.grid_width * self.block_size + 10, 10))

        if self.game_over and not self.clearing_lines:
            font = pygame.font.Font(None, 48)
            game_over_text = font.render('Игра окончена!', True, self.colors['white'])
            self.screen.blit(game_over_text, (self.screen_width // 2 - 100, self.screen_height // 2))

    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_item = (self.selected_item - 1) % len(self.menu_items)
                elif event.key == pygame.K_DOWN:
                    self.selected_item = (self.selected_item + 1) % len(self.menu_items)
                elif event.key == pygame.K_RETURN:
                    if self.selected_item == 0:
                        self.state = 'game'
                        self.reset_game()
                    elif self.selected_item == 1:
                        self.state = 'highscores'
                    elif self.selected_item == 2:
                        self.state = 'help'
                    elif self.selected_item == 3:
                        self.running = False

    def handle_game_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Сохраняем результат перед возвратом в меню
                    self.highscores.append({'name': self.nickname, 'score': self.score})
                    self.save_highscores()
                    self.state = 'menu'
                    self.reset_game()
                elif not self.game_over:
                    if event.key == pygame.K_LEFT:
                        if self.valid_move(self.current_piece, self.current_piece['x'] - 1,
                                           self.current_piece['y'] + self.piece_y_offset / self.block_size):
                            self.current_piece['x'] -= 1
                    elif event.key == pygame.K_RIGHT:
                        if self.valid_move(self.current_piece, self.current_piece['x'] + 1,
                                           self.current_piece['y'] + self.piece_y_offset / self.block_size):
                            self.current_piece['x'] += 1
                    elif event.key == pygame.K_DOWN:
                        if self.valid_move(self.current_piece, self.current_piece['x'],
                                           self.current_piece['y'] + self.piece_y_offset / self.block_size + 1):
                            self.current_piece['y'] += 1
                            self.piece_y_offset = 0
                    elif event.key == pygame.K_UP:
                        self.rotate_piece()

    def handle_help_highscores_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.state = 'menu'

    def handle_nick_input_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and self.nickname:
                    self.state = 'menu'
                elif event.key == pygame.K_BACKSPACE:
                    self.nickname = self.nickname[:-1]
                elif event.key in range(pygame.K_a, pygame.K_z + 1) and len(self.nickname) < 10:
                    self.nickname += chr(event.key).upper()

    def update_game(self):
        if not self.game_over:
            self.fall_time += 1
            if self.fall_time >= self.fall_speed:
                self.fall_time = 0
                self.piece_y_offset += self.block_size / 2

                next_y = self.current_piece['y'] + (self.piece_y_offset + self.block_size / 2) / self.block_size
                if not self.valid_move(self.current_piece, self.current_piece['x'], next_y):
                    self.merge_piece()
                    self.clear_lines()
                    if self.clearing_lines:
                        return
                    self.current_piece = self.new_piece()
                    self.piece_y_offset = 0
                    if not self.valid_move(self.current_piece, self.current_piece['x'], self.current_piece['y']) or any(
                            self.grid[0]):
                        self.game_over = True
                        self.gameover_sound.play()
                        self.highscores.append({'name': self.nickname, 'score': self.score})
                        self.save_highscores()
                elif self.piece_y_offset >= self.block_size:
                    self.current_piece['y'] += 1
                    self.piece_y_offset -= self.block_size

        if self.clearing_lines:
            self.clear_animation_time -= 1
            if self.clear_animation_time <= 0:
                self.finish_clearing()

    def update_menu(self):
        if self.menu_alpha < 255:
            self.menu_alpha += 15

    def run(self):
        while self.running:
            self.screen.fill(self.colors['black'])

            if self.state == 'nick_input':
                self.handle_nick_input_events()
                self.draw_nick_input()
            elif self.state == 'menu':
                self.handle_menu_events()
                self.update_menu()
                self.draw_menu()
            elif self.state == 'game':
                self.handle_game_events()
                self.update_game()
                self.draw_grid()
                self.draw_game_ui()
            elif self.state == 'help':
                self.handle_help_highscores_events()
                self.draw_help()
            elif self.state == 'highscores':
                self.handle_help_highscores_events()
                self.draw_highscores()

            pygame.display.flip()
            self.clock.tick(60)

        if self.state == 'game' and self.game_over:
            pygame.time.wait(2000)
        pygame.quit()


if __name__ == '__main__':
    game = Tetris()
    game.run()