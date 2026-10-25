
import time

class RateLimiter:
    def __init__(self, max_requests=5, window_seconds=10):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = {}

    def allow_request(self, client_id):
        now = time.monotonic()
        recent = self.requests.get(client_id, [])

        recent = [
            timestamp for timestamp in recent
            if now - timestamp < self.window_seconds
        ]

        if len(recent) >= self.max_requests:
            self.requests[client_id] = recent
            return False

        recent.append(now)
        self.requests[client_id] = recent
        return True


limiter = RateLimiter(max_requests=5, window_seconds=10)

print("LT Hub AgentGuard — AG-C054")
print("Limit: 5 requests per client per 10-second window")
print()

for number in range(1, 8):
    allowed = limiter.allow_request("test-client")
    result = "ALLOWED" if allowed else "BLOCKED"
    print(f"Request {number}: {result}")
  
