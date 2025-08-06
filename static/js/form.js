// Função para adicionar nova linha na tabela de produtos
function adicionarLinha() {
  const tabela = document.getElementById('produtos').getElementsByTagName('tbody')[0];

  // Cria uma nova linha
  const novaLinha = tabela.insertRow();

  // Colunas: Código
  const codigoCell = novaLinha.insertCell(0);
  codigoCell.innerHTML = '<input type="text" name="codigo[]" required />';

  // Colunas: Descrição
  const descricaoCell = novaLinha.insertCell(1);
  descricaoCell.innerHTML = '<input type="text" name="descricao[]" required />';

  // Colunas: Quantidade
  const qtdCell = novaLinha.insertCell(2);
  qtdCell.innerHTML = '<input type="number" name="quantidade[]" required />';

  // Colunas: Botão remover
  const acaoCell = novaLinha.insertCell(3);
  acaoCell.innerHTML = '<button type="button" onclick="removerLinha(this)">Remover</button>';
}

// Função para remover linha clicada
function removerLinha(botao) {
  const linha = botao.closest('tr');
  linha.remove();
}
