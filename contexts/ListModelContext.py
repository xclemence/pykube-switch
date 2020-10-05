from PySide2.QtCore import QAbstractListModel, QModelIndex, Qt
import inspect

class ListModelContext(QAbstractListModel):
    def __init__(self, items, type, parent=None):
        super(ListModelContext, self).__init__(parent)
        self.items = items
        self.item_type = type
        self.schema = self.get_schema()

    def get_schema(self):
        return [name for name, val in inspect.getmembers(self.item_type) if not name.startswith('_') and not callable(val)]

    def append(self, item):
        self.beginInsertRows(QModelIndex(),
                             self.rowCount(),
                             self.rowCount())

        self.items.append(item)
        self.endInsertRows()

    def data(self, index, role):
        key = self.schema[role]
        return self.items[index.row()].__dict__.get(key)

    def setData(self, index, value, role):
        key = self.schema[role]
        self.items[index.row()][key] = value
        self.dataChanged.emit(index, index)

    def rowCount(self, parent=QModelIndex()):
        return len(self.items)

    def roleNames(self):
        role_names = {}
        index = 0

        for field in self.get_schema():
            role_names[index] = field.encode()
            index += 1
        
        return role_names
