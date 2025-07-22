const endpoint = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSHEET_ID/pub?output=csv";

fetch(endpoint)
  .then(res => res.text())
  .then(csv => {
    const linhas = csv.trim().split("\n");
    const dados = linhas.slice(1).map(linha => linha.split(","));

    const tbody = document.querySelector("#tabela-pedidos tbody");
    tbody.innerHTML = "";

    dados.forEach(linha => {
      const tr = document.createElement("tr");
      linha.forEach(coluna => {
        const td = document.createElement("td");
        td.textContent = coluna;
        tr.appendChild(td);
      });
      tbody.appendChild(tr);
    });
  })
  .catch(err => {
    const tbody = document.querySelector("#tabela-pedidos tbody");
    tbody.innerHTML = `<tr><td colspan="8">Erro ao carregar dados: ${err.message}</td></tr>`;
  });
