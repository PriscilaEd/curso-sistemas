window.mostrarPromocao = function() {
  const nome  = document.querySelector('#medicamento').value.trim();
  const preco = Number(document.querySelector('#preco').value);
  if (!nome || !preco) {
    document.querySelector('#saida').textContent = 'Preencha medicamento e preço.';
    return;
  }
  const total = Math.floor(preco * 2);
  document.querySelector('#saida').innerHTML =
    `Promoção de ${nome}<br>Leve 2 por apenas R$: ${total.toFixed(2)}`;
}