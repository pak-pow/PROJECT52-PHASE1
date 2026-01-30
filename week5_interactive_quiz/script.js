// ==========================
// 1. SELECTORS & VARIABLES
// ==========================
const homeScreen = document.getElementById("home-screen");
const creatorScreen = document.getElementById("creator-screen");
const gameScreen = document.getElementById("game-screen");
const resultCard = document.getElementById("result-card");
const quizCard = document.getElementById("quiz-card"); // The card inside game screen

const questionElement = document.getElementById("question-text");
const hintElement = document.getElementById("hint-text");
const scoreElement = document.getElementById("score");
const finalScoreElement = document.getElementById("final-score");
const optionButtons = document.querySelectorAll("#game-screen .option-btn");
const nextButton = document.getElementById("next-btn");

// CREATOR INPUTS
const newQ = document.getElementById("new-q");
const newA = document.getElementById("new-a");
const newB = document.getElementById("new-b");
const newC = document.getElementById("new-c");
const newD = document.getElementById("new-d");
const newCorrect = document.getElementById("new-correct");
const newHint = document.getElementById("new-hint");

let currentQuestionIndex = 0;
let score = 0;
let questions = [];

// ==========================
// 2. THE DATA
// ==========================
const defaultQuestions = [
  {
    question: "Which language runs in a web browser?",
    options: ["Java", "C", "Python", "JavaScript"],
    correct: "JavaScript",
    hint: "It's the only one natively supported by Chrome and Firefox.",
  },
  {
    question: "What does CSS stand for?",
    options: [
      "Central Style Sheets",
      "Cascading Style Sheets",
      "Cascading Simple Sheets",
      "Cars SUVs Sailboats",
    ],
    correct: "Cascading Style Sheets",
    hint: "It describes how HTML elements are displayed on screen.",
  },
  {
    question: "What year was JavaScript launched?",
    options: ["1996", "1995", "1994", "None of the above"],
    correct: "1995",
    hint: "It was created by Brendan Eich in 10 days in the mid-90s.",
  },
  {
    question: "Which HTML tag is used for JavaScript?",
    options: ["<js>", "<script>", "<javascript>", "<code >"],
    correct: "<script>",
    hint: "It sounds like what an actor reads from.",
  },
];

// ==========================
// 3. FUNCTIONS
// ==========================

function loadQuestionsFromStorage() {
  const stored = localStorage.getItem("myQuizQuestions");
  if (stored) {
    questions = JSON.parse(stored);
  } else {
    questions = defaultQuestions;
  }
}

function saveQuestion() {
  // 1. Validate (Make sure they typed something)
  if (!newQ.value || !newCorrect.value) {
    alert("Please fill in at least the Question and Correct Answer!");
    return;
  }

  // 2. Create Object
  const newQuestion = {
    question: newQ.value,
    options: [newA.value, newB.value, newC.value, newD.value],
    correct: newCorrect.value,
    hint: newHint.value || "No hint available.",
  };

  // 3. Add to List & Save
  questions.push(newQuestion);
  localStorage.setItem("myQuizQuestions", JSON.stringify(questions));

  // 4. Success & Reset
  alert("Question Saved!");
  newQ.value = "";
  newA.value = "";
  newB.value = "";
  newC.value = "";
  newD.value = "";
  newCorrect.value = "";
  newHint.value = "";

  // 5. Go back home
  goHome();
}

function resetDefaults() {
    // 1. Clear the custom data
    localStorage.removeItem('myQuizQuestions');
    
    // 2. Reload defaults
    questions = defaultQuestions;
    
    // 3. Feedback
    alert("Questions reset to default!");
}

function goHome() {
  homeScreen.classList.remove("hide");
  creatorScreen.classList.add("hide");
  gameScreen.classList.add("hide");
  resultCard.classList.add("hide");
}

function showCreator() {
  homeScreen.classList.add("hide");
  creatorScreen.classList.remove("hide");
  loadQuestionsFromStorage(); // Load existing so we don't overwrite
}

function startQuiz() {
  loadQuestionsFromStorage(); // Load latest data

  if (questions.length === 0) {
    alert("No questions found! Go create some first.");
    return;
  }

  // Reset Game State
  currentQuestionIndex = 0;
  score = 0;
  scoreElement.innerText = 0;

  // Switch Screens
  homeScreen.classList.add("hide");
  gameScreen.classList.remove("hide");
  quizCard.classList.remove("hide"); // Ensure the card itself is visible

  loadQuestion();
}

function loadQuestion() {
  const currentQuestionData = questions[currentQuestionIndex];

  // 1. Update Text
  questionElement.innerText = currentQuestionData.question;
  hintElement.innerText = `💡 Hint: ${currentQuestionData.hint}`;

  // 2. Reset UI State
  hintElement.classList.add("hide");
  nextButton.disabled = true; // Gray out Next button

  // 3. Update Buttons
  optionButtons.forEach((button, index) => {
    button.innerText = currentQuestionData.options[index];
    button.classList.remove("correct", "wrong");
    button.disabled = false;
  });
}

function showHint() {
  hintElement.classList.remove("hide");
}

function checkAnswer(selectedButton) {
  const selectedAnswer = selectedButton.innerText;
  const correctAnswer = questions[currentQuestionIndex].correct;

  // 1. Logic Check
  if (selectedAnswer === correctAnswer) {
    selectedButton.classList.add("correct");
    score++;
    scoreElement.innerText = score;
  } else {
    selectedButton.classList.add("wrong");
    // Show correct answer
    optionButtons.forEach((btn) => {
      if (btn.innerText === correctAnswer) {
        btn.classList.add("correct");
      }
    });
  }

  // 2. Lock Board
  optionButtons.forEach((btn) => {
    btn.disabled = true;
  });

  // 3. Unlock Next Button
  nextButton.disabled = false;
}

function showResults() {
  quizCard.classList.add("hide");
  resultCard.classList.remove("hide");
  finalScoreElement.innerText = `${score} / ${questions.length}`;
}

function restartQuiz() {
  goHome();
}

// ==========================
// 4. EVENT LISTENERS
// ==========================

// We handle the Next click HERE, outside of other functions
nextButton.addEventListener("click", () => {
  currentQuestionIndex++;
  if (currentQuestionIndex < questions.length) {
    loadQuestion();
  } else {
    showResults();
  }
});

const creatorInputs = [newQ, newA, newB, newC, newD, newCorrect, newHint];

creatorInputs.forEach((input, index) => {
    input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            e.preventDefault(); // Stop it from doing anything else
            
            const nextInput = creatorInputs[index + 1];
            
            if (nextInput) {
                // If there is a next box, jump to it
                nextInput.focus();
            } else {
                // If we are at the last box (Hint), SAVE the question!
                saveQuestion();
            }
        }
    });
});

// START
goHome();
