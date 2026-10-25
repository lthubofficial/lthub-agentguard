
import threading
import time


class ThreadSafeRateLimiter:
    """
    In-process rate limiter for experimental testing.

    This is not a distributed or production-ready security gateway.
    """

    def __init__(self, max_requests=5, window_seconds=10):
        if not isinstance(max_requests, int) or isinstance(max_requests, bool):
            raise ValueError("max_requests must be a positive integer")

        if max_requests <= 0:
            raise ValueError("max_requests must be greater than zero")

        if window_seconds <= 0:
            raise ValueError("window_seconds must be greater than zero")

        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = {}
        self.lock = threading.Lock()

    def allow_request(self, client_id):
        if not isinstance(client_id, str) or not client_id.strip():
            raise ValueError("client_id must be a non-empty string")

        with self.lock:
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


def main():
    limiter = ThreadSafeRateLimiter(
        max_requests=5,
        window_seconds=10
    )

    print("LT Hub AgentGuard - AG-C054")
    print("Thread-safe experimental rate limiter")
    print("Limit: 5 requests per client per 10-second window")
    print()

    for number in range(1, 8):
        allowed = limiter.allow_request("test-client")
        result = "ALLOWED" if allowed else "BLOCKED"
        print(f"Request {number}: {result}")


if __name__ == "__main__":
    main()
          
