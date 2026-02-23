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

        inputs.forEach((input) => {

            const fieldName = input.id;
            const fieldValue = input.value.trim();
            const ruleString = input.getAttribute('data-rules')
        })
        console.log("Ready to process inputs")
    }
}

const signupValidator = new Validator('register-form')