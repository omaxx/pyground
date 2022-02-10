import urwid

from .observer import Observable


def get_data(obj, key):
    return getattr(obj, key)


class TableHeader(urwid.Columns):
    def __init__(self, fields):
        self.fields = fields
        cols = [urwid.Text(field) for field in fields]
        super().__init__(cols)


class TableRow(urwid.Columns):
    def __init__(self, obj, fields):
        self.obj = obj
        self.fields = fields
        cols = [urwid.Text(get_data(obj, field)) for field in fields]
        super().__init__(cols)
        if isinstance(obj, Observable):
            obj.register_observer(self)

    def update(self):
        for i, field in enumerate(self.fields):
            self.contents[i][0].set_text(get_data(self.obj, field))


class TableRowList(urwid.ListBox):
    def __init__(self, table, fields):
        self.table = table
        self.fields = fields
        rows = [TableRow(obj, fields) for obj in table]
        super().__init__(urwid.SimpleFocusListWalker(rows))


class Table(urwid.Pile):
    def __init__(self, table, fields):
        self.row_list = TableRowList(table, fields)
        rows = [
            ("pack", TableHeader(fields)),
            ("pack", urwid.Divider(div_char="=")),
            ("weight", 1, self.row_list)
        ]
        super().__init__(rows)


class Main(urwid.WidgetWrap):
    def __init__(self, table, fields):
        table = Table(table, fields)
        super().__init__(table)
