import tkinter

# membuat kelas Question yang berisi pertanyaan, opsi, dan jawaban benar
class Question:
    def __init__(self, question, options, correctIndex):
        self.question = question # contoh: "Apa ibukota Indonesia?"
        self.options = options # contoh: ["a", "b", "c", "d"]
        self.correctIndex = correctIndex # contoh: 0 -> berarti jawaban a benar
        
    def isCorrect(self, answerIndex: int):
        return self.correctIndex == answerIndex


# Inisialisasi soal-soal kuis
pertanyaanku = [
    Question("Apa ibukota Indonesia?", ["Jakarta", "Bandung", "Surabaya", "Bali"], 0),
    Question("Siapa presiden Indonesia saat ini?", ["Jokowi", "SBY", "Megawati", "Gus Dur"], 0),
    Question("Siapa penemu lampu?", ["Edison", "Tesla", "Newton", "Einstein"], 0),
    Question("Berapa 1 + 1?", ["1", "2", "3", "4"], 1),
]


# Inisialisasi variabel yang diperlukan
currentQuestionIndex = 0
correctAnswers = 0


# membuat window baru dan menyimpannya ke variabel window
window = tkinter.Tk()

# membuat widgets
labelTitle = tkinter.Label(window, text="Kuis Sederhana", font=("Arial", 18))
labelCorrectCount = tkinter.Label(window, text=f"Jawaban Benar: {correctAnswers} / {len(pertanyaanku)}")
labelQuestion = tkinter.Label(window, text="")
buttonOption1 = tkinter.Button(window, text="")
buttonOption2 = tkinter.Button(window, text="")
buttonOption3 = tkinter.Button(window, text="")
buttonOption4 = tkinter.Button(window, text="")

labelTitle.pack()
labelCorrectCount.pack()
labelQuestion.pack()
buttonOption1.pack()
buttonOption2.pack()
buttonOption3.pack()
buttonOption4.pack()


# ketika salah satu buttonOption diklik :
# 1. cek apakah jawaban benar
# 2. naikkan nilai correctAnswers jika jawaban benar
# 3. naikkan currentQuestionIndex
# 4. tampilkan pertanyaan berikutnya (showQuestion())
def onOptionClick(isCorrect: bool):
    global correctAnswers # kita pakai global karena kita akan mengubah nilai correctAnswers di atas
    global currentQuestionIndex # kita pakai global karena kita akan mengubah nilai currentQuestionIndex di atas
    if isCorrect:
        correctAnswers += 1
    currentQuestionIndex += 1
    showQuestion()


# mengambil pertanyaan dari list pertanyaanku sesuai dengan currentQuestionIndex
# kemudian mengubah teks labelQuestion dan buttonOption sesuai dengan pertanyaan
def showQuestion():
    # jika sudah selesai semua pertanyaan, tampilkan skor
    if currentQuestionIndex >= len(pertanyaanku):
        labelQuestion.config(text="Kuis Selesai!")
        labelCorrectCount.config(text=f"Skor Anda: {correctAnswers} / {len(pertanyaanku)}")
        buttonOption1.pack_forget()
        buttonOption2.pack_forget()
        buttonOption3.pack_forget()
        buttonOption4.pack_forget()
        return
    
    # tapi jika belum, tampilkan pertanyaan berikutnya
    currentQuestion = pertanyaanku[currentQuestionIndex]
    labelQuestion.config(text=currentQuestion.question)
    labelCorrectCount.config(text=f"Jawaban Benar: {correctAnswers} / {len(pertanyaanku)}")
    buttonOption1.config(text=currentQuestion.options[0], command=lambda: onOptionClick(currentQuestion.isCorrect(0)))
    buttonOption2.config(text=currentQuestion.options[1], command=lambda: onOptionClick(currentQuestion.isCorrect(1)))
    buttonOption3.config(text=currentQuestion.options[2], command=lambda: onOptionClick(currentQuestion.isCorrect(2)))
    buttonOption4.config(text=currentQuestion.options[3], command=lambda: onOptionClick(currentQuestion.isCorrect(3)))
    # kenapa command=lambda: onOptionClick(currentQuestion.isCorrect(0))?
    # agak susah jelasinnya wkkwkw
    # https://stackoverflow.com/questions/8269096/why-is-button-parameter-command-executed-when-declared

# tampilkan pertanyaan pertama
showQuestion()

# menampilkan window
window.mainloop()
