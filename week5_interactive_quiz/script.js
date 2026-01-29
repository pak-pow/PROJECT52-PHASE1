// ==========================
// 1. SELECTORS & VARIABLES
// ==========================
const quizCard = document.getElementById('quiz-card');
const resultCard = document.getElementById('result-card');
const finalScoreElement = document.getElementById('final-score');
const hintElement = document.getElementById('hint-text');
const questionElement = document.getElementById("question-text");
const scoreElement = document.getElementById("score");
const optionButtons = document.querySelectorAll(".option-btn"); // Changed to match HTML class
const nextButton = document.getElementById("next-btn");

let currentQuestionIndex = 0;
let score = 0;

// ==========================
// 2. THE DATA
// ==========================
const questions = [
  {
    question: "Which language runs in a web browser?",
    options: ["Java", "C", "Python", "JavaScript"],
    correct: "JavaScript",
    hint: "It's the only one natively supported by Chrome and Firefox."
  },
  {
    question: "What does CSS stand for?",
    options: ["Central Style Sheets", "Cascading Style Sheets", "Cascading Simple Sheets", "Cars SUVs Sailboats"],
    correct: "Cascading Style Sheets",
    hint: "It describes how HTML elements are displayed on screen."
  },
  {
    question: "What year was JavaScript launched?",
    options: ["1996", "1995", "1994", "None of the above"],
    correct: "1995",
    hint: "It was created by Brendan Eich in 10 days in the mid-90s."
  },
  {
    question: "Which HTML tag is used for JavaScript?",
    options: ["<js>", "<script>", "<javascript>", "<code >"],
    correct: "<script>",
    hint: "It sounds like what an actor reads from."
  },
];

// ==========================
// 3. FUNCTIONS
// ==========================

function loadQuestion() {
  const currentQuestionData = questions[currentQuestionIndex];

  // 1. Update Text
  questionElement.innerText = currentQuestionData.question;
  hintElement.innerText = `💡 Hint: ${currentQuestionData.hint}`;
  
  // 2. Reset UI State
  hintElement.classList.add('hide');
  nextButton.disabled = true; // Gray out Next button
  
  // 3. Update Buttons
  optionButtons.forEach((button, index) => {
    button.innerText = currentQuestionData.options[index];
    button.classList.remove("correct", "wrong");
    button.disabled = false;
  });
}

function showHint() {
    hintElement.classList.remove('hide');
}

function checkAnswer(selectedButton) {
  const selectedAnswer = selectedButton.innerText;
  const correctAnswer = questions[currentQuestionIndex].correct;

  // 1. Logic Check
  if (selectedAnswer === correctAnswer) {
    selectedButton.classList.add('correct');
    score++;
    scoreElement.innerText = score;
  } else {
    selectedButton.classList.add('wrong');
    // Show correct answer
    optionButtons.forEach(btn => {
      if (btn.innerText === correctAnswer) {
        btn.classList.add("correct");
      }
    });
  }

  // 2. Lock Board
  optionButtons.forEach(btn => {
    btn.disabled = true;
  });

  // 3. Unlock Next Button
  nextButton.disabled = false;
}

function showResults(){
  quizCard.classList.add('hide');
  resultCard.classList.remove('hide');
  finalScoreElement.innerText = `${score} / ${questions.length}`;
}

function restartQuiz() {
    currentQuestionIndex = 0;
    score = 0;
    scoreElement.innerText = 0;
    resultCard.classList.add('hide');
    quizCard.classList.remove('hide');
    loadQuestion();
}

// ==========================
// 4. EVENT LISTENERS
// ==========================

// We handle the Next click HERE, outside of other functions
nextButton.addEventListener('click', () => {
    currentQuestionIndex++;
    if (currentQuestionIndex < questions.length) {
      loadQuestion();
    } else {
      showResults();
    }
});

// START
loadQuestion();