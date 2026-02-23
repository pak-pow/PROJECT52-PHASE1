class Validator {
    constructor(formId){

        // find the form in the html
        this.form = document.getElementById(formId);

        if (!this.form){
            console.error(`Validator Error: Form with ID '${formId}' not found.`);
            return;
        }

        this.form.addEventListener('submit', (event) => {
            
            // Preventing the page from refreshing the page
            event.preventDefault();

            // running the class
            this.validateForm();
        });
    }

    validateForm(){
        console.log("Validation Starter!");

        // finding every input inside of THIS form
        const inputs = this.form.querySelectorAll("input[data-rules]");

        // looping all the inputs
        inputs.forEach((input) => {

            // extracting the data
            const fieldName = input.id;                          // names
            const fieldValue = input.value.trim();               // what the user typed
            const ruleString = input.getAttribute('data-rules');

            // chopping the text into the a list or a array
            const rulesArray = ruleString.split('|');

            console.log(`Checking Field [${fieldName}]`);
            console.log(` - Value Typed [${fieldValue}]`);
            console.log(` - Rules to Run:`, rulesArray);
        });
        console.log("\n----------------")
    }
}

const signupValidator = new Validator('register-form')