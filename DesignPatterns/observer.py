from typing import Protocol

class Observer(Protocol):
    def update(self, message: str) -> None:
        ...

class Subject:
    def __init__(self) -> None:
        self._observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, message: str) -> None:
        for observer in self._observers:
            observer.update(message)

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

    subject.notify("Hello, Observers!")