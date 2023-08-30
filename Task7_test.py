class ATM:
    def __init__(self):
        self.denominations = [500, 200, 50]

    def validate_amount(self, amount):
        return amount > 0 and amount % 50 == 0

    def dispense_notes(self, amount):
        notes_count = {}
        for denomination in self.denominations:
            count = amount // denomination
            if count > 0:
                notes_count[denomination] = count
                amount -= denomination * count
        return notes_count

    def perform_transaction(self, amount):
        if not self.validate_amount(amount):
            print("Invalid amount. Please enter a valid amount (multiple of 50).")
            return False
        
        notes_count = self.dispense_notes(amount)
        print("Dispensing notes:")
        for item in notes_count.items():
            denomination, count = item
            print(str(denomination) + " notes:", count)

        return True

atm = ATM()

while True:
    withdrawal_amount = int(input("Enter the withdrawal amount: "))
    
    if atm.perform_transaction(withdrawal_amount):
        choice = input("Do you want to continue (y/n)? ").lower()
        if choice != "y":
            print("Transaction canceled.")
            break
