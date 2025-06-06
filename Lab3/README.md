---

# 🏆 Tetris Game

"Tetris Game" — это классическая десктопная игра "Тетрис", реализованная на Python с использованием библиотеки Pygame. Приложение позволяет играть в Тетрис, сохранять результаты в таблице рекордов, просматривать правила и управлять игрой через интуитивно понятный интерфейс. Игра поддерживает ввод ника игрока при запуске и автоматическое сохранение результатов в формате JSON.

---

## 🌟 Основные функции приложения

- **Игра в Тетрис:** Управление падающими фигурами с помощью клавиш (стрелки и поворот).
- **Сохранение результатов:** Автоматическая запись имени игрока и набранных очков в таблицу рекордов.
- **Таблица рекордов:** Просмотр лучших результатов с сортировкой по убыванию очков.
- **Справка:** Отображение правил игры.
- **Интерфейс меню:** Навигация между игрой, таблицей рекордов, справкой и выходом.
- **Звуковое сопровождение:** Фоновая музыка и звуковые эффекты для действий в игре.
- **Простой пользовательский интерфейс:** Стильный и удобный дизайн с поддержкой анимации.

---

## 💻 Используемые технологии

- **Язык программирования:** [Python 3.x](https://www.python.org/)
- **UI-библиотека:** [Pygame](https://www.pygame.org/)
- **Хранение данных:** JSON (файл `highscores.json`)
- **Архитектура проекта:** Процедурная с элементами объектно-ориентированного подхода

---

## 🚀 Установка и запуск приложения

### Шаг 1: Установить зависимости

Перед запуском убедитесь, что у вас установлены:
1. **[Python](https://www.python.org/downloads/)** версии 3.x.
2. **Pygame** — библиотека для создания игр.
3. **Виртуальное окружение** (необязательно, но рекомендуется).

Установите Pygame через `pip`:
```bash
pip install pygame
```

---

### Шаг 2: Настройка файлов

При первом запуске приложение автоматически создаст файл `highscores.json` в директории `.venv` для хранения таблицы рекордов. Если файл отсутствует, он будет создан с пустым списком `[]`.

Также требуются:
- **`config.json`** — файл конфигурации игры (размеры поля, цвета, фигуры, правила).
- **Аудиофайлы** — фоновые музыка и звуковые эффекты в `.venv/assets`.

#### Пример структуры директорий
```
Tetris/
├── .venv/
│   ├── main.py
│   ├── config.json
│   ├── highscores.json
│   └── assets/
│       ├── music/
│       │   └── background.mp3
│       └── sounds/
│           ├── drop.wav
│           ├── clear.wav
│           ├── gameover.wav
│           └── rotate.wav
```

#### Пример `config.json`
```json
{
    "window": {
        "block_size": 30,
        "grid_width": 10,
        "grid_height": 20
    },
    "colors": {
        "black": [0, 0, 0],
        "white": [255, 255, 255],
        "cyan": [0, 255, 255],
        "yellow": [255, 255, 0],
        "magenta": [255, 0, 255],
        "red": [255, 0, 0],
        "green": [0, 255, 0],
        "blue": [0, 0, 255],
        "orange": [255, 165, 0]
    },
    "shapes": [
        {"name": "I", "layout": [[1, 1, 1, 1]], "color": "cyan"},
        {"name": "O", "layout": [[1, 1], [1, 1]], "color": "yellow"},
        {"name": "T", "layout": [[1, 1, 1], [0, 1, 0]], "color": "magenta"},
        {"name": "L", "layout": [[1, 1, 1], [1, 0, 0]], "color": "orange"},
        {"name": "J", "layout": [[1, 1, 1], [0, 0, 1]], "color": "blue"},
        {"name": "S", "layout": [[1, 1, 0], [0, 1, 1]], "color": "green"},
        {"name": "Z", "layout": [[0, 1, 1], [1, 1, 0]], "color": "red"}
    ],
    "scoring": {
        "points_per_line": 100
    },
    "levels": [
        {"level": 1, "fall_speed": 50},
        {"level": 2, "fall_speed": 40},
        {"level": 3, "fall_speed": 30}
    ],
    "help": "Правила игры Тетрис:\n1. Фигуры падают сверху вниз.\n2. Используйте стрелки:\n   - Влево/Вправо: перемещение\n   - Вниз: ускорение падения\n   - Вверх: поворот\n3. Заполните линию, чтобы она исчезла.\n4. Игра заканчивается, если фигуры достигают верха."
}
```

---

### Шаг 3: Установка зависимостей

Если используете виртуальное окружение:
```bash
python -m venv .venv
source .venv/bin/activate  # Для Linux/MacOS
.venv\Scripts\activate     # Для Windows
pip install pygame
```

---

### Шаг 4: Запуск приложения

1. Перейдите в директорию проекта:
   ```bash
   cd Tetris
   ```
2. Запустите приложение:
   ```bash
   python .venv/main.py
   ```

---

## 📂 Структура проекта

### Директории

- `.venv/` — корневая директория с основными файлами и ресурсами.
- `.venv/assets/` — звуковые файлы для музыки и эффектов.

### Основные файлы

- [`.venv/main.py`](.venv/main.py) — точка входа приложения, содержит всю логику игры.
- [`.venv/config.json`](.venv/config.json) — конфигурация игры (параметры окна, цвета, фигуры).
- [`.venv/highscores.json`](.venv/highscores.json) — файл для хранения таблицы рекордов.

---

## 🎯 Сценарии демонстрации

### 1. Запуск приложения
- При запуске появляется окно ввода ника.
- Введите имя (например, "PLAYER") и нажмите `Enter` — откроется главное меню.

### 2. Работа с игрой

#### Игра в Тетрис
- Выберите "Начать игру" в меню.
- Управляйте фигурами:
  - **Стрелка влево/вправо** — перемещение.
  - **Стрелка вниз** — ускорение падения.
  - **Стрелка вверх** — поворот фигуры.
  - **Escape** — возврат в меню с сохранением результата.
- Очищайте линии, чтобы набрать очки. Игра заканчивается, если фигуры достигают верха.

#### Просмотр таблицы рекордов
- Выберите "Таблица рекордов" в меню.
- Отображаются до 5 лучших результатов, отсортированных по убыванию очков.

#### Просмотр справки
- Выберите "Справка" в меню.
- Отображаются правила игры из `config.json`.

#### Выход из игры
- Нажмите "Выход" в меню или закройте окно.

### 3. Сохранение результатов
- При завершении игры (естественном или через `Escape`) текущий счёт и ник автоматически сохраняются в `highscores.json`.

---

## 👤 Автор

[Павел Кадиков]  
[[GitHub]([https://github.com/твой_профиль](https://github.com/showmeurback))]  
