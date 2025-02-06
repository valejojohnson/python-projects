# Look up instance type from dictionary

ec2_instances = {
    "i-12345": "t2.micro",
    "i-67890": "m5.large",
    "i-98765": "c5.xlarge"
}

# TODO: Look up the instance type of "i-67890"
instance_type = ec2_instances["i-67890"]

print(instance_type)  # Expected: "m5.large"