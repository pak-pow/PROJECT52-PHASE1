// ==========================
// 1. SELECTORS & VARIABLES
// ==========================
// We "reach into" the HTML to grab specific elements so we can control them.
const homeScreen = document.getElementById("home-screen");      // The Main Menu Div
const creatorScreen = document.getElementById("creator-screen");// The "Add Question" Div
const gameScreen = document.getElementById("game-screen");      // The Quiz Playing Div
const resultCard = document.getElementById("result-card");      // The Final Score Div
const quizCard = document.getElementById("quiz-card");          // The inner card inside the game screen

// Text Elements (Where we inject strings)
const questionElement = document.getElementById("question-text"); // The <h2> where the question goes
const hintElement = document.getElementById("hint-text");         // The <p> for the hint
const scoreElement = document.getElementById("score");            // The small score counter in header
const finalScoreElement = document.getElementById("final-score"); // The big score at the end

// Button Groups
// CRITICAL FIX FROM DAY 6: We specifically look inside "#game-screen" to avoid grabbing the Home Menu buttons by mistake.
const optionButtons = document.querySelectorAll("#game-screen .option-btn"); 
const nextButton = document.getElementById("next-btn");

// CREATOR INPUTS (The form fields)
const newQ = document.getElementById("new-q");
const newA = document.getElementById("new-a");
const newB = document.getElementById("new-b");
const newC = document.getElementById("new-c");
const newD = document.getElementById("new-d");
const newCorrect = document.getElementById("new-correct");
const newHint = document.getElementById("new-hint");

// STATE VARIABLES (The Memory)
let currentQuestionIndex = 0; // Tracks which question we are on (0, 1, 2...)
let score = 0;                // Tracks how many points the user has
let questions = [];           // An empty list that we will fill with data later

// ==========================
// 2. THE DATA
// ==========================
// This is the "Fallback" data. If the user has no saved questions, we use these.
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

// FUNCTION: Load data from the browser's hard drive (Local Storage)
function loadQuestionsFromStorage() {
  // 1. Check if "myQuizQuestions" exists in the browser's storage
  const stored = localStorage.getItem("myQuizQuestions");
  
  if (stored) {
    // 2. If yes, turn the text string back into a JavaScript Array (JSON.parse)
    questions = JSON.parse(stored);
  } else {
    // 3. If no, load the defaults defined above
    questions = defaultQuestions;
  }
}

// FUNCTION: Save a new question from the Creator Mode
function saveQuestion() {
  // 1. Validation: Don't save if the Question or Answer is empty!
  if (!newQ.value || !newCorrect.value) {
    alert("Please fill in at least the Question and Correct Answer!");
    return; // Stop the function here
  }

  // 2. Object Creation: Pack the inputs into a neat JSON object
  const newQuestion = {
    question: newQ.value,
    options: [newA.value, newB.value, newC.value, newD.value], // Array of options
    correct: newCorrect.value,
    hint: newHint.value || "No hint available.", // Logical OR: If hint is empty, use default string
  };

  // 3. Update State: Add to our list
  questions.push(newQuestion);
  
  // 4. Persist: Save the updated list to the browser (Must convert Array -> String with JSON.stringify)
  localStorage.setItem("myQuizQuestions", JSON.stringify(questions));

  // 5. Feedback & Cleanup
  alert("Question Saved!");
  // Clear all text boxes so they are ready for the next question
  newQ.value = ""; newA.value = ""; newB.value = "";
  newC.value = ""; newD.value = ""; newCorrect.value = ""; newHint.value = "";

  // 6. Navigate back to Main Menu
  goHome();
}

// FUNCTION: Delete custom data and restore the original quiz
function resetDefaults() {
  localStorage.removeItem('myQuizQuestions'); // Delete the file
  questions = defaultQuestions;               // Reload RAM with defaults
  alert("Questions reset to default!");       // Tell user
}

// FUNCTION: Navigation - Show Home, Hide everything else
function goHome() {
  homeScreen.classList.remove("hide");    // Show
  creatorScreen.classList.add("hide");    // Hide
  gameScreen.classList.add("hide");       // Hide
  resultCard.classList.add("hide");       // Hide
}

