# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.

class WareHouse:
    pass


class OfficeOrg:
    vat = 0.15
    added_value = 2.5
    retail_rate = 1.5

    def __init__(
            self,
            type_org: str,
            vendor_name: str,
            model_name: str,
            color_org: str,
            price_org: float,
    ):
        self.type = type_org
        self.vendor_name = vendor_name
        self.model_name = model_name
        self.color_org = color_org
        self.price_org = price_org
        self.printable = True if self.type in ("принтер", "ксерокс") else False
        self.scannable = True if self.type in ("сканер", "ксерокс") else False

    @property
    def retailprice(self):
        return self.notretailprice * self.retail_rate

    @property
    def notretailprice(self):
        return self.price_org * (1 + self.vat) * (1 + self.added_value)

    def __str__(self):
        return f"Тип устройства: {self.type}, фирма-произмодитель: {self.vendor_name}, модель: {self.model_name}, цвет: ({self.color_org})."


class Printer(OfficeOrg):
    printable = True
    scannable = False

    def __init__(self, *args):
        super().__init__("принтер", *args)


class Scanner(OfficeOrg):
    printable = False
    scannable = True

    def __init__(self, *args):
        super().__init__("сканер", *args)


class Xerox(OfficeOrg):
    printable = True
    scannable = True

    def __init__(self, *args):
        super().__init__("ксерокс", *args)


if __name__ == '__main__':
    x1 = Xerox("Xerox", "B1025", "white", 1)
    print(x1)
