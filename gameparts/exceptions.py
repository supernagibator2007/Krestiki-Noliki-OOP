class FieldIndexError(IndexError):

    def __str__(self):
        return 'Вы ввели координаты за границами поля'


class CellOccupiedError(Exception):

    def __str__(self):
        return 'Попытка изменить заданную ячейку'
