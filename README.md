# PasswordAnalyser
Password Analysers are a piece of software that aims to determine how easy your password is to guess. I am currently making my own for personal use and to display here.

Password creation should be based around some simple policies to ensure that your password cannot be guessed. These important policies include:

1. Length. Passwords should be at least 12 characters long to ensure they cannot be brute-forced. Brute-forcing passwords is when an attacker attempts to guess your password by using all possible combinations of characters. Given a password that contains lowercase, uppercase and special characters, a 12 character password has 4.7x10^63 possible combinations. This is considered  adequate, as even with a decently powerful computer, it would take roughly 2,000 years to crack.

2. Complexity. This helps prevent brute-force attacks by increasing the character range. Without any special characters, the possible combinations for your password drop by almost two thirds. 

3. Uniqueness. It is important to not use any common words that attackers could easily guess. The classic 'password' is an example and is often the first attempt attackers make. 

4. Update frequency. Password should be changed frequently, commonly, at least every 3 months. 

5.  Do not reuse passwords across multiple accounts. This prevents large amount of damage to occur if your password is compromised and makes it easier to identify which password is compromised if a password is cracked.

These above policies are implemented in both the Python script and JS.

PYTHON SCRIPT
This python script requires the common.txt to be in the same directory in order to implement the 'uniqueness' policy. Ensure to download the common.txt file too into the same directory.
