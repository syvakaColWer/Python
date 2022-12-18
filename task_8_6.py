# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class AppError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class AcceptWareHouseError(AppError):
    def __init__(self, text):
        self.text = f"Товар не добавлен:\n {text}."


class TransferWareHouseError(AppError):
    def __init__(self, text):
        self.text = f"Оборудование не передано:\n {text}."


AddWareHouseError = AcceptWareHouseError


class ValidateEquipmentError(AppError):
    pass


class WareHouse:
    def __init__(self):
        self.__WareHouse = []

    def add(self, equipments):
        if not all([isinstance(equipment, OfficeOrg) for equipment in equipments]):
            raise AddWareHouseError(f"Это не оргтехника.")
        self.__WareHouse.extend(equipments)

    def transfer(self, idx: int, department: str):
        if not isinstance(idx, int):
            raise TransferWareHouseError(f"Недопустимый тип {type(item)}.")
        item: OfficeOrg = self.__WareHouse[idx]
        if item.department:
            raise TransferWareHouseError(f"Оборудование {item} уже на балансе отдела {item.department}.")
        item.department = department

    def filter_by(self, **kwargs):
        for id_, item in enumerate(self):
            if all([item.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield id_, item

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError
        return self.__WareHouse[key]

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError
        del self.__WareHouse[key]

    def __iter__(self):
        return self.__WareHouse.__iter__()

    def __str__(self):
        return f"На складе сейчас {len(self.__WareHouse)} единиц(ы) оргтехники."


class OfficeOrg:
    __required_props = ("type_org", "vendor_name", "model_name")

    def __init__(self, type_org: str = None, vendor_name: str = "", model_name: str = ""):
        self.type = type_org
        self.vendor_name = vendor_name
        self.model_name = model_name
        self.department = None

    def __setattr__(self, key, value):
        if key in self.__required_props and not value:
            raise AttributeError(f"{key} должен быть не false.")
        object.__setattr__(self, key, value)

    def __str__(self):
        return f"{self.type} {self.vendor_name} {self.model_name}"

    @staticmethod
    def validate(cnt):
        if not isinstance(cnt, int):
            ValidateEquipmentError(f"{type(cnt)}; количество инстансов должен быть типа 'int'")

    @classmethod
    def create(cls, cnt, **properties):
        cls.validate(cnt)
        return [cls(**properties) for _ in range(cnt)]


class Printer(OfficeOrg):
    def __init__(self, **kwargs):
        super().__init__(type_org='принтер', **kwargs)


class Scanner(OfficeOrg):
    def __init__(self, **kwargs):
        super().__init__(type_org='сканер', **kwargs)


class Xerox(OfficeOrg):
    def __init__(self, **kwargs):
        super().__init__(type_org='ксерокс', **kwargs)


if __name__ == '__main__':
    WareHouse = WareHouse()
    WareHouse.add(Printer.create(3, vendor_name="Canon", model_name="Pixma TS3150"))
    WareHouse.add(Printer.create(2, vendor_name="Epson", model_name="L110"))
    WareHouse.add(Scanner.create(3, vendor_name="Canon", model_name="CanoScan LiDE400"))
    WareHouse.add(Scanner.create(2, vendor_name="HP", model_name="ScanJet200"))
    WareHouse.add(Xerox.create(3, vendor_name="Xerox", model_name="Phaser3300"))
    WareHouse.add(Xerox.create(2, vendor_name="Xerox", model_name="B210"))
    print(WareHouse)
    for idx, itm in WareHouse.filter_by(department=None, vendor_name="HP", model_name="ScanJet410"):
        print(f"Резервируем {itm} в ОК.")
        WareHouse.transfer(idx, 'ОК.')
    for idx, itm in WareHouse.filter_by(department=None):
        print(idx, f"{itm} не распределены по отделам.")
    print(WareHouse)
    print("Снимаем с баланса.")
    del WareHouse[0]
    print(WareHouse)
