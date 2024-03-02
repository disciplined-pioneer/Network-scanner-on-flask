const max_rows = 30

const socket = io.connect('http://' + location.hostname + ':' + location.port);

socket.on('update_metrics', function(data) {
    const table = document.getElementById('metrics-table');
    const newRow = table.insertRow(0);

    newRow.innerHTML = `
        <td>${data.timestamp}</td>
        <td>${data.cpu_usage}</td>
        <td>${data.memory_usage}</td>
        <td>${data.network_sent}</td>
        <td>${data.network_recv}</td>
    `;
});

