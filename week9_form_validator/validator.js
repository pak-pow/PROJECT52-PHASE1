class Validator {
    constructor(formId){
        this.form = document.getElementById(formId);

        if (!this.form){
            console.error(`Validator Error: Form with ID '${formId}' not found.`);
            return;
        }

        this.form.addEventListener('submit', (event) => {
            event.preventDefault();
            this.validateForm();
        });
    }

    validateForm(){
        
    }
}