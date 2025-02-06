# Add up costs for AWS Resources

# Cost per hour for each AWS resource type
resource_cost_per_hour = {
    "EC2": 0.10,
    "S3": 0.02,
    "RDS": 0.15,
    "Lambda": 0.001
}

# Hours each resource was used in a given month
resource_usage_hours = {
    "EC2": 720,   # 30 days * 24 hours
    "S3": 50000,  # Storage access time
    "RDS": 600,
    "Lambda": 250000  # High usage due to many small executions
}

# TODO: Calculate total cost per resource
resource_total_cost = {}

# TODO: Calculate total AWS bill
total_bill = 0

for resource in resource_cost_per_hour:
    cost = resource_cost_per_hour[resource] * resource_usage_hours[resource]
    resource_total_cost[resource] = cost
    total_bill += cost


print("Total Cost Per Resource:", resource_total_cost)
print("Total AWS Bill: $", total_bill)