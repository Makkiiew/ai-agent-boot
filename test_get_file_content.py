from functions.get_file_content import get_file_content

def run_tests():
    # 1. Test Truncation (Keep this as is)
    print("--- Testing lorem.txt (Truncation) ---")
    print(get_file_content("calculator", "lorem.txt"))
    
    # 2. Test Success cases - PRINT FULL CONTENT HERE
    print("\n--- Testing main.py ---")
    # Remove any slicing like [:100]. Print the whole thing!
    print(get_file_content("calculator", "main.py"))

    print("\n--- Testing pkg/calculator.py ---")
    print(get_file_content("calculator", "pkg/calculator.py"))

    # 3. Test Security/Error cases
    print("\n--- Testing /bin/cat (Outside sandbox) ---")
    print(get_file_content("calculator", "/bin/cat"))

    print("\n--- Testing pkg/does_not_exist.py ---")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    run_tests()