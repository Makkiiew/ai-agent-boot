from functions.run_python_file import run_python_file

def run_tests():
    print("--- Test 1: Run main.py ---")
    print(run_python_file("calculator", "main.py"))
    print("-" * 30)

    print("--- Test 2: Run main.py with '3 + 5' ---")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print("-" * 30)

    print("--- Test 3: Run tests.py ---")
    print(run_python_file("calculator", "tests.py"))
    print("-" * 30)

    print("--- Test 4: Run ../main.py (Security Error) ---")
    print(run_python_file("calculator", "../main.py"))
    print("-" * 30)

    print("--- Test 5: Run nonexistent.py ---")
    print(run_python_file("calculator", "nonexistent.py"))
    print("-" * 30)

    print("--- Test 6: Run lorem.txt ---")
    print(run_python_file("calculator", "lorem.txt"))
    print("-" * 30)

if __name__ == "__main__":
    run_tests()