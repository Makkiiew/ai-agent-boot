from functions.write_file import write_file

def run_tests():
    print("--- Test 1: Overwrite lorem.txt ---")
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print("-" * 30)

    print("--- Test 2: Create pkg/morelorem.txt ---")
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print("-" * 30)

    print("--- Test 3: Write to /tmp/temp.txt ---")
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    print("-" * 30)

if __name__ == "__main__":
    run_tests()