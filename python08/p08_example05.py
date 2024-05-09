beatles = []  # Step 1: Create an empty list

# Step 2: Add initial members
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print("Step 1:", beatles)

# Step 3: Add temporary members using a loop
for member in ["Stu Sutcliffe", "Pete Best"]:
    beatles.append(member)
    print(f"Step 3 (adding {member}):", beatles)

# Step 4: Remove temporary members
del beatles[4]  # Remove Pete Best (index 4)
del beatles[3]  # Remove Stu Sutcliffe (index 3)

print("Step 4:", beatles)

# Step 5: Add Ringo Starr to the beginning
beatles.insert(0, "Ringo Starr")

print("Step 5:", beatles)

# Check list length
print("The Fab Four:", len(beatles))
