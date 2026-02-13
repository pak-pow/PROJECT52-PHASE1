const toggleButton = document.getElementById('billing-toggle')
const toggleCircle = document.getElementById('toggle-circle')

const priceStarter = document.getElementById('price-starter')
const pricePro = document.getElementById('price-pro')
const priceEnterprise = document.getElementById('price-enterprise')

const price = {
    monthly: {starter: 0, pro: 29, enterprise: 99},
    yearly: {starter: 0, pro: 290, enterprise: 999}
}