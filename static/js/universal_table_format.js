document.addEventListener('DOMContentLoaded', (event) => {
    formatTables();
});

function formatTables() {
    const tables = document.querySelectorAll('table');
    tables.forEach(table => {
        sortTableByDate(table);
        formatNumberColumns(table);
        formatDatetimeColumns(table); // New function call
    });
}

function sortTableByDate(table) {
    const rows = Array.from(table.querySelectorAll('tr')).slice(1); // Exclude header row
    rows.sort((a, b) => {
        const aTimestamp = a.querySelector('td[data-type="datetime"]').dataset.timestamp;
        const bTimestamp = b.querySelector('td[data-type="datetime"]').dataset.timestamp;
        return bTimestamp - aTimestamp; // Sort in descending order
    });
    rows.forEach(row => table.appendChild(row)); // Re-append rows in sorted order
}

function formatNumberColumns(table) {
    const numberCells = table.querySelectorAll('td[data-type="number"]');
    numberCells.forEach(cell => {
        const number = parseFloat(cell.textContent);
        if (!isNaN(number)) {
            cell.textContent = number.toFixed(2); // Format to two decimals
        }
    });
}

function formatDatetimeColumns(table) {
    const datetimeCells = table.querySelectorAll('td[data-type="datetime"]');
    datetimeCells.forEach(cell => {
        const timestamp = cell.dataset.timestamp;
        if (timestamp) {
            const date = new Date(timestamp * 1000); // Convert Unix timestamp to milliseconds
            cell.textContent = date.toLocaleString(); // Convert to local datetime string
        }
    });
}