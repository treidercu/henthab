import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SAVE_FILE = BASE_DIR / "database" / "saves" / "save.json"


def save_game(player):
    SAVE_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(SAVE_FILE, "w", encoding="utf-8") as file:
        json.dump(player, file, ensure_ascii=False, indent=4)

    print("Игра успешно сохранена!")


def load_game():
    if not SAVE_FILE.exists():
        return None

    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as file:
            player = json.load(file)

        return player if isinstance(player, dict) else None

    except (json.JSONDecodeError, OSError):
        print("Ошибка чтения сохранения!")
        return None


def delete_save():
    if SAVE_FILE.exists():
        SAVE_FILE.unlink()
        print("Сохранение удалено!")
    else:
        print("Сохранение не найдено.")