function showCreator() {
  homeScreen.classList.add("hide");
  creatorScreen.classList.remove("hide");
  loadQuestionsFromStorage(); // Load existing so we don't overwrite
}

// FUNCTION: Start the Game
function startQuiz() {
  loadQuestionsFromStorage(); // Ensure we have the latest questions

  // Safety Check: What if the list is empty?
  if (questions.length === 0) {
    alert("No questions found! Go create some first.");
    return;
  }

  // Reset Game State (Score and Index must be 0)
  currentQuestionIndex = 0;
  score = 0;
  scoreElement.innerText = 0;

  // Switch Screens
  homeScreen.classList.add("hide");
  gameScreen.classList.remove("hide");
  quizCard.classList.remove("hide"); 

  loadQuestion(); // Run the logic to display Question #1
}

// FUNCTION: Inject the current question into the HTML
function loadQuestion() {
  // 1. Get the data for the current index (e.g., Question 0)
  const currentQuestionData = questions[currentQuestionIndex];

  // 2. Inject Text into the DOM
  questionElement.innerText = currentQuestionData.question;
  hintElement.innerText = `💡 Hint: ${currentQuestionData.hint}`;

  // 3. Reset UI State for the new question
  hintElement.classList.add("hide"); // Hide hint
  nextButton.disabled = true;        // Disable "Next" button (User must pick an answer first)

  // 4. Update the 4 Option Buttons
  optionButtons.forEach((button, index) => {
    button.innerText = currentQuestionData.options[index]; // Set text
    button.classList.remove("correct", "wrong");           // Remove old colors (Green/Red)
    button.disabled = false;                               // Make clickable again
  });
}

function showHint() {
  hintElement.classList.remove("hide");
}

// FUNCTION: Logic for checking if the click was right or wrong
function checkAnswer(selectedButton) {
  const selectedAnswer = selectedButton.innerText;
  const correctAnswer = questions[currentQuestionIndex].correct;

  // 1. Compare Strings
  if (selectedAnswer === correctAnswer) {
    // CORRECT!
    selectedButton.classList.add("correct"); // Turn Green
    score++;                                 // Add Point
    scoreElement.innerText = score;          // Update Header
  } else {
    // WRONG!
    selectedButton.classList.add("wrong");   // Turn Red
    
    // Educational Moment: Find and highlight the RIGHT answer so the user learns
    optionButtons.forEach((btn) => {
      if (btn.innerText === correctAnswer) {
        btn.classList.add("correct");
      }
    });
  }

  // 2. Lock the Board (Disable all buttons so user can't cheat/click twice)
  optionButtons.forEach((btn) => {
    btn.disabled = true;
  });

  // 3. Allow user to proceed
  nextButton.disabled = false; // Enable "Next" button
}

// FUNCTION: Show the final scorecard
function showResults() {
  quizCard.classList.add("hide");       // Hide Questions
  resultCard.classList.remove("hide");  // Show Results
  finalScoreElement.innerText = `${score} / ${questions.length}`; // "3 / 4"
}

function restartQuiz() {
  goHome();
}

// ==========================
// 4. EVENT LISTENERS
// ==========================

// Listener for the "Next Arrow" button
nextButton.addEventListener("click", () => {
  currentQuestionIndex++; // Move to next index
  
  // Logic: Do we have more questions?
  if (currentQuestionIndex < questions.length) {
    loadQuestion(); // Yes? Load it.
  } else {
    showResults();  // No? End Game.
  }
});

// Listener for "Enter Key" navigation in Creator Mode
const creatorInputs = [newQ, newA, newB, newC, newD, newCorrect, newHint];

creatorInputs.forEach((input, index) => {
    input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            e.preventDefault(); // Stop default behavior
            
            const nextInput = creatorInputs[index + 1]; // Find the next box
            
            if (nextInput) {
                nextInput.focus(); // Jump cursor to next box
            } else {
                saveQuestion(); // If no next box, we are at the end. Save!
            }
        }
    });
});

// INITIALIZATION: Run this when the script loads to ensure we start at the Home Screen
goHome();
