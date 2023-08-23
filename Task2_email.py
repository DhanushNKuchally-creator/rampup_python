import re


def is_valid_email(email):
    # Regular expression for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

def write_emails_to_file(emails, file_path):
    with open(file_path, "w") as file:
        for email in emails:
            file.write(email + "\n")

def main():
    valid_emails = []
    file_path = r"C:\Users\Dhanush N INT-214\Desktop\Valid_emails.txt"
    
    while True:
        email = input("Enter an email address: ")
        
        if is_valid_email(email):
            valid_emails.append(email)
            print("Valid email. Added to the list.")
        else:
            print("Invalid email. Please enter a valid email address.")
        
        response = input("Do you want to continue? (Yes/No): ").strip().lower()
        
        if response == "no":
            write_emails_to_file(valid_emails,file_path)
            f= open(file_path, "r") 
            print("Email IDs in the file:")
            for x in f:
                print(x)
            break
    
    if valid_emails:
       # file_path = r"C:\Users\Dhanush N INT-214\Desktop\Valid_emails.txt"
        write_emails_to_file(valid_emails, file_path)
        print(f"Valid emails have been written to '{file_path}'.")
    else:
        print("No valid emails to write.")

if __name__ == "__main__":
    main()
