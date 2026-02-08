import doctest


class Pot:
    def __init__(self, capacity: float, material: str, current_fill: float = 0.0):
        """
        Создание и подготовка к работе объекта "Кастрюля".

        :param capacity: Максимальный объем кастрюли в литрах.
        :param material: Материал изготовления (например, "сталь").
        :param current_fill: Текущий объем содержимого в литрах.

        Примеры:
        >>> pot = Pot(5.0, "сталь", 0.0)
        """
        if not isinstance(capacity, (int, float)) or capacity <= 0:
            raise ValueError("Объем кастрюли должен быть положительным числом")
        self.capacity = float(capacity)

        if not isinstance(material, str) or not material:
            raise TypeError("Материал должен быть непустой строкой")
        self.material = material

        if not isinstance(current_fill, (int, float)) or not (0 <= current_fill <= capacity):
            raise ValueError("Содержимое не может быть отрицательным или превышать объем")
        self.current_fill = float(current_fill)

    def add_liquid(self, volume: float) -> None:
        """
        Долить жидкость в кастрюлю.

        :param volume: Объем добавляемой жидкости в литрах.
        :raise ValueError: Если жидкость переливается через край.

        Примеры:
        >>> pot = Pot(3.0, "керамика")
        >>> pot.add_liquid(1.5)
        """
        if not isinstance(volume, (int, float)) or volume < 0:
            raise ValueError("Объем добавляемой жидкости должен быть положительным")
        ...

    def boil_water(self, temperature: int) -> bool:
        """
        Нагреть содержимое до определенной температуры.

        :param temperature: Целевая температура в градусах Цельсия.
        :return: Достигнута ли точка кипения (100°C).

        Примеры:
        >>> pot = Pot(2.0, "эмаль", 1.0)
        >>> pot.boil_water(100)
        """
        if not isinstance(temperature, int):
            raise TypeError("Температура должна быть целым числом")
        ...


class Queue:
    def __init__(self, max_size: int):
        """
        Создание структуры данных "Очередь" с ограничением размера.

        :param max_size: Максимально допустимое количество элементов.

        Примеры:
        >>> my_queue = Queue(max_size=10)
        """
        if not isinstance(max_size, int) or max_size <= 0:
            raise ValueError("Размер очереди должен быть положительным целым числом")
        self.max_size = max_size
        self.current_items_count = 0

    def enqueue(self, item_id: int) -> None:
        """
        Добавить элемент в конец очереди.

        :param item_id: Идентификатор элемента.
        :raise OverflowError: Если очередь заполнена.

        Примеры:
        >>> my_queue = Queue(5)
        >>> my_queue.enqueue(101)
        """
        if not isinstance(item_id, int):
            raise TypeError("ID элемента должен быть целым числом")
        ...

    def dequeue(self) -> int:
        """
        Извлечь элемент из начала очереди.

        :return: Идентификатор извлеченного элемента.

        Примеры:
        >>> my_queue = Queue(5)
        >>> # my_queue.dequeue()
        """
        ...


class Subscription:
    def __init__(self, service_name: str, monthly_cost: float, is_active: bool = True):
        """
        Управление подпиской на сервис.

        :param service_name: Название сервиса.
        :param monthly_cost: Стоимость в месяц.
        :param is_active: Активна ли подписка.

        Примеры:
        >>> sub = Subscription("Yandex Plus", 299.0, True)
        """
        if not isinstance(service_name, str):
            raise TypeError("Название сервиса должно быть строкой")
        self.service_name = service_name

        if not isinstance(monthly_cost, (int, float)) or monthly_cost < 0:
            raise ValueError("Стоимость не может быть отрицательной")
        self.monthly_cost = float(monthly_cost)

        self.is_active = is_active

    def cancel_subscription(self) -> bool:
        """
        Отменить текущую подписку.

        :return: True если успешно отменена.

        Примеры:
        >>> sub = Subscription("Netflix", 15.99)
        >>> sub.cancel_subscription()
        """
        ...

    def apply_discount(self, discount_percent: int) -> float:
        """
        Применить скидку к стоимости.

        :param discount_percent: Процент скидки (0-100).
        :return: Новая стоимость.

        Примеры:
        >>> sub = Subscription("Spotify", 10.0)
        >>> sub.apply_discount(20)
        """
        if not isinstance(discount_percent, int) or not (0 <= discount_percent <= 100):
            raise ValueError("Скидка должна быть целым числом от 0 до 100")
        ...


if __name__ == "__main__":
    # Запуск тестов из документации
    doctest.testmod()