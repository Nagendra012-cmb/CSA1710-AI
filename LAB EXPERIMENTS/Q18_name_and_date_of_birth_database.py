people = {"Anil":"2003-05-12", "Ravi":"2002-11-08", "Meena":"2004-02-19"}
print("Name - Date of Birth")
for name, dob in people.items(): print(name, "-", dob)
search_name = "Ravi"
print(f"\nDOB of {search_name}:", people.get(search_name, "Record not found"))
