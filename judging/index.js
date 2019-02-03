const fs = require('fs');
const uuid = require('uuid/v1');
const exec = require('child_process').exec;

const path = require('path');
const express = require('express');
const app = express();
const port = 3001;
const email = require('nodemailer');

const bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.use('/public', express.static('public'));

app.get('/', function (req, res) {
   res.sendFile(path.join(__dirname + '/frontend/index.html'));
});

app.post('/pdf', function (req, res) {
   let filename = uuid();
   fs.readFile('latex/template.tex', (err, data) => {
      if (err) console.log(err);
      data = data.toString().replace('{NAME}', req.body.applicant.name)
                 .replace('{ADDRESS}', req.body.applicant.address)
                 .replace('{CITY}', req.body.applicant.city)
                 .replace('{STATE}', req.body.applicant.state)
                 .replace('{COUNTRY}', req.body.applicant.country)
                 .replace('{ZIP}', req.body.applicant.zip)
                 .replace('{PHONE}', req.body.applicant.phone)
                 .replace('{EMAIL}', req.body.applicant.email)
                 .replace('{COMMENT1}', req.body.applicant.video_comments1)
                 .replace('{COMMENT2}', req.body.applicant.video_comments2)
                 .replace('{COMMENT3}', req.body.applicant.video_comments3)
                 .replace('{RATING1}', req.body.applicant.video_rating1)
                 .replace('{RATING2}', req.body.applicant.video_rating2)
                 .replace('{RATING3}', req.body.applicant.video_rating3)
                 .replace('{COMMENT4}', req.body.applicant.code_comments)
                 .replace('{RATING4}', req.body.applicant.code_rating)
                 .replace('{TIME}', req.body.applicant.code_time)
                 .replace('{FLAGGED}', req.body.applicant.flagged ? 'Yes' : 'No')
      console.log('read');
      fs.writeFile(`public/pdf/${filename}.tex`, data, function (err) {
         if (err) console.log(err);
         console.log('write');
         exec(`pdflatex ` + path.join(__dirname + `/public/pdf/${filename}.tex`), function (err, stdout, stderr) {
            if (err) console.log(err);
            console.log('compile');
            fs.rename(`${filename}.pdf`, `public/pdf/${filename}.pdf`, function (err) {
               if (err) console.log(err);
               console.log('rename');
               res.end(JSON.stringify({'file': `/public/pdf/${filename}.pdf`}));
               exec(`rm ${path.join(__dirname, '/*.aux')} ${path.join(__dirname, '/*.log')}`, function (err, stdout, stderr) {
                  console.log('cleaned up');
               });
            }); 
         });
      });
   });
});

// steal my info please <3
const transporter = email.createTransport({
  service: 'gmail',
  auth: {
    user: 'state.farm.dev.recruiting@gmail.com',
    pass: 'State' + '.' + 'Farm' + (1 + 3) + '9'
  }
});

app.post('/invite', function (req, res) {
   const mailOptions = {
      from: 'state.farm.dev.recruiting@gmail.com',
      to: req.body.applicant.email,
      subject: 'On-site Interview Invitation',
      text:
`Hi ${req.body.applicant.name.split(' ')[0]},

We were impressed by your application to StateFarm! We are offering you the opportunity to interview on-site, fully paid for. Let us know when you're available!

Looking forward to meeting you in person,

Chris Zhang
StateFarm Developer Recruiting
state.farm.dev.recruiting@gmail.com
+1 (555) 123-4567`
   }

   transporter.sendMail(mailOptions, function (err, info) {
      if (err) console.log(err);
      console.log('Sent email');
      res.end(JSON.stringify({'sent': true}));
   });
});

app.listen(port, function () {
   console.log(`Listening on port ${port}`);
});
