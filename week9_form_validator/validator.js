class Validator {
    constructor(formId){

        // find the form in the html
        this.form = document.getElementById(formId);

        if (!this.form){
            console.error(`Validator Error: Form with ID '${formId}' not found.`);
            return;
        }

        // Finds all input
        this.inputs = this.form.querySelectorAll('input[data-rules]');
        
        // Listen for the submit form
        this.form.addEventListener('submit', (event) => {
            
            // Preventing the page from refreshing the page
            event.preventDefault();

            // running the class
            this.validateForm();
        });

        // listen for typing in real-time
        this.inputs.forEach((input) => {
            input.addEventListener('input', () => {
                
                // checking just this one field as they type
                this.validateField(input);
            });
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

    validateField(input) {
        const fieldValue = input.value.trim();
        const rulesArray = input.getAttribute('data-rules').split('|');
        const prettyName = this.getFieldName(input);

        this.showSuccess(input); // Reset first
        let hasError = false;

        for (let rule of rulesArray) {
            if (hasError) break; 

            let ruleName = rule;
            let ruleParam = null;

            if (rule.includes(':')) {
                const parts = rule.split(':');
                ruleName = parts[0];
                ruleParam = parts[1];
            }

            switch (ruleName) {
                case 'required':
                    if (fieldValue === '') {
                        this.showError(input, `${prettyName} is required`);
                        hasError = true;
                    }
                    break;
                    
                case 'min':
                    if (fieldValue !== '' && fieldValue.length < parseInt(ruleParam)) {
                        this.showError(input, `${prettyName} must be at least ${ruleParam} characters`);
                        hasError = true;
                    }
                    break;
                    
                case 'email':
                    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                    if (fieldValue !== '' && !emailRegex.test(fieldValue)) {
                        this.showError(input, `${prettyName} is not a valid email`);
                        hasError = true;
                    }
                    break;
            }
        }
        
        return !hasError; 
    }
    validateAll() {
        let isFormValid = true; 

        this.inputs.forEach((input) => {
            // Check each field. If even one fails, the whole form is invalid.
            const isFieldValid = this.validateField(input);
            if (!isFieldValid) {
                isFormValid = false;
            }
        });

        if (isFormValid) {
            console.log("✅ SUCCESS: Sending data to server...");
            // this.form.submit();
        }
    }
}

const signupValidator = new Validator('register-form')