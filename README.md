# HackSMU-2019

## Inspiration

A combination of StateFarm's problem statement and our experiences with inconvenient, cold application systems prompted us to develop an application to streamline job applications.

## What it does

Our app implements both an applicant side and a recruiter side.

The applicant is presented with a minimalist design application portal where they are presented with a series of questions. Using WebRTC, the user records themselves answering the questions. After the applicant has finished the video questions, they are presented with a programming challenge. The programming challenge implements an in-browser IDE with syntax highlighting, a timer, and a set of test cases that must run successfully for the applicant to submit their application. Once the applicant has completed the programming challenge, they can submit their application to StateFarm.

From the recruiter end, the recruiter is presented with a list of applicants ordered by likelihood of hire. Using machine learning to detect possible hires and the time it took to complete the technical challenge, we predict whether the applicant is a good fit for StateFarm. The recruiter can click on an applicant to view their videos and solution to the technical challenge. The recruiter can add comments and rate each challenge. Once the recruiter is finished reviewing the application, they can print a report in PDF format or send an email inviting the applicant to an interview with the click of a button.

## How we built it

The front end is built on VueJS and Bulma with Ajax requests to fetch applicant data from the database. We use RecordRTC to record the user using the camera and microphone over the browser. The technical challenge syntax highlighting was built with CodeMirror. On the backend, we are using NodeJS, ExpressJS, and MongoDB. We use LaTeX to generate the application report PDF and nodemailer to send the email inviting the user to an interview.

@bintay Built the frontend, file server, PDF generator, email invitation service, and routing. @gaiscioch Built the database, applicant API, and worked on ML. @ium0002 Worked on resume scraping with python and natural language processing before having to leave early. @wdeng112 Worked on data visualization and machine learning to predict an applicants interview status.

## Challenges we ran into

One of the challenges we faced was generating PDFs from the applicant data we had stored in the database. We decided to use a LaTeX template and NodeJS's filesystem support to generate LaTeX files for each applicant then compile them to PDFs using NodeJS's exec support and PDFLaTeX.

Another challenge we had was getting video from the browser. We ended up using RecordRTC to record and write the data to a blob then send it to the server with formdata. We then processed the video on the file server and returned a url for the video, which was stored in the applicant database for easy access to the video on the recruiting view.

## Accomplishments that we're proud of

We are proud of making a coherent webapp that makes the interview process easier for both applicants and recruiters. With a system that can screen out applicants that can't solve a technical challenge while also providing videos that give a glimpse into their personality.

We are happy with our product and hope StateFarm feels the same way.

## What we learned

This was our first project using VueJS, and we learned a ton about how to use the framework. It seems like a flexible, easy to use framework that we plan on using in the future.

We also learned how to delegate different parts of large projects in order to develop more complex applications quickly. With an application of this scale, it was crucial for us to work together and communicate to define a standard interface for communication across the components and a uniform design.

## What's next

With more time, we would implement a resume scraping feature that could automatically find education and previous work experience in a resume. We were working on a system similar to this, but one of our team members had to leave early.

It would also be interesting to experiment with a larger amount of data to see the power of the time spent on the technical challenge and the video portion to predict applicant hiring.

## Built With

JavaScript, ES6, ExpressJS, NodeJS, nodemailer, VueJS, jQuery, RecordRTC, Code Mirror, Latex, Python, numpy, Pandas, Bokeh, CSS, SASS, Bulma, Font Awesome, HTML, LaTeX, MongoDB, Mongoose, RESTful APIs
