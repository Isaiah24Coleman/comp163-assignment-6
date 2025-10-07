# comp163-assignment-6
# Isaiah24Coleman_assignment_6.py
Student: Isaiah Coleman
Assignment 6: Contact Information Formatter 

Demonstrates mastery of string methods for data cleaning and formatting

#Initialize an empty list to store contact entries

contacts = []

print("Enter contact information (format: name|phone|email|address):")

# Input loop: read contact data until user types "DONE"
while True:
    line = input().strip()
    if line.upper() == "DONE":
        break
    contacts.append(line)

print("\n=== CONTACT DIRECTORY ===\n")

num = 1
for contact in contacts:
    # Parse contact into fields, separated by '|'
    parts = contact.split("|")
    if len(parts) != 4:
        print(f"Skipping invalid entry: {contact}")
        continue

    # Clean and format each field
    name = parts[0].strip()
    phone = parts[1].strip()
    email = parts[2].strip()
    address = parts[3].strip()

    # Proper capitalization for name using .title()
    name_parts = [part.title() for part in name.split()]
    name = " ".join(name_parts)

    # Phone number: left as input, can add formatting if desired
    phone = phone

    # Email: lowercase and remove spaces
    email = email.lower().replace(" ", "")

    # Address: capitalize each word for professional appearance
    address = " ".join(word.title() for word in address.split())

    # Print formatted contact entry
    print(f"CONTACT {num}:")
    print(f"Name:     {name}")
    print(f"Phone:    {phone}")
    print(f"Email:    {email}")
    print(f"Address:  {address}\n")
    num += 1

print("=== DIRECTORY SUMMARY ===")
print(f"Total contacts processed: {len(contacts)}\n")

print("=== FORMATTED FOR PRINTING ===")

for contact in contacts:
    parts = contact.split("|")
    if len(parts) != 4:
        continue
    name = parts[0].strip()
    phone = parts[1].strip()
    email = parts[2].strip()

    # Reformat name to "Last, First" for printing
    name_parts = name.split()
    if len(name_parts) >= 2:
        last_name = name_parts[-1]
        first_name = " ".join(name_parts[:-1])
        formatted_name = f"{last_name}, {first_name}"
    else:
        formatted_name = name

    # Align columns for professional output
    print(f"{formatted_name:<30} {phone:<20} {email}")
