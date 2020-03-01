var express = require('express');
var router = express.Router();

router.get('/', function(req, res) {
    res.render('main', {
        page:'Main',
        menuId: 'main'
    });
});

router.get('/login', function(req, res) {
    res.render('login', {
        page:'Login',
        menuId: 'login'
    });
});

router.get('/signup', function(req, res) {
    res.render('signup', {
        page:'Signup',
        menuId: 'signup'
    });
});

router.get('/loginSignUp', function(req, res) {
    res.render('loginSignUp', {
        page:'LoginSignUp',
        menuId: 'loginSignUp'
    });
});

router.get('/datapage', function(req, res) {
    res.render('datapage', {
        page:'Datapage',
        menuId: 'datapage'
    });
});


module.exports = router;