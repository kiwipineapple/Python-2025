"""
setattr (Schwer)
Wir haben eine Klasse LineItem gegeben. Erstelle LineItem-Objekte und speichere
sie in einer Liste line_items. Achte in __init__ darauf, dass die Werte in
**kwargs übergeben werden und erstelle dynamisch die Attribute.
Es muss __repr__ implementiert sein, exakt(!) wie unten in Result gezeigt.
"""

from pprint import pprint


class LineItem:
    def __init__(self, **kwargs):
        # print(kwargs)  # dict
        for attribute, value in kwargs.items():
            setattr(self, attribute, value)

    def __repr__(self) -> str:
        value_list = [f"{k}={v!r}" for k, v in vars(self).items()]
        value_string = ", ".join(value_list)  # id=3, name='Pencil Geha' ...
        return f"<{self.__class__.__name__}({value_string})>"


lines = [
    {
        "id": 3,
        "name": "Pencil Geha",
        "style": "bold",
        "color": "black",
    },
    {
        "id": 13,
        "name": "Pencil Geha Professional",
        "style": "bold",
        "color": "red",
    },
    {
        "id": 23,
        "name": "Parker Chef",
        "style": "thin",
        "color": "silver",
        "bevel": True,
    },
]


line_items = [LineItem(**item) for item in lines]
pprint(line_items)
# print(line_items[0].__dict__)
# Result:
# [
# <LineItem(id=3, name='Pencil Geha', style='bold', color='black')>,
# <LineItem(id=13, name='Pencil Geha Professional', style='bold', color='red')>,
# <LineItem(id=23, name='Parker Chef', style='thin', color='silver', bevel=True)>
# ]
