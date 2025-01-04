# Halfwaves_banking_system
A console-based Banking System that allows users to create accounts, perform banking transactions, and manage their finances. The project should include secure login functionality, transaction logging, and persistent storage of user and transaction data using file handling.
1. Accounts File (accounts.txt):
        - Store details of all users in the format:
        
        Example:
            
            
      Account Number, Name, Password, Balance
      123456,John Doe,password123,1500
      - Write account details to the file during account creation.
     - Read account details for login validation and user account operations.
    2. **Transactions File (transactions.txt):**
        - Store all transactions in the format:
        
        Example:
            
            
       Account Number, Transaction Type (Deposit/Withdrawal), Amount, Date
            
            
            
            
       123456,Deposit,500,2024-12-23
            
            
            
    
  *Console Flow Example:*
    
  1. *Main Menu:*
        
        
        Welcome to the Banking System!
        1. Create Account
        2. Login
        3. Exit
        Enter your choice: 1
        
        
        
  2. *Creating an Account:*
        
        
        Enter your name: John Doe
        Enter your initial deposit: 1000
        Your account number: 123456 (Save this for login)
        Enter a password: ****
        Account created successfully!
        (Account details saved to accounts.txt)
        
        
        
   3. *Logging In:*
        
        
        Enter your account number: 123456
        Enter your password: ****
        Login successful!
        
        
        
   4. *Performing Transactions (Deposit):*
        
        
        Enter amount to deposit: 500
        Deposit successful! Current balance: 1500
        (Transaction logged in transactions.txt)
