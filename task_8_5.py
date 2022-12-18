# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).

class WareHouseError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class AddWareHouseError(WareHouseError):
    def __init__(self, text):
        self.text = f"Товар на склад не добавлен:\n {text}"


class TransferWareHouseError(WareHouseError):
    def __init__(self, text):
        self.text = f"Оборудование не передано:\n {text}"


class WareHouse:
    def __init__(self):
        self.__WareHouse = []

    def add(self, item: "OfficeOrg"):
        if not isinstance(item, OfficeOrg):
            raise AddWareHouseError(f"{item} не является оргтехникой.")
        self.__WareHouse.append(item)

    def transfer(self, idx: int, department: str):
        if not isinstance(idx, int):
            raise TransferWareHouseError(f"Недопустимый тип '{type(item)}'.")
        item: OfficeOrg = self.__WareHouse[idx]
        if item.department:
            raise TransferWareHouseError(f"Оборудование {item} не добавлено. Оно уже закреплено за {item.department}.")
        item.department = department

    def filter_by(self, **kwargs):
        for idx, item in enumerate(self):
            a: OfficeOrg = item
            if all([a.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield idx, item

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
    def __init__(
            self,
            type_org: str,
            vendor_name: str,
            model_name: str,
    ):
        self.type = type_org
        self.vendor_name = vendor_name
        self.model_name = model_name
        self.department = None

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

    def __str__(self):
        return f"{self.type} {self.vendor_name} {self.model_name}"


class Printer(OfficeOrg):
    def __init__(self, *args):
        super().__init__('принтер', *args)


class Scanner(OfficeOrg):
    def __init__(self, *args):
        super().__init__('сканер', *args)


class Xerox(OfficeOrg):
    def __init__(self, *args):
        super().__init__('ксерокс', *args)


if __name__ == '__main__':
    WareHouse = WareHouse()
    WareHouse.add(Printer("Epson", "L110"))
    WareHouse.add(Scanner("Canon", "CanoScan LiDE 400"))
    WareHouse.add(Xerox("Xerox", "B215"))
    print(WareHouse)
    last_idx = None
    for idx, itm in WareHouse.filter_by(department=None):
        print(idx, itm)
        last_idx = idx
    print("Передаем на баланс:")
    WareHouse.transfer(last_idx, 'ОК')
    for idx, itm in WareHouse.filter_by(department=None):
        print(idx, itm)
    print(WareHouse)
    print("Снимаем с баланса:")
    del WareHouse[last_idx]
    print(WareHouse)
    last_idx = None
    for idx, itm in WareHouse.filter_by(department=None):
        print(idx, itm)
        last_idx = idx
