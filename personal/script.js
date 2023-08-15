// Initialize the map
var map = L.map('map').setView([0, 0], 2); // Center the map at (latitude: 0, longitude: 0) with zoom level 2

// Add a tile layer (OpenStreetMap)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Add markers or other map features as needed
