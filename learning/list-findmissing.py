# Find missing instances from list

expected_instances = ["i-111", "i-222", "i-333", "i-444"] # A list
running_instances = {"i-222", "i-333"} # A Set

# TODO: Find the missing instances
missing_instances = set(expected_instances) - running_instances

print(sorted(missing_instances))  # Expected: {'i-111', 'i-444'}