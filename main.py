import random

class FlashcardsApp:
    def __init__(self):
        self.flashcards = []
        self.current_card = None

    def add_flashcard(self, question, answer):
        self.flashcards.append({'question': question, 'answer': answer})

    def show_flashcard(self):
        if not self.flashcards:
            return "No flashcards available. Add flashcards first."

        self.current_card = random.choice(self.flashcards)
        return "Question: {}".format(self.current_card['question'])

    def check_answer(self, user_answer):
        if not self.current_card:
            return "No flashcard to check. Use 'show' to get a new flashcard."

        correct_answer = self.current_card['answer']
        if user_answer.lower() == correct_answer.lower():
            return "Correct! Well done!"
        else:
            return "Incorrect. The correct answer is: {}".format(correct_answer)

    def delete_flashcard(self, question):
        for index, card in enumerate(self.flashcards):
            if card['question'] == question:
                deleted_card = self.flashcards.pop(index)
                return "Flashcard deleted: {}".format(deleted_card)
        
        return "Flashcard with question '{}' not found. No flashcard deleted.".format(question)

if __name__ == "__main__":
    app = FlashcardsApp()

    while True:
        print("\nOptions:")
        print("1. Add Flashcard")
        print("2. Show Flashcard")
        print("3. Check Answer")
        print("4. Delete Flashcard")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        try:
            choice = int(choice)

            if 1 <= choice <= 5:
                if choice == 1:
                    question = input("Enter the question: ")
                    answer = input("Enter the answer: ")
                    app.add_flashcard(question, answer)
                    print("Flashcard added!")

                elif choice == 2:
                    print(app.show_flashcard())

                elif choice == 3:
                    user_answer = input("Enter your answer: ")
                    print(app.check_answer(user_answer))

                elif choice == 4:
                    question_to_delete = input("Enter the question of the flashcard to delete: ")
                    print(app.delete_flashcard(question_to_delete))

                elif choice == 5:
                    print("Quitting the flashcards app. Goodbye!")
                    break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")