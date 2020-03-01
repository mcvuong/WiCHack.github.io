var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var session = require('express-session');
const axios = require('axios');
var bodyParser = require('body-parser'); 
const auth = require('./auth');
require('dotenv').config();
var WEGMANS_KEY = process.env.WEGMANS_KEY;


var app = express();

app.use(session({
	secret: 'secret',
	resave: true,
	saveUninitialized: true
}));


app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(bodyParser.json());


// view engine setup
app.set('views', path.join(__dirname, '/views'));
app.set('view engine', 'ejs');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());

app.use(express.static(__dirname + '/public'));

app.get('/', function(request, response) {
    response.render('main');
});

app.get('/test', function(request, response) {
    async function getUser() {
        try {
          const response = await axios.get('https://api.wegmans.io/products/categories', {
            params: {
                'api-version': '2018-10-18',
                'Subscription-Key': WEGMANS_KEY
            }
          }); 
          console.log(response.data);
        } catch (error) {
          console.error(error);
        }
      }
      getUser();
});


app.get('/loginSignUp', function(request, response) {
    response.render('loginSignUp');
});

app.get('/datapage', function(request, response) {
  response.render('datapage');
});


app.post('/signup', function(request, response) {
  response.render('datapage');
});

//Authenticates login
app.post('/login', function(request, response) {
  response.render('datapage');
});

//Authenticates signup
app.post('/auth', function(request, response) {
  response.render('datapage');
});

module.exports = app;