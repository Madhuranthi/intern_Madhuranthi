
fetch("http://127.0.0.1:5000/user")
.then(response => response.json())
.then(data => {

    let table = document.getElementById("tableBody");

    data.forEach(emp => {

        table.innerHTML += `
        <tr>
            <td>${emp.id}</td>
            <td>${emp.name}</td>
            <td>${emp.email_id}</td>
        </tr>
        `;

    });

});