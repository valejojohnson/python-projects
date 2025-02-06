# Store API requests in a set - Dupes should be ignored

api_requests = ["req-001", "req-002", "req-003", "req-001", "req-002"]

# TODO: Store unique API requests in a set
unique_requests = sorted(set(api_requests))

print(unique_requests)  # Expected: {'req-001', 'req-002', 'req-003'}