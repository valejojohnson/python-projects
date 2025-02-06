# Count the error types from dict

aws_logs = [
    "EC2: InstanceFailed",
    "Lambda: Timeout",
    "S3: PermissionDenied",
    "EC2: InstanceFailed",
    "EC2: InstanceFailed",
    "Lambda: MemoryExceeded",
    "Lambda: Timeout",
    "S3: PermissionDenied",
    "EC2: DiskFull",
    "Lambda: Timeout"
]

# TODO: Write code to count each error type
error_count = {}

for error in aws_logs:
    if error in error_count:
        error_count[error] += 1
    else:
        error_count[error] = 1


print(error_count)