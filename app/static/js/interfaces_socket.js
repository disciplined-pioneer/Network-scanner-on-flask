
const socket = io.connect('http://' + location.hostname + ':' + location.port);

socket.on('update_interfaces', function(data) {
    var table = document.getElementById('interfaces-table');

    table.innerHTML = '';

    data.forEach(function(interface) {
        var newRow = table.insertRow();

        newRow.innerHTML = `
            <td>${interface.id}</td>
            <td>${interface.ip}</td>
            <td>${interface.name}</td>
            <td>${interface.type}</td>
            <td>${interface.description}</td>
            <td>${interface.status}</td>
        `;
    });
});