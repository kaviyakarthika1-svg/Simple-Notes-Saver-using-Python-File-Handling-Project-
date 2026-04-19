import os

FILE_NAME = "notes.txt"

def create_note():
    print("\n--- Create Note ---")
    title = input("Enter title: ")
    content = input("Enter content: ")

    file = open(FILE_NAME, "a")
    file.write("Title: " + title + "\n")
    file.write("Content: " + content + "\n")
    file.write("-" * 30 + "\n")
    file.close()

    print("Note saved successfully!\n")


def read_notes():
    print("\n--- All Notes ---")

    if not os.path.exists(FILE_NAME):
        print("No notes found!\n")
        return

    file = open(FILE_NAME, "r")
    data = file.read()
    file.close()

    if data == "":
        print("No notes available!\n")
    else:
        print(data)


def main():
    while True:
        print("===== Notes Saver =====")
        print("1. Create Note")
        print("2. Read Notes")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_note()
        elif choice == "2":
            read_notes()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.\n")


main()
