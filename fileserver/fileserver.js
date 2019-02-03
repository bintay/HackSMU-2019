// Includes
const path = require('path');

// Set up express
const express = require('express');
const app = express();
const port = process.argv[2] || 12345;

app.use('/public', express.static('public'));

var multer  = require('multer');
var upload = multer({ dest: __dirname + '/public/uploads/' });
var type = upload.single('data');
var exec = require('child_process').exec;
var fs = require('fs');

app.post('/video/', type, function (req, res) {
   res.setHeader("Access-Control-Allow-Origin", "*");
   res.end(JSON.stringify({'success': true, filename: req.file.filename}));
});

app.listen(port, function () {
   console.log(`Listening on port ${port}`);
});
