const toggleButton = document.getElementById('billing-toggle');
const toggleCircle = document.getElementById('toggle-circle');

const priceStarter = document.getElementById('price-starter');
const pricePro = document.getElementById('price-pro');
const priceEnterprise = document.getElementById('price-enterprise');

const price = {
    monthly: {starter: 0, pro: 29, enterprise: 99},
    yearly: {starter: 0, pro: 290, enterprise: 999}
};

let isYearly = false;

toggleButton.addEventListener('click', () => {

    isYearly = !isYearly;
    if(isYearly){

        toggleCircle.classList.add('translate-x-6');
        toggleButton.classList.remove('bg-gray-600');
        toggleButton.classList.add('bg-purple-600');

        priceStarter.textContent = price.yearly.starter;
        pricePro.textContent = price.yearly.pro;
        priceEnterprise.textContent = price.yearly.enterprise;
    } else {

        toggleCircle.classList.remove('translate-x-6');
        toggleButton.classList.remove('bg-purple-600');
        toggleButton.classList.add('bg-gray-600');

        priceStarter.textContent = prices.monthly.starter;
        pricePro.textContent = prices.monthly.pro;
        priceEnterprise.textContent = prices.monthly.enterprise;

    }
});