question_lists =[
    "What is my favourite color?\n a)Coral Pink\nb)Neon Green\nc)White\nd)Black\n\n",
    "What is my favourite TV show?\n a)GOT\nb)Ozark\nc) Too Hot to Handle d)The Office\n\n",
    "What is my favourite pastime ?\na) Reading \n b)Sleeping\n c)Watching shows online\n d)Eating/cooking \n\n",
    "If I had Rs 1 crore, what would i do with it?\na) Nothing. Invest it.\n b) buy a house\n c) Donate\nd) Die \n\n",
    "Do you love me? \n a) Yes\nb) No\n c) Maybe \nd)More than anything else in the world\n\n",
    "Do you think i can do well in the IT sector?\na)Yes\nb)No\nc)for a short time yes\nd)Why?\n\n"
]
print(question_lists[5])
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

quis_ques = [Question(question_lists[0], "a"),
             Question(question_lists[1], "d"),
             Question(question_lists[2], "b"),
             Question(question_lists[3], "d"),
             Question(question_lists[4], "d"),
             Question(question_lists[5], "d")]


def run_test(quiz_ques):
    score = 0
    for Question in quiz_ques:
        answer = input(quiz_ques.prompt)
        if answer == quiz_ques.answer:
            score += 1
    if score in range(4, 7):
        print("You know me too well. I dont like it.")
        print("Your score is " + str(score) + "/" + str(len(quiz_ques)) + ".")
    elif score in range(2, 4):
        print("Woah, good job mister. You could do better.")
        print("Your score is " + str(score) + "/" + str(len(quiz_ques)) + ".")
    elif score in range(0, 2):
        print("I am glad you couldnt answer")
        print("Your score is " + str(score) + "/" + str(len(quiz_ques)) + ".")

