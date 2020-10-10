import inspect

from PySide2.QtCore import QAbstractListModel, QModelIndex, Property

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

    def remove(self, item):
        item_index = self.items.index(item)

        self.beginRemoveRows(QModelIndex(), item_index, item_index)

        self.items.remove(item)
        self.endRemoveRows()

    def update(self, item):
        item_index = self.items.index(item)

        index = self.index(item_index, 0)
        self.dataChanged.emit(index, index)

    def update_all(self):
        self.dataChanged.emit(self.index(0), self.index(len(self.items) - 1))

    def data(self, index, role):
        key = self.schema[role]
        return getattr(self.items[index.row()], key)

    def rowCount(self, parent=QModelIndex()):
        return len(self.items)

    def roleNames(self):
        role_names = {}
        index = 0

        for field in self.get_schema():
            role_names[index] = field.encode()
            index += 1
        
        return role_names
