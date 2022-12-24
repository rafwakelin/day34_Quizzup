from tkinter import *
from quiz_brain import *
from playsound import playsound

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzup")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Here goes the question",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"),
                                                     width=280,
                                                     anchor="center",
                                                     justify="center")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        button_true_image = PhotoImage(file="images/true.png")
        self.button_true = Button(image=button_true_image, highlightthickness=0, command=self.answer_true)
        self.button_true.grid(row=2, column=0)
        button_true_false = PhotoImage(file="images/false.png")
        self.button_false = Button(image=button_true_false, highlightthickness=0, command=self.answer_false)
        self.button_false.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text= f"You've completed the quiz\n"
                                         f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.button_false.config(state="disabled")
            self.button_true.config(state="disabled")

    def answer_true(self):
        self.feedback(self.quiz.check_answer(user_answer="true"))

    def answer_false(self):
        self.feedback(self.quiz.check_answer(user_answer="false"))

    def feedback(self, correct):
        if correct:
            self.canvas.config(bg="green")
            playsound("sounds/421002__eponn__correct.wav")
        else:
            self.canvas.config(bg="red")
            playsound("sounds/som_de_resposta_errada_efeito_sonoro_toquesengracadosmp3.com.mp3")


        self.window.after(1000, func=self.get_next_question)
