contacts = []

print("Enter contact information (format: name|phone|email|address):")


while True:
    line = input().strip()
    if line.upper() == "DONE":
        break
    contacts.append(line)

print("\n=== CONTACT DIRECTORY ===\n")

num = 1
for contact in contacts:
    parts = contact.split("|")
    if len(parts) != 4:
        print(f"Skipping invalid entry: {contact}")
        continue

    name = parts[0].strip()
    phone = parts[1].strip()
    email = parts[2].strip()
    address = parts[3].strip()

    # Proper capitalization for name
    name_parts = [part.title() for part in name.split()]
    name = " ".join(name_parts)

    # Clean phone number (keep as-is if formatted)
    phone = phone

    # Clean email
    email = email.lower().replace(" ", "")

    # Proper case for address
    address = " ".join(word.title() for word in address.split())

    # Display each contact
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

    # Reformat name to "Last, First"
    name_parts = name.split()
    if len(name_parts) >= 2:
        last_name = name_parts[-1]
        first_name = " ".join(name_parts[:-1])
        formatted_name = f"{last_name}, {first_name}"
    else:
        formatted_name = name

    # Align columns nicely
    print(f"{formatted_name:<30} {phone:<20} {email}")
