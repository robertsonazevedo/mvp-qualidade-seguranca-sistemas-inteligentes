/*
  --------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
  let url = 'http://127.0.0.1:5000/pacientes';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.pacientes.forEach(item => insertList(item.name, 
                                                item.a1_score, 
                                                item.a2_score,
                                                item.a3_score,
                                                item.a4_score,
                                                item.a5_score,
                                                item.a6_score,
                                                item.a7_score,
                                                item.a8_score,
                                                item.a9_score,
                                                item.a10_score,
                                                item.gender_cod,
                                                item.jaundice_cod,
                                                item.autism_cod,
                                                item.relation_cod,
                                                item.outcome
                                              ))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Chamada da função para carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/
getList()




/*
  --------------------------------------------------------------------------------------
  Função para colocar um item na lista do servidor via requisição POST
  --------------------------------------------------------------------------------------
*/
const postItem = async (inputPatient, inputA1_score, inputA2_score,
                        inputA3_score, inputA4_score, inputA5_score, 
                        inputA6_score, inputA7_score, inputA8_score,
                        inputA9_score, inputA10_score, inputGender_cod,
                        inputJaundice_cod, inputAutism_cod, inputRelation_cod) => {
    
  const formData = new FormData();
  formData.append('name', inputPatient);
  formData.append('a1_score', inputA1_score);
  formData.append('a2_score', inputA2_score);
  formData.append('a3_score', inputA3_score);
  formData.append('a4_score', inputA4_score);
  formData.append('a5_score', inputA5_score);
  formData.append('a6_score', inputA6_score);
  formData.append('a7_score', inputA7_score);
  formData.append('a8_score', inputA8_score);
  formData.append('a9_score', inputA9_score);
  formData.append('a10_score', inputA10_score);
  formData.append('gender_cod', inputGender_cod);
  formData.append('jaundice_cod', inputJaundice_cod);
  formData.append('autism_cod', inputAutism_cod);
  formData.append('relation_cod', inputRelation_cod);

  let url = 'http://127.0.0.1:5000/paciente';
  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Função para criar um botão close para cada item da lista
  --------------------------------------------------------------------------------------
*/
const insertDeleteButton = (parent) => {
  let span = document.createElement("span");
  let txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  parent.appendChild(span);
}

/*
  --------------------------------------------------------------------------------------
  Função para remover um item da lista de acordo com o click no botão close
  --------------------------------------------------------------------------------------
*/
const removeElement = () => {
  let close = document.getElementsByClassName("close");
  // var table = document.getElementById('myTable');
  let i;
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
      let div = this.parentElement.parentElement;
      const nomeItem = div.getElementsByTagName('td')[0].innerHTML
      if (confirm("Você tem certeza?")) {
        div.remove()
        deleteItem(nomeItem)
        alert("Removido!")
      }
    }
  }
}

