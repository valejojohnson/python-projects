# Testing fast look up in a set

valid_regions = {"us-east-1", "us-west-1", "us-west-2", "ap-south-1"}

# TODO: Check if "eu-central-1" is a valid region
is_supported = 'us-east-1'

if is_supported in valid_regions:
    print("True")
else:
    print("False")

print(is_supported)  # Expected: False