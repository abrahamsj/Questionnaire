
// not sureif this will stay
document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    
    form.addEventListener('submit', (event) => {
        const name = document.getElementById('name').value;
        const date = document.getElementById('date').value;
        
        if (!name || !date) {
            alert('Please fill in all required fields.');
            event.preventDefault();
        }
    });
});
