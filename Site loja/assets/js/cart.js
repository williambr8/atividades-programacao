let cart = JSON.parse(localStorage.getItem('ribbCart')) || [];

function addToCart(id) {
  const product = products.find(p => p.id === id);
  if (!product) return;

  const existing = cart.find(item => item.id === id);
  if (existing) {
    existing.quantity = (existing.quantity || 1) + 1;
  } else {
    cart.push({ ...product, quantity: 1 });
  }

  localStorage.setItem('ribbCart', JSON.stringify(cart));
  updateCartCount();
  showToast(`${product.name} adicionado ao carrinho!`);
  renderCart();
}

function removeFromCart(id) {
  cart = cart.filter(item => item.id !== id);
  localStorage.setItem('ribbCart', JSON.stringify(cart));
  updateCartCount();
  renderCart();
}

function changeQuantity(id, change) {
  const item = cart.find(i => i.id === id);
  if (item) {
    item.quantity = Math.max(1, (item.quantity || 1) + change);
    localStorage.setItem('ribbCart', JSON.stringify(cart));
    renderCart();
    updateCartCount();
  }
}

function updateCartCount() {
  const countEl = document.getElementById('cart-count');
  if (countEl) {
    countEl.textContent = cart.reduce((acc, item) => acc + (item.quantity || 1), 0);
  }
}

function renderCart() {
  const cartItems = document.getElementById('cart-items');
  const cartTotal = document.getElementById('cart-total');
  if (!cartItems) return;

  cartItems.innerHTML = '';

  if (cart.length === 0) {
    cartItems.innerHTML = `<p class="text-center py-12 text-gray-400">Seu carrinho está vazio</p>`;
    if (cartTotal) cartTotal.textContent = '0,00';
    return;
  }

  let total = 0;
  cart.forEach(item => {
    const itemTotal = item.price * (item.quantity || 1);
    total += itemTotal;

    cartItems.innerHTML += `
      <div class="flex gap-4 border-b border-white/10 pb-6">
        <img src="${item.image}" class="w-20 h-20 object-cover rounded-2xl">
        <div class="flex-1">
          <h4 class="font-medium">${item.name}</h4>
          <p class="text-gold">R$ ${item.price.toFixed(2)}</p>
          <div class="flex items-center gap-3 mt-3">
            <button onclick="changeQuantity(${item.id}, -1)" class="w-7 h-7 border border-white/30 rounded hover:bg-white/10">-</button>
            <span class="w-6 text-center">${item.quantity || 1}</span>
            <button onclick="changeQuantity(${item.id}, 1)" class="w-7 h-7 border border-white/30 rounded hover:bg-white/10">+</button>
            <button onclick="removeFromCart(${item.id})" class="ml-auto text-red-400 text-sm hover:text-red-500">Remover</button>
          </div>
        </div>
      </div>`;
  });

  if (cartTotal) cartTotal.textContent = total.toFixed(2);
}

function toggleCart() {
  const drawer = document.getElementById('cart-drawer');
  if (drawer) {
    drawer.classList.toggle('translate-x-full');
    renderCart();
  }
}

function closeCart() {
  const drawer = document.getElementById('cart-drawer');
  if (drawer) drawer.classList.add('translate-x-full');
}

function finalizePurchase() {
  if (cart.length === 0) {
    alert("Seu carrinho está vazio!");
    return;
  }
  alert("✅ Pedido finalizado com sucesso! (Simulação)");
  cart = [];
  localStorage.setItem('ribbCart', JSON.stringify(cart));
  closeCart();
  updateCartCount();
}

// Torna funções globais
window.addToCart = addToCart;
window.removeFromCart = removeFromCart;
window.changeQuantity = changeQuantity;
window.toggleCart = toggleCart;
window.closeCart = closeCart;
window.finalizePurchase = finalizePurchase;