# Get rid of dupes and sort list

iam_roles = ["Admin", "ReadOnly", "Admin", "Developer", "ReadOnly"]

# TODO: Remove duplicates and sort the roles
sorted_roles = sorted(set(iam_roles))

print(sorted_roles)  # Expected: ['Admin', 'Developer', 'ReadOnly']