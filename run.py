# coding=utf-8
import random
import atexit

class Question:
  def __init__(self, question, correctAnswer, correctCount, targetCount, lineText, index):
    self.question = question
    self.correctAnswer = correctAnswer
    self.correctCount = correctCount
    self.targetCount = targetCount
    self.index = index
    self.lineText = lineText

def find(pred, iterable):
  for element in iterable:
    if pred(element):
      return element
    return None

class Player:
  def __init__(self, questions):
    self.questions = questions
    atexit.register(self.saveQuestions)

  def play(self):
    currentQuestion = self.findUnlearnedQuestion()
    self.currentQuestion = currentQuestion
    while(self.currentQuestion is not None):
      self.ask()
      self.waitForAnswer()
      self.currentQuestion = self.findUnlearnedQuestion()

  def findUnlearnedQuestion(self):
    unlookedIndexes = range(len(self.questions))
    random.shuffle(unlookedIndexes)
    for x in unlookedIndexes:
      question = self.questions[x]
      if question.correctCount != question.targetCount:
        return question
      else:
        unlookedIndexes.remove(x)
    # return find(lambda question: getattr(question, 'correctCount') != getattr(question, 'targetCount'), self.questions)

  def createChoices(self):
    index = self.currentQuestion.index
    randomQuestionIndexes = random.sample(range(len(self.questions)), 4)
    if index in randomQuestionIndexes:
      randomQuestionIndexes.remove(index)
    else:
      randomQuestionIndexes.pop()
    choices = map(lambda i: self.questions[i].correctAnswer, randomQuestionIndexes)
    choices.append(self.currentQuestion.correctAnswer)
    random.shuffle(choices)

    choiceLetters = ['a','b','c','d']
    choicesTextToPrint = ''

    for i,choice in enumerate(choices):
      choicesTextToPrint += "{}: {}\n".format(choiceLetters[i].upper(), choice)
      if(choice == self.currentQuestion.correctAnswer):
        self.correctChoiceLetter = choiceLetters[i]
    self.choicesTextToPrint = choicesTextToPrint


  def ask(self):
    self.createChoices()
    print("{} ?\n".format(self.currentQuestion.question))
    print(self.choicesTextToPrint)


  def waitForAnswer(self):
    selectedChoice = raw_input("")
    if selectedChoice == self.correctChoiceLetter or selectedChoice == self.correctChoiceLetter.upper():
      print('True')
      self.currentQuestion.correctCount = str(int(self.currentQuestion.correctCount) + 1)
    else:
      print('False')
      self.currentQuestion.correctCount = str(int(self.currentQuestion.correctCount) - 1)
    self.updateLineText()

  def updateLineText(self):
    cq = self.currentQuestion
    cc = cq.correctCount
    q = cq.question
    ca = cq.correctAnswer
    tc = cq.targetCount
    self.currentQuestion.lineText = "{},{},{},{}".format(q,ca,cc,tc)

  def saveQuestions(self):
    with open('words.txt', 'w') as file:
      file.write('\n'.join(map(lambda q: "{}".format(q.lineText), self.questions)))
      

with open('words.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    questions = []
    for i,line in enumerate(lines):
      a,b,c,d = line.split(',')
      questions.append(Question(a, b, c, d, line, i))
    player = Player(questions)
    player.play()
