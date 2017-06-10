import random


class Quiz:

    def __init__(self):
        self.questions = []
        self.given_answers = []
        self.correct_answers = []
        # contains the question numbers to display in sequence
        self.questions_sequence = []

    def read_questions(self, filename):
        with open(filename) as file:
            question = file.readline()
            while question:
                question = question.split('. ')[1].split('\n')[0]
                self.questions.append(question)
                question = file.readline()

    def read_key(self, filename):
        with open(filename) as file:
            answer = file.readline()
            while answer:
                answer = answer.split('. ')[1].split('\n')[0]
                self.correct_answers.append(answer)
                answer = file.readline()

    def print_questions(self):
        print ("--------------------Questions-------------------")
        for i in range(0, len(self.questions_sequence)):
            print (str(i + 1)
                   + ". "
                   + self.questions[self.questions_sequence[i]]
                   + '\n')

    def verify_answers(self):
        print ("---------------------Result---------------------")
        for i in range(0, len(self.given_answers)):
            if (self.given_answers[i]
                != self.correct_answers[self.questions_sequence[i]]):

                print ("Sorry, the correct answer of Question-"
                       + str(i + 1)
                       + " is "
                       + self.correct_answers[self.questions_sequence[i]]
                       + '\n')
            else:
                print ("Question-"
                       + str(i + 1)
                       + " answered correcly."
                       + '\n')

    def input_answers(self):
        print ("------------------Give Answers------------------")
        for i in range(0, len(self.questions_sequence)):
            print ("Question - " + str(i + 1) + " :")
            # Take answer as input from the user
            answer = input()
            self.given_answers.append(answer)

    def generate_quiz(self, no_of_questions):
        if no_of_questions <= len(self.questions):
            for i in range(0, len(self.questions)):
                self.questions_sequence.append(i)

            # shuffling the question sequence,
            # so random questions will be displayed
            self.questions_sequence = random.sample(self.questions_sequence,
                                                    no_of_questions)
            self.print_questions()
        else:
            print ("There are only "
                   + str(len(self.questions))
                   + " questions.")
