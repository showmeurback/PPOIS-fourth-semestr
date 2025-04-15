# ✈️ Airplane System

`Airplane System` — это приложение для управления авиакомпанией, реализованное на Python с использованием библиотеки Flask для веб-интерфейса и CLI для текстового управления. Приложение позволяет добавлять самолёты, регистрировать пассажиров и экипаж, управлять взлётными полосами, планировать маршруты, выполнять взлёт и посадку, а также сохранять и загружать состояние самолётов в файлы. Веб-интерфейс стилизован с современным дизайном, обеспечивая удобное взаимодействие через браузер.

---

## 🌟 Основные функции приложения

- **Управление самолётами:** Добавление новых самолётов, выполнение взлёта и посадки.
- **Регистрация пассажиров и экипажа:** Добавление пассажиров с билетами и членов экипажа с ролями.
- **Управление взлётными полосами:** Занятие и освобождение полос.
- **Планирование маршрутов:** Задание начальной и конечной точки полёта.
- **Обслуживание в полёте:** Подача еды и напитков пассажирам.
- **Сохранение и загрузка состояния:** Сериализация состояния самолёта в файлы `.pkl` и их восстановление.
- **Два интерфейса:**
  - **Веб-интерфейс:** Стилизованный интерфейс для управления через браузер.
  - **CLI:** Текстовый интерфейс для управления через консоль.
- **Совместимость данных:** Действия в CLI и веб-интерфейсе синхронизируются через общие классы.

---

## 💻 Используемые технологии

