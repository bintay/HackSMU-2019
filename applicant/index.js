const path = require('path');
const express = require('express');
const app = express();
const port = process.argv[2] || 3000;

app.use('/public', express.static('public'));

app.get('/', function (req, res) {
   res.sendFile(path.join(__dirname, 'frontend/index.html'));
});

app.listen(port, function () {
   console.log(`Listening on port ${port}`);
});
