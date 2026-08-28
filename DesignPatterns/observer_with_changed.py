from typing import Protocol

class Observer(Protocol):
    def update(self, message: str) -> None:
        ...
        
class Subject(Protocol):
    def attach(self, observer: Observer) -> None:
        ...
    def detach(self, observer: Observer) -> None:
        ...
    def notify(self, message: str) -> None:
        ...
        
class Subject:
    def __init__(self) -> None:
        self._observers: list[Observer] = []
        self.changed = False

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)
        
    # Allows us to specify conditions under which
    # notifications should be sent out
    # say, past a given threshold or a certain frequency
    def set_changed(self):
        self.changed = True
        
    def clear_changed(self):
        self.changed = False
        
    def has_changed(self):
        return self.changed

    def notify(self, message: str) -> None:
        if self.changed:
            for observer in self._observers:
                observer.update(message)
        self.changed = False

class MonitorObserver(Observer):
    def update(self, message: str) -> None:
        print(f"Received message: {message}")

class LoggerObserver(Observer):
    def update(self, message: str) -> None:
        print(f"Logging message: {message}")

if __name__ == "__main__":
    subject = Subject()
    monitor_observer = MonitorObserver()
    logger_observer = LoggerObserver()

    subject.attach(monitor_observer)
    subject.attach(logger_observer)

    subject.set_changed()   # Must be called before any notifications can be sent
    subject.notify("Hello, Observers!")
