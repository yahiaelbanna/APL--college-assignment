class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        print(f"Received update: {message}")

subject = Subject()
obs1 = Observer()
obs2 = Observer()

subject.attach(obs1)
subject.attach(obs2)

subject.notify("Update available!")