
from src.services import filter_state


def test_filter_state() -> None:
    transactions: list[dict[str, str | None | float]] = [
        {
            "Дата операции": "16.10.2021 15:16:16",
            "Дата платежа": "16.10.2021",
            "Номер карты": None,
            "Статус": "OK",
            "Сумма операции": -50.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -50.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Переводы",
            "MCC": None,
            "Описание": "Азер Г.",
            "Бонусы (включая кэшбэк)": 0,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 50.0,
        },
        {
            "Дата операции": "15.10.2021 21:25:17",
            "Дата платежа": "16.10.2021",
            "Номер карты": "*7197",
            "Статус": "OK",
            "Сумма операции": -86.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -86.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Местный транспорт",
            "MCC": 4111.0,
            "Описание": "Северо-Западная пригородная пассажирская компания",
            "Бонусы (включая кэшбэк)": 1,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 86.0,
        },
    ]
    assert filter_state(transactions) == [
        {
            "Дата операции": "16.10.2021 15:16:16",
            "Дата платежа": "16.10.2021",
            "Номер карты": None,
            "Статус": "OK",
            "Сумма операции": -50.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -50.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Переводы",
            "MCC": None,
            "Описание": "Азер Г.",
            "Бонусы (включая кэшбэк)": 0,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 50.0,
        }
    ]
