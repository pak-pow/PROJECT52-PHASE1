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

    showError(input, message){

        const formControl = input.parentElement;
        const small = formControl.querySelector('small')
        formControl.className = 'form-control error';
        small.innerText = message;

    }

    showSuccess(input){
        const formControl = input.parentElement;
        formControl.className = 'form-control';
    }
    
    getFieldName(input) {
        return input.id.charAt(0).toUpperCase() + input.id.slice(1);
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
            const prettyName = this.getFieldName(input);

            this.showSuccess(input);
            let hasError = false

            for (let rule of rulesArray){

                if (hasError) break;

                let ruleName = rule;
                let ruleParam = null;

                if (rule.includes(':')) {
                    const parts = rule.split(":");
                    ruleName = parts[0];
                    ruleParam = parts[1];
                }

                switch(ruleName){

                    case 'required':
                        if (fieldValue === ''){;
                            this.showError(input, `${prettyName} is required`);
                            hasError = true;
                            isFormValid = false;
                        }

                        break;

                    case 'min':
                        if (fieldValue !== '' && fieldValue.length < parseInt(ruleParam)) {
                            this.showError(input, `${prettyName} must be at least ${ruleParam} characters`);
                            hasError = true;
                            isFormValid = false;
                        }
                        break;

                    case 'email':
                        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                        if (fieldValue !== '' && !emailRegex.test(fieldValue)) {
                            this.showError(input, `${prettyName} is not a valid email`);
                            hasError = true;
                            isFormValid = false;
                        }
                        break;
                }
            };
        });
        console.log("\n----------------")

        if(isFormValid){
            console.log("SUCCESS: All Fields Are Valid!");
        } else {
            console.log("WARNING: Forms Contains Error");
        };
    }
}

const signupValidator = new Validator('register-form')