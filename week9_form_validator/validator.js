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

        // Cleaning the form every time the submit button is hit
        console.clear()
        console.log("Validation Starter!");

        // finding every input inside of THIS form
        const inputs = this.form.querySelectorAll("input[data-rules]");
        let isFormValid = true;

        // looping all the inputs
        inputs.forEach((input) => {

            // extracting the data
            const fieldName = input.id;                          // names
            const fieldValue = input.value.trim();               // what the user typed
            const rulesArray = input.getAttribute('data-rules').split('|');

            rulesArray.forEach((rule) => {

                let ruleName = rule;
                let ruleParam = null;

                if (rule.includes(':')) {
                    const parts = rule.split(":");
                    ruleName = parts[0];
                    ruleParam = parts[1];
                }

                switch(ruleName){

                    case 'required':
                        if (fieldName === '');
                        console.log(`X [${fieldName}]: This field is required.`);
                        isFormValid = false;
                }
            });

            console.log(`Checking Field [${fieldName}]`);
            console.log(` - Value Typed [${fieldValue}]`);
            console.log(` - Rules to Run:`, rulesArray);
        });
        console.log("\n----------------")
    }
}

const signupValidator = new Validator('register-form')