from data_structures import PriorityQueue

class RequestQueue:
    PRIORITY_LEVELS = {
        "Emergency": 1,
        "Standard": 2,
        "Low": 3,
    }

    def __init__(self):
        self.body = PriorityQueue()
        self._counter = 0

    def enqueue(self, request, priority_label="Standard"):
        if not isinstance(request, str) or not request.strip():
            raise ValueError("Request description must be a non-empty string.")
        if priority_label not in self.PRIORITY_LEVELS:
            raise ValueError(f"Unknown priority level: {priority_label}")

        priority_value = self.PRIORITY_LEVELS[priority_label]
        self.body.enqueue(
            {
                "description": request.strip(),
                "priority": priority_label,
            },
            (priority_value, self._counter),
        )
        self._counter += 1

    def dequeue(self):
        result = self.body.dequeue()
        if result is None or isinstance(result, IndexError):
            return None
        _, item = result
        return item

    def peek(self):
        result = self.body.peek()
        if result is None or isinstance(result, IndexError):
            return None
        _, item = result
        return item

    def is_empty(self):
        return len(self.body.data) == 0

    def get_all_requests(self):
        return [
            {
                "description": item[1]["description"],
                "priority": item[1]["priority"],
            }
            for item in sorted(self.body.data)
        ]
