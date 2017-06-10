from quiz import Quiz


if __name__ == "__main__":
    q1 = Quiz()
    q1.read_questions("./questions.txt")
    # key contains the correct answers to questions file
    q1.read_key("./key.txt")

    # generate_quiz takes no. of questions as input
    q1.generate_quiz(3)
    q1.input_answers()
    q1.verify_answers()

    # Similarly more quizes can be generated the same way
