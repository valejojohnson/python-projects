# Use a dictionary to count occurences of word

lambda_executions = ["process_data", "send_email", "process_data", "log_event", "send_email", "send_email"]

# TODO: Use a dictionary to count executions
execution_count = {}

for func in lambda_executions:
    if func in execution_count:
        execution_count[func] += 1
    else:
        execution_count[func] = 1

print(execution_count)  # Expected: {'process_data': 2, 'send_email': 3, 'log_event': 1}