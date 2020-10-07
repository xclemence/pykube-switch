from PySide2.QtCore import QAbstractListModel, QModelIndex, Property
import inspect

class ListModelContext(QAbstractListModel):
    def __init__(self, items, type, parent=None):
        super(ListModelContext, self).__init__(parent)
        self.items = items
        self.item_type = type
        self.schema = self.get_schema()

    def get_schema(self):
        return [name for name, val in inspect.getmembers(self.item_type, lambda o: isinstance(o, Property)) ]

    def append(self, item):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())

        self.items.append(item)
        self.endInsertRows()

    def data(self, index, role):
        key = self.schema[role]
        return getattr(self.items[index.row()], key)

    def setData(self, index, value, role):
        pass

    def rowCount(self, parent=QModelIndex()):
        return len(self.items)

    def roleNames(self):
        role_names = {}
        index = 0

        for field in self.get_schema():
            role_names[index] = field.encode()
            index += 1
        
        return role_names