/*
  --------------------------------------------------------------------------------------
  Função para deletar um item da lista do servidor via requisição DELETE
  --------------------------------------------------------------------------------------
*/
const deleteItem = (item) => {
  console.log(item)
  let url = 'http://127.0.0.1:5000/paciente?name='+item;
  fetch(url, {
    method: 'delete'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Função para adicionar um novo item com nome, quantidade e valor 
  --------------------------------------------------------------------------------------
*/
const newItem = async () => {
  let inputPatient = document.getElementById("newInput").value;
  let inputA1_score = document.getElementById("newA1_score").value;
  let inputA2_score = document.getElementById("newA2_score").value;
  let inputA3_score = document.getElementById("newA3_score").value;
  let inputA4_score = document.getElementById("newA4_score").value;
  let inputA5_score = document.getElementById("newA5_score").value;
  let inputA6_score = document.getElementById("newA6_score").value;
  let inputA7_score = document.getElementById("newA7_score").value;
  let inputA8_score = document.getElementById("newA8_score").value;
  let inputA9_score = document.getElementById("newA9_score").value;
  let inputA10_score = document.getElementById("newA10_score").value;
  let inputGender_cod = document.getElementById("newGender_cod").value;
  let inputJaundice_cod = document.getElementById("newJaundice_cod").value;
  let inputAutism_cod = document.getElementById("newAutism_cod").value;
  let inputRelation_cod = document.getElementById("newRelation_cod").value;

  // Verifique se o nome do produto já existe antes de adicionar
  const checkUrl = `http://127.0.0.1:5000/pacientes?nome=${inputPatient}`;
  fetch(checkUrl, {
    method: 'get'
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.pacientes && data.pacientes.some(item => item.name === inputPatient)) {
        alert("O paciente já está cadastrado.\nCadastre o paciente com um nome diferente ou atualize o existente.");
      } else if (inputPatient === '' || inputA1_score === '' || inputA2_score === '' || inputA3_score === '' || inputA4_score === '' || inputA5_score === '' || inputA6_score === '' || inputA7_score === '' || inputA8_score === '' || inputA9_score === '' || inputA10_score === '' || inputGender_cod === '' || inputJaundice_cod === '' || inputAutism_cod === '' || inputRelation_cod === '') {
        alert("Existem campos vazios. Verifique se preencheu NOME e todos os dados nas caixas de seleções.");
      } else if (isNaN(inputA1_score) || isNaN(inputA2_score) || isNaN(inputA3_score) || isNaN(inputA4_score) || isNaN(inputA5_score) || isNaN(inputA6_score) || isNaN(inputA7_score) || isNaN(inputA8_score) || isNaN(inputA9_score) || isNaN(inputA10_score) || isNaN(inputGender_cod) || isNaN(inputJaundice_cod) || isNaN(inputAutism_cod) || isNaN(inputRelation_cod)) {
        alert("Esse(s) campo(s) precisam ser números!");
      } else {
        insertList(inputPatient, inputA1_score, inputA2_score, inputA3_score, inputA4_score, inputA5_score, inputA6_score, inputA7_score, inputA8_score, inputA9_score, inputA10_score, inputGender_cod, inputJaundice_cod, inputAutism_cod, inputRelation_cod);
        postItem(inputPatient, inputA1_score, inputA2_score, inputA3_score, inputA4_score, inputA5_score, inputA6_score, inputA7_score, inputA8_score, inputA9_score, inputA10_score, inputGender_cod, inputJaundice_cod, inputAutism_cod, inputRelation_cod);
        alert("Paciente adicionado!");
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Função para inserir items na lista apresentada
  --------------------------------------------------------------------------------------
*/
const insertList = (namePatient, a1_score, a2_score, a3_score, a4_score, a5_score, a6_score, a7_score, a8_score, a9_score, a10_score, gender_cod, jaundice_cod, autism_cod, relation_cod, outcome) => {
  var item = [namePatient, a1_score, a2_score, a3_score, a4_score, a5_score, a6_score, a7_score, a8_score, a9_score, a10_score, gender_cod, jaundice_cod, autism_cod, relation_cod, outcome];
  var table = document.getElementById('myTable');
  var row = table.insertRow();

  for (var i = 0; i < item.length; i++) {
    var cell = row.insertCell(i);
    cell.textContent = item[i];
  }

  var deleteCell = row.insertCell(-1);
  insertDeleteButton(deleteCell);


  document.getElementById("newInput").value = "";
  document.getElementById("newA1_score").value = "";
  document.getElementById("newA2_score").value = "";
  document.getElementById("newA3_score").value = "";
  document.getElementById("newA4_score").value = "";
  document.getElementById("newA5_score").value = "";
  document.getElementById("newA6_score").value = "";
  document.getElementById("newA7_score").value = "";
  document.getElementById("newA8_score").value = "";
  document.getElementById("newA9_score").value = "";
  document.getElementById("newA10_score").value = "";
  document.getElementById("newGender_cod").value = "";
  document.getElementById("newJaundice_cod").value = "";
  document.getElementById("newAutism_cod").value = "";
  document.getElementById("newRelation_cod").value = "";

  removeElement();
}