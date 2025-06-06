# 🏆 Sport Records Manager

"Sport Records Manager" — это десктопное приложение для управления записями о спортсменах. Приложение позволяет **добавлять**, **удалять**, **искать записи**, а также загружать данные из базы данных и экспортировать/импортировать их в формате XML. Оно реализовано в архитектуре **MVC** и использует **SQLite** в качестве базы данных.

---

## 🌟 Основные функции приложения

- **Добавление записей:** Ввод информации о новом спортсмене через интерфейс.
- **Удаление записей:** Удаление спортсменов по **ФИО** и/или **виду спорта**.
- **Поиск данных:** Поиск по **ФИО**, **виду спорта** или другим параметрам.
- **Работа с базой данных:** Загрузка данных спортсменов с поддержкой пагинации.
- **Работа с XML:** Импорт и экспорт данных о спортсменах в формате XML.
- **Два режима отображения:** Табличный вид и древовидный вид данных.
- **Простой пользовательский интерфейс:** Стильный и интуитивно понятный дизайн.

---

## 💻 Используемые технологии

- **Язык программирования:** [Python 3.x](https://www.python.org/)
- **UI-библиотека:** [Tkinter](https://docs.python.org/3/library/tkinter.html)
- **База данных:** [SQLite](https://www.sqlite.org/index.html)
- **Работа с XML:** DOM (запись) и SAX (чтение)
- **Архитектура проекта:** [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)

---

## 🚀 Установка и запуск приложения

### Шаг 1: Установить зависимости

Перед запуском убедитесь, что у вас установлены:
1. **[Python](https://www.python.org/downloads/)** версии 3.x.
2. **SQLite** (обычно входит в стандартную библиотеку Python).
3. **Виртуальное окружение** (необязательно, но рекомендуется).

---

### Шаг 2: Настройка базы данных

При первом запуске приложение автоматически создаст базу данных `records.db` в корневой директории проекта. Если вы хотите изменить имя базы данных, обновите строку подключения в файле `MVC/model/database.py`:

```python
self.conn = sqlite3.connect("records.db")
```

Таблица будет создана автоматически при первом запуске. Если вы хотите создать таблицу вручную, используйте следующий SQL-запрос:

```sql
CREATE TABLE records (
    id INTEGER PRIMARY KEY,
    fio TEXT NOT NULL,
    composition TEXT NOT NULL,
    position TEXT NOT NULL,
    titles INTEGER NOT NULL,
    sport_type TEXT NOT NULL,
    rank TEXT NOT NULL
);
```

---

### Шаг 3: Установка зависимостей

Если вы используете виртуальное окружение, активируйте его и установите зависимости:

```bash
python -m venv .venv
source .venv/bin/activate  # Для Linux/MacOS
.venv\Scripts\activate     # Для Windows
```

Зависимости не требуются, так как приложение использует только стандартные библиотеки Python.

---

### Шаг 4: Запуск приложения

1. Склонируйте проект и перейдите в его директорию:
   ```bash
   git clone https://github.com/showmeurback/PPOIS-fourth-semestr/blob/main/Lab2
   cd Lab2
   ```
2. Запустите приложение:
   ```bash
   python app.py
   ```

---

## 📂 Структура проекта

### Директории

- `MVC/model` — модели данных и работа с базой данных.
- `MVC/view` — представления (интерфейсы пользователя).
- `MVC/controller` — контроллеры для обработки логики.
- `app.py` — точка входа приложения.

### Основные файлы

#### Модели
- [`record.py`](MVC/model/record.py) — модель данных для записи о спортсмене.
- [`database.py`](MVC/model/database.py) — работа с базой данных SQLite.
- [`xml_handler.py`](MVC/model/xml_handler.py) — работа с XML (импорт и экспорт).

#### Представления
- [`main_window.py`](MVC/view/main_window.py) — главное окно программы.
- [`dialog_add_record.py`](MVC/view/dialog_add_record.py) — диалог добавления спортсмена.
- [`dialog_search_record.py`](MVC/view/dialog_search_record.py) — диалог для поиска записей.
- [`dialog_delete_record.py`](MVC/view/dialog_delete_record.py) — диалог для удаления записей.
- [`tree_view.py`](MVC/view/tree_view.py) — древовидное представление данных.

#### Контроллеры
- [`main_controller.py`](MVC/controller/main_controller.py) — основной контроллер.
- [`add_record_controller.py`](MVC/controller/add_record_controller.py) — логика добавления.
- [`search_record_controller.py`](MVC/controller/search_record_controller.py) — логика поиска.
- [`delete_record_controller.py`](MVC/controller/delete_record_controller.py) — логика удаления.
- [`tree_view_controller.py`](MVC/controller/tree_view_controller.py) — логика древовидного представления.

---

## 🎯 Сценарии демонстрации

### 1. Запуск приложения
- При запуске открывается главное окно приложения.
- В главном окне отображаются все доступные записи из базы данных.

### 2. Работа с данными

#### Добавление записей
- Нажмите "Add Record" в меню или на панели инструментов.
- В открывшемся окне заполните данные спортсмена (**ФИО**, **состав**, **позицию**, **титулы**, **вид спорта**, **разряд**).
- Нажмите "Submit" для сохранения.

#### Удаление записей
- Нажмите "Delete Record" в меню или на панели инструментов.
- Укажите критерии удаления (например, **ФИО** или **вид спорта**).
- Нажмите "Delete". Приложение покажет сообщение о количестве удаленных записей.

#### Поиск записей
- Нажмите "Search Record" в меню или на панели инструментов.
- Укажите параметры поиска (например, **ФИО** или **вид спорта**).
- Полученные результаты отобразятся в таблице.

#### Загрузка из базы
- При запуске приложение автоматически загружает данные из базы данных.
- Используйте кнопки пагинации для перехода между страницами.

### 3. Работа с XML
- Экспорт данных: нажмите соответствующую кнопку в меню.
- Импорт данных: выберите XML-файл через диалоговое окно.

### 4. Альтернативное отображение данных
- Нажмите "Tree View" в меню или на панели инструментов.
- Данные будут отображены в виде дерева, где каждый листовой элемент соответствует полю записи.

---

## 👤 Автор

[Павел Кадиков]  
[[GitHub](https://github.com/showmeurback)]  

