# Input reading
N = int(input())
fat = list(map(int, input().split()))
protein = list(map(int, input().split()))
vitamin = list(map(int, input().split()))

# Convert all arrays to sets
fat_set = set(fat)
protein_set = set(protein)
vitamin_set = set(vitamin)

# Find unique elements for each category
fat_only = fat_set - protein_set - vitamin_set
protein_only = protein_set - fat_set - vitamin_set
vitamin_only = vitamin_set - fat_set - protein_set

# Count occurrences of those unique elements in their respective original lists
fat_count = sum(1 for x in fat if x in fat_only)
protein_count = sum(1 for x in protein if x in protein_only)
vitamin_count = sum(1 for x in vitamin if x in vitamin_only)

# Output the results
print(fat_count, protein_count, vitamin_count)