- **Язык программирования:** [Python 3.x](https://www.python.org/)
- **Веб-фреймворк:** [Flask](https://flask.palletsprojects.com/)
- **Шаблонизатор:** [Jinja2](https://jinja.palletsprojects.com/)
- **Хранение данных:** Сериализация объектов в файлы `.pkl` (библиотека `pickle`)
- **Стилизация:** Встроенный CSS для веб-интерфейса
- **Архитектура проекта:** Объектно-ориентированный подход с модульной структурой

---

## 🚀 Установка и запуск приложения

### Шаг 1: Установить зависимости

Перед запуском убедитесь, что у вас установлены:
1. **[Python](https://www.python.org/downloads/)** версии 3.7 или выше.
2. **Flask** и **Werkzeug** — библиотеки для веб-интерфейса.
3. **Виртуальное окружение** (рекомендуется для изоляции зависимостей).

Установите зависимости через `pip`:
```bash
pip install flask==2.3.3 werkzeug==2.3.8
```

---

### Шаг 2: Настройка файлов

Приложение не требует дополнительных конфигурационных файлов. Сохранение состояния самолётов выполняется в файлы `.pkl`, которые создаются автоматически в директории `.venv` при использовании функции сохранения.

Требуемые файлы:
- **Модули Python** — классы для самолётов, пассажиров, экипажа и т.д. (в `.venv\Source\`).
- **Шаблоны HTML** — стилизованные страницы для веб-интерфейса (в `.venv\templates\`).
- **`requirements.txt`** — файл с зависимостями.

#### Пример структуры директорий
```
AirplaneSystem/
├── .venv/
│   ├── Source/
│   │   ├── __init__.py
│   │   ├── airplane.py
│   │   ├── crew.py
│   │   ├── flight_operations.py
│   │   ├── inflight_service.py
│   │   ├── passenger.py
│   │   ├── runway.py
│   │   ├── ticket.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── airplane_details.html
│   │   ├── add_airplane.html
│   ├── cli.py
│   ├── web_app.py
│   ├── requirements.txt
│   ├── Scripts/
│   └── Lib/
```

#### Пример `requirements.txt`
```plaintext
Flask==2.3.3
Werkzeug==2.3.8
```

---

### Шаг 3: Установка зависимостей

Если используете виртуальное окружение:
```bash
python -m venv .venv
# Для Windows:
.venv\Scripts\activate
# Для Linux/MacOS:
source .venv/bin/activate
pip install -r .venv\requirements.txt
```

---

### Шаг 4: Запуск приложения

1. Перейдите в директорию проекта:
   ```bash
   cd AirplaneSystem
   ```

2. Запустите веб-интерфейс:
   ```bash
   python .venv\web_app.py
   ```
   Откройте браузер и перейдите по `http://127.0.0.1:5000/`.

3. Запустите CLI (в отдельной консоли):
   ```bash
   python .venv\cli.py
   ```

---

## 📂 Структура проекта

### Директории

- `.venv\` — корневая директория с кодом приложения и зависимостями.
- `.venv\Source\` — модули Python с классами приложения.
- `.venv\templates\` — HTML-шаблоны для веб-интерфейса.

### Основные файлы

- [`.venv\web_app.py`](.venv/web_app.py) — точка входа для веб-интерфейса, содержит маршруты Flask.
- [`.venv\cli.py`](.venv/cli.py) — точка входа для CLI, реализует текстовое меню.
- [`.venv\Source\airplane.py`](.venv/Source/airplane.py) — класс `Airplane` для управления самолётами.
- [`.venv\Source\passenger.py`](.venv/Source/passenger.py) — класс `Passenger` для пассажиров.
- [`.venv\Source\crew.py`](.venv/Source/crew.py) — класс `Crew` для экипажа.
- [`.venv\Source\runway.py`](.venv/Source/runway.py) — класс `Runway` для взлётных полос.
- [`.venv\Source\ticket.py`](.venv/Source/ticket.py) — класс `Ticket` для билетов.
- [`.venv\Source\flight_operations.py`](.venv/Source/flight_operations.py) — класс `FlightOperations` для планирования маршрутов.
- [`.venv\Source\inflight_service.py`](.venv/Source/inflight_service.py) — класс `InflightService` для обслуживания.
- [`.venv\templates\index.html`](.venv/templates/index.html) — главная страница веб-интерфейса.
- [`.venv\templates\airplane_details.html`](.venv/templates/airplane_details.html) — страница деталей самолёта.
- [`.venv\templates\add_airplane.html`](.venv/templates/add_airplane.html) — страница добавления самолёта.
- [`.venv\requirements.txt`](.venv/requirements.txt) — зависимости проекта.

---

## 🎯 Сценарии демонстрации

### 1. Запуск веб-интерфейса
- Запустите `python .venv\web_app.py`.
- Откройте `http://127.0.0.1:5000/` в браузере.
- Увидите главную страницу с одним самолётом (`Boeing 737`) и одной свободной взлётной полосой.

#### Добавление самолёта
- Нажмите **"Add New Airplane"**.
- Заполните форму:
  - **Model**: `Airbus A320`
  - **Capacity**: `180`
- Нажмите **"Add Airplane"**.
- На главной странице появится новый самолёт: `Airbus A320 - Status: on_ground, Passengers: 0/180`.

#### Управление самолётом
- Кликните на **"Boeing 737"** (перейдёте на `/airplanes/0`).
- **Добавить пассажира**:
  - **Name**: `John Smith`
  - **Flight Number**: `AA123`
  - **Seat**: `12A`
  - Нажмите **"Add Passenger"**.
  - Появится: `John Smith - Flight: AA123, Seat: 12A`.
- **Добавить экипаж**:
  - **Name**: `Anna Brown`
  - **Role**: `Pilot`
  - Нажмите **"Add Crew"**.
  - Появится: `Anna Brown - Pilot`.
- **Взлёт**: Нажмите **"Take Off"** (статус изменится на `in_air`).
- **Посадка**: Нажмите **"Land"** (статус вернётся на `on_ground`).
- **Сохранить состояние**:
  - **Filename**: `boeing737_state.pkl`
  - Нажмите **"Save State"**.

#### Управление взлётной полосой
- На главной странице в разделе "Runways" нажмите **"Occupy"** (статус полосы станет `Occupied`).
- Нажмите **"Free"** (вернётся на `Free`).

#### Планирование маршрута
- В разделе "Flight Operations":
  - **Start**: `Minsk`
  - **Destination**: `Warsaw`
  - Нажмите **"Plan Route"**.
  - В консоли: `Route planned: Minsk -> Warsaw`.

#### Обслуживание в полёте
- В разделе "Inflight Services":
  - Нажмите **"Serve Meal"** (в консоли: `Serving meals to passengers`).
  - Нажмите **"Serve Drinks"** (в консоли: `Serving drinks to passengers`).

#### Загрузка состояния
- В разделе "Load Airplane State":
  - **Filename**: `boeing737_state.pkl`
  - Нажмите **"Load State"**.
  - Новый самолёт (копия Boeing 737) появится в списке.

### 2. Запуск CLI
- Запустите `python .venv\cli.py`.
- Появится текстовое меню с опциями 1–12.

#### Пример взаимодействия
- Выберите **1** (List airplanes) — отобразится список: `0: Boeing 737, Status: on_ground, Passengers: 1/200`, и т.д.
- Выберите **2** (Add passenger):
  - **Airplane index**: `0`
  - **Name**: `Alice Johnson`
  - **Flight Number**: `AA456`
  - **Seat**: `15B`
  - Выведет: `Passenger Alice Johnson has been registered on board`.
- Выберите **4** (Take off):
  - **Airplane index**: `0`
  - Выведет: `Boeing 737 is taking off`.
- Выберите **8** (Save airplane state):
  - **Airplane index**: `0`
  - **Filename**: `boeing737_cli.pkl`
  - Выведет: `State of the airplane has been saved to boeing737_cli.pkl`.
- Выберите **12** (Exit) для завершения.

### 3. Синхронизация веб и CLI
- Добавьте пассажира в CLI (например, `Alice Johnson`).
- Перейдите на сайт (`/airplanes/0`) — увидите `Alice Johnson` в списке пассажиров.
- Сохраните состояние в веб-интерфейсе и загрузите его в CLI — данные сохранятся.

---

## 👤 Автор

[showmeurback]
