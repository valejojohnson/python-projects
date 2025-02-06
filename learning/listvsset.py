# list of AWS regions where we need to get rid of dupes

regions = ["us-east-1", "us-west-1", "us-east-1", "us-west-2", "us-west-1"]

# TODO: Convert the list to a set to remove duplicates
unique_regions = set(regions)

print(unique_regions)  # Expected: {'us-east-1', 'us-west-1', 'us-west-2'}