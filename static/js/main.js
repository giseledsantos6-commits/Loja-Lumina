document.addEventListener('DOMContentLoaded', () => {
    let cartCount = 0;
    const cartElement = document.getElementById('cart-count');
    const addToCartButtons = document.querySelectorAll('.add-to-cart');

    // Adiciona evento de clique a todos os botões de adicionar ao carrinho
    addToCartButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            const productName = e.target.getAttribute('data-nome');
            cartCount++;
            if (cartElement) {
                cartElement.textContent = cartCount;
            }
            alert(`"${productName}" foi adicionado ao seu carrinho!`);
        });
    });

    // Manipulação do formulário de contato (se estiver na página de contato)
    const formContato = document.getElementById('form-contato');
    if (formContato) {
        formContato.addEventListener('submit', (e) => {
            e.preventDefault();
            alert('Obrigado pela sua mensagem! Entraremos em contato em breve.');
            formContato.reset();
        });
    }
});
