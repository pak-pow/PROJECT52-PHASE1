// array of questions
const quizCard = document.getElementById('quiz-card');
const resultCard = document.getElementById('result-card');
const finalScoreElement = document.getElementById('final-score');

const questions = [
  {
    question: "Which language runs in a web browser?",
    options: ["Java", "C", "Python", "JavaScript"],
    correct: "JavaScript",
    hint: "It's the only one natively supported by Chrome and Firefox."
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

// current states
let currentQuestionIndex = 0;
let score = 0;

// dom selector
const questionElement = document.getElementById("question-text");
const scoreElement = document.getElementById("score");

// selecting all buttons inside the options container
const optionButtons = document.querySelectorAll(".options-container .btn");
const nextButton = document.getElementById("next-btn");

// functions
function loadQuestion() {
  // getting the data from the current question
  const currentQuestionData = questions[currentQuestionIndex];

  // updating the quesion text
  questionElement.innerText = currentQuestionData.question;

  // updating the option buttons
  // looping through the 4 buttons and text from the data
  optionButtons.forEach((button, index) => {
    button.innerText = currentQuestionData.options[index];
    button.classList.remove("correct", "wrong");
    button.disabled = false;
  });

  // hide the next button until it is answered
  nextButton.classList.add("hide");
}

function checkAnswer(selectedButton) {
  const selectedAnswer = selectedButton.innerText;
  const correctAnswer = questions[currentQuestionIndex].correct;

  // logic 
  if (selectedAnswer == correctAnswer) {
    
    // turn green
    selectedButton.classList.add('correct');
    
    // increment 1 point
    score++;

    // update screen
    scoreElement.innerText = score;

  } else {

    // turn red
    selectedButton.classList.add('wrong');

    // showing the user the right answer 
    optionButtons.forEach(btn => {
      if (btn.innerText === correctAnswer) {
        btn.classList.add("correct");
      }
    });
  }

  optionButtons.forEach(btn => {
    btn.disabled = true;
  })

  nextButton.classList.remove('hide')

  nextButton.addEventListener('click', () => {

    currentQuestionIndex++;

    if (currentQuestionIndex < questions.length) {
      loadQuestion();

    } else {
      showResults();
    }
  });
}

function showResults(){

  // hide the question card and next button
  quizCard.classList.add('hide');
  nextButton.classList.add('hide');

  // show the result card
  resultCard.classList.remove('hide');

  // update the final score text
  finalScoreElement.innerText = `${score} / ${questions.length}`;

}

function restartQuiz() {
    // 1. Reset Logic
    currentQuestionIndex = 0;
    score = 0;
    scoreElement.innerText = 0;
    
    // 2. Reset UI (Hide Result, Show Question)
    resultCard.classList.add('hide');
    quizCard.classList.remove('hide');
    
    // 3. Load First Question
    loadQuestion();
}

loadQuestion();
