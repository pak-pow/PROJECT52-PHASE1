// array of questions
const questions = [
  {
    question: "Which language runs in a web browser?",
    options: ["Java", "C", "Python", "JavaScript"],
    correct: "JavaScript",
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
  },

  {
    question: "What year was JavaScript launched?",
    options: ["1996", "1995", "1994", "None of the above"],
    correct: "1995",
  },

  {
    question: "Which HTML tag is used for JavaScript?",
    options: ["<js>", "<script>", "<javascript>", "<code >"],
    correct: "<script>",
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
  console.log("Button clicked:", selectedButton.innerText);
}

loadQuestion();
