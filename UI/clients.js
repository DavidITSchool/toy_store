console.log('Loaded clients.js')

async function showAllClients() {
	const request = new Request('http://localhost:5000/get_all_clients');
	fetch(request)
		.then(response => response.json())
		.then(clients => {
			client_list = clients['clients'];
			let content = ''
			for(let client of client_list){
			    console.log(client.cnp);
			    content += "<div class='card card_container'> <b><p>" +
			     client.cnp + "</p></b> <b><p>" +
			     client.first_name + "</p></b> <b><p>" +
			     client.last_name + "</p></b> <b><p>" +
			     client.email + "</p></b> <b><p>" +
			     client.age_group + "</p></b> <b><p>" +
			     "</p></b> </div>"
			}

			document.getElementById('main').innerHTML = content;

		}).catch(error => console.warn(error));
}


async function showOneClient() {
    content = '<input id="client_cnp_input" type="text"></input> <button type="button" class="btn btn-primary" onclick="loadClientByCnp()"> Get client by cnp </button> <br> <div id="one_client_div"></div>'
    document.getElementById('main').innerHTML = content
}

async function loadClientByCnp() {
    let cnp = document.getElementById('client_cnp_input').value
	const request = new Request('http://localhost:5000/get_client/' + cnp);
	console.log(request.url)
	fetch(request)
		.then(response => response.json())
		.then(client_data => {
			console.log(client_data);
			client = client_data['client'];
			console.log(client);
			content = '';
			content += "<div class='card card_container'> <b><p>" +
			     client.cnp + "</p></b> <b><p>" +
			     client.first_name + "</p></b> <b><p>" +
			     client.last_name + "</p></b> <b><p>" +
			     client.email + "</p></b> <b><p>" +
			     client.age_group + "</p></b> <b><p>" +
			     "</p></b> </div>"

			document.getElementById('one_client_div').innerHTML = content
		}).catch(error => console.warn(error));
}


async function showAddClient() {
    content =
        '<label>Client CNP:</label>' +
        '<input id="client_cnp_input" type="text"></input>' +
        '<br>' +
        '<label>Client First Name:</label>' +
        '<input id="client_first_name_input" type="text"></input>' +
        '<br>' +
        '<label>Client Last Name:</label>' +
        '<input id="client_last_name_input" type="text"></input>' +
        '<br>' +
        '<label>Client Email:</label>' +
        '<input id="client_email_input" type="text"></input>' +
        '<br>' +
        '<button type="button" class="btn btn-primary" onclick="addClient()">Add client</button>'
    document.getElementById('main').innerHTML = content
}

async function addClient() {
    let cnp = document.getElementById('client_cnp_input').value
    let first_name = document.getElementById('client_first_name_input').value
    let last_name = document.getElementById('client_last_name_input').value
    let email = document.getElementById('client_email_input').value

    let client_data = {
        'cnp': cnp,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        }

    $.ajax({
      type: "POST",
      contentType: "application/json; charset=utf-8",
      url: "http://localhost:5000/add_client",
      data: JSON.stringify(client_data),
      success: function () {
        alert('Client added successfully');
      },
      dataType: "json"
    });
}

async function showRemoveClient() {
    content =
        '<label>Client CNP to remove:</label> ' +
        '<input id="client_cnp_input" type="text"></input>' +
        '<br>' +
        '<button type="button" class="btn btn-primary" onclick="removeClient()">Remove client</button>'
    document.getElementById('main').innerHTML = content
}

async function removeClient() {
    let cnp = document.getElementById('client_cnp_input').value

    let client_cnp = {
        'cnp': cnp
        }

    $.ajax({
      type: "POST",
      contentType: "application/json; charset=utf-8",
      url: "http://localhost:5000/remove_client",
      data: JSON.stringify(client_cnp),
      success: function () {
        alert('Client removed successfully');
      },
      dataType: "json"
    });
}

async function showUpdateClient() {
    content =
        '<label>Client CNP:</label>' +
        '<input id="client_cnp_input" type="text"></input>' +
        '<br>' +
        '<label>Client First Name to be changed:</label>' +
        '<input id="client_first_name_input" type="text"></input>' +
        '<br>' +
        '<label>Client Last Name to be changed:</label>' +
        '<input id="client_last_name_input" type="text"></input>' +
        '<br>' +
        '<label>Client Email to be changed:</label>' +
        '<input id="client_email_input" type="text"></input>' +
        '<br>' +
        '<button type="button" class="btn btn-primary" onclick="updateClient()">Update client</button>'
    document.getElementById('main').innerHTML = content
}

async function updateClient() {
    let cnp = document.getElementById('client_cnp_input').value
    let first_name = document.getElementById('client_first_name_input').value
    let last_name = document.getElementById('client_last_name_input').value
    let email = document.getElementById('client_email_input').value

    let client_data = {
        'cnp': cnp,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        }

    $.ajax({
      type: "POST",
      contentType: "application/json; charset=utf-8",
      url: "http://localhost:5000/update_client",
      data: JSON.stringify(client_data),
      success: function () {
        alert('Client updated successfully');
      },
      dataType: "json"
    });
}