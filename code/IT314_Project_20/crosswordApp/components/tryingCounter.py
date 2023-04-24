from django.utils.timezone import now
from django_unicorn.components import UnicornView , PollUpdate
import time

class TryingcounterView(UnicornView):
    polling_disabled = False
    counter = 0
    current_time = now()

    def slow_update(self):
        self.counter += 1
        time.sleep(0.8)  # Simulate slow request

    def get_date(self):
        self.current_time = now()

    def startTimer(self):
        self.call("startTimer")