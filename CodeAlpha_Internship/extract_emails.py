import re

def extract_emails(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()

    emails = re.findall(r'\b[\w.-]+?@\w+?\.\w+?\b', content)

    with open(output_file, 'w') as file:
        for email in emails:
            file.write(email + "\n")

    print(f"✅ Extracted {len(emails)} email(s) to {output_file}")


extract_emails('sample.txt', 'emails.txt')
