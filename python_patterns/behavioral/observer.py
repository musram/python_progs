"""
http://code.activestate.com/recipes/131499-observer-pattern/
*TL;DR
Maintains a list of dependents and notifies them of any state changes.
*Examples in Python ecosystem:
Django Signals: https://docs.djangoproject.com/en/2.1/topics/signals/
Flask Signals: http://flask.pocoo.org/docs/1.0/signals/
"""

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

class Data(Subject):
    def __init__(self, name=''):
        Subject.__init__(self)
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()
                
class HexViewer:
    def update(self, subject):
        print('HexViewer: Subject {} has data 0x{:x}'.format(subject.name, subject.data))


class DecimalViewer:
    def update(self, subject):
        print('DecimalViewer: Subject %s has data %d' % (subject.name, subject.data))

if __name__ == "__main__":

    data1 = data('data 1')
    data2  = data('data 2')
    view1 = DecimalViewer()
    view2 = HexViewer()
    data1.attach(view1)
    data1.attach(view2)
    data2.attach(view2)
    data2.attach(view1)
    data1.data = 10
    data2.data = 15
    data1.data = 3
    data2.data = 5
    data1.detach(view2)
    data2.detach(view2)
    data1.data = 10
    data2.data = 15
