def palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    return False

num = input("Enter: ")

if palindrome(num):
    print("Palindrome")
else:
    print("Not Palindrome")