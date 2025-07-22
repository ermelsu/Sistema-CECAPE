document.getElementById("pedidoForm").addEventListener("submit", function(event) {
  event.preventDefault();

  const nome = document.getElementById("nome").value;
  const email = document.getElementById("email").value;
  const setor = document.getElementById("setor").value;
  const dataPrevista = document.getElementById("data-prevista").value;
  const produtos = [];

  const linhas = document.querySelectorAll("#produtos tbody tr");
  linhas.forEach(linha => {
    const codigo = linha.querySelector("input[name='codigo[]']").value;
    const descricao = linha.querySelector("input[name='descricao[]']").value;
    const quantidade = linha.querySelector("input[name='quantidade[]']").value;
    produtos.push({ codigo, descricao, quantidade });
  });

  fetch("https://script.google.com/macros/s/AKfycbxEt9saMTxqV-91_fRWf24iGoz0Sm8UgHMEcoYTeAd7eWgsRZiSVKHkA7oi1h2pKsNbVw/exec", {
    method: "POST",
    body: JSON.stringify({ nome, email, setor, dataPrevista, produtos }),
    headers: { "Content-Type": "application/json" }
  })
  .then(res => res.json())
  .then(data => {
    alert("Pedido enviado com sucesso!");
    document.getElementById("pedidoForm").reset();
    document.querySelector("#produtos tbody").innerHTML = `
      <tr>
        <td><input type="text" name="codigo[]" required></td>
        <td><input type="text" name="descricao[]" required></td>
        <td><input type="number" name="quantidade[]" required></td>
        <td><button type="button" onclick="removerLinha(this)">Remover</button></td>
      </tr>
    `;
  })
  .catch(error => alert("Erro ao enviar pedido: " + error.message));
});

function adicionarLinha() {
  const tabela = document.querySelector("#produtos tbody");
  const novaLinha = document.createElement("tr");
  novaLinha.innerHTML = `
    <td><input type="text" name="codigo[]" required></td>
    <td><input type="text" name="descricao[]" required></td>
    <td><input type="number" name="quantidade[]" required></td>
    <td><button type="button" onclick="removerLinha(this)">Remover</button></td>
  `;
  tabela.appendChild(novaLinha);
}

function removerLinha(botao) {
  const linha = botao.parentElement.parentElement;
  linha.remove();
}
