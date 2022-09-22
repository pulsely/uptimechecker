import Vue from 'vue'

////import Datetime from 'vue-datetime'
// You need a specific loader for CSS files
////import 'vue-datetime/dist/vue-datetime.css'

////import { Settings } from 'luxon'

//Settings.defaultLocale = 'fr'
////window.LuxonSettings = Settings;

////Vue.use(Datetime)


// import VueCtkDateTimePicker from 'vue-ctk-date-time-picker';
// import 'vue-ctk-date-time-picker/dist/vue-ctk-date-time-picker.css';

//window.VueCtkDateTimePicker = VueCtkDateTimePicker;

//Vue.component('VueCtkDateTimePicker', VueCtkDateTimePicker);



/*
Vue.component('message', {
template: '<p> Hey there, I am a re-usable component </p>'
});
*/

Vue.mixin({
    delimiters: ['[[', ']]']
});



// Add filter
import moment from "moment";

Vue.filter('formatDate', function (value) {
    if (value) {
        return moment(String(value)).format('YYYY-MM-DD HH:mm:ss')
    }
});

Vue.filter('unixtimeformat', function (value) {
    if (value) {
        return moment.unix(String(value)).format('YYYY-MM-DD HH:mm:ss');
    }
});

Vue.filter('unixtimeago', function (value) {
    if (value) {
        return moment.unix(String(value)).fromNow();
    }
});



window.Vue = Vue;
//window.Vue.component('vue-ctk-date-time-picker', VueCtkDateTimePicker);

// import owl
import 'owl.carousel/dist/assets/owl.carousel.css';
import 'owl.carousel/dist/assets/owl.theme.default.css';
import 'owl.carousel';


// import 'bootstrap-offcanvas/offcanvas.css';
// import 'bootstrap-offcanvas/offcanvas.js';

// Make jquery global
// (function (global) {
//     // $ and jQuery are function here...
//     global.$ = $;
//     global.jQuery = jQuery;
// }(typeof window !== 'undefined' ? window : this));


import axios from 'axios';

window.axios = axios;

// AOS

// import AOS from 'aos';
// import 'aos/dist/aos.css'; // You can also use <link> for styles
// AOS.init({once: true});

// ES6 Modules or TypeScript
import Swal from 'sweetalert2'

window.Swal = Swal;


import {Settings} from 'luxon'

//Settings.defaultLocale = 'fr'
window.LuxonSettings = Settings;
import {DateTime as LuxonDateTime} from 'luxon'

window.LuxonDateTime = LuxonDateTime;


// CommonJS
//onst Swal = require('sweetalert2')

// Font awesome
// import '@fortawesome/fontawesome-free/css/all.css'
// import '@fortawesome/fontawesome-free/js/all.js'

//or, as of 2.0, all tools are exported from the "all" file (excluding bonus plugins):
//typical import
////import {TweenMax, Power2, TimelineLite} from "gsap/TweenMax";
////window.TweenMax = TweenMax;


// import $ from 'jquery';
////import datepickerFactory from 'jquery-datepicker';
////import datepickerCNFactory from 'jquery-datepicker/i18n/jquery.ui.datepicker-zh-CN';

////datepickerFactory($);
////datepickerCNFactory($);

////import { DateTime as LuxonDateTime } from 'luxon'
////window.LuxonDateTime = LuxonDateTime;

//var bootstrap = require('bootstrap');
//require('bootstrap/dist/css/bootstrap.css');





// import 'bootstrap';
// import 'bootstrap/dist/css/bootstrap.min.css';

// import 'bootstrap-offcanvas/offcanvas';
// import 'bootstrap-offcanvas/offcanvas.css';


// And their styles (for UI plugins)
// require('@uppy/core/dist/style.css')
// require('@uppy/dashboard/dist/style.css')



// Import the plugins
// const Uppy = require('@uppy/core')
// const XHRUpload = require('@uppy/xhr-upload')
// const Dashboard = require('@uppy/dashboard')

// And their styles (for UI plugins)
// require('@uppy/core/dist/style.css')
// require('@uppy/dashboard/dist/style.css')
//
// window.Uppy = Uppy;
// window.XHRUpload = XHRUpload;
// window.Dashboard = Dashboard;
//

/*
const uppy = Uppy()
  .use(Dashboard, {
    trigger: '#select-files'
  })
  .use(XHRUpload, { endpoint: 'https://api2.transloadit.com' })

uppy.on('complete', (result) => {
  console.log('Upload complete! We’ve uploaded these files:', result.successful)
})
 */

// "use strict";
// +function (a, b) {
//     var c = {name: "django", version: "2.0"};
//     c.defaults = {googleApiKey: null, googleAnalyticsId: null, smoothScroll: !0}, c.breakpoint = {
//         xs: 576,
//         sm: 768,
//         md: 992,
//         lg: 1200
//     }, c.config = function (d) {
//         if ("string" == typeof d) return c.defaults[d];
//         a.extend(!0, c.defaults, d), c.defaults.smoothScroll || SmoothScroll.destroy(), a('[data-provide~="map"]').length && void 0 === b["google.maps.Map"] && a.getScript("https://maps.googleapis.com/maps/api/js?key=" + c.defaults.googleApiKey + "&callback=thesaas.map"), c.defaults.googleAnalyticsId && (!function (a, b, c, d, e, f, g) {
//             a.GoogleAnalyticsObject = e, a[e] = a[e] || function () {
//                 (a[e].q = a[e].q || []).push(arguments)
//             }, a[e].l = 1 * new Date, f = b.createElement(c), g = b.getElementsByTagName(c)[0], f.async = 1, f.src = "https://www.google-analytics.com/analytics.js", g.parentNode.insertBefore(f, g)
//         }(b, document, "script", 0, "ga"), ga("create", c.defaults.googleAnalyticsId, "auto"), ga("send", "pageview"))
//     }, c.init = function () {
//         c.topbar();
//         c.scrolling();
//     }, c.scrolling = function () {
//         var b = a("html, body");
//         a(document).on("click", ".scroll-top", function () {
//             return b.animate({scrollTop: 0}, 600), a(this).blur(), !1
//         }), a(document).on("click", "[data-scrollto]", function () {
//             var c = "#" + a(this).data("scrollto");
//             if (a(c).length > 0) {
//                 var d = 0;
//                 a(".topbar.topbar-sticky").length && (d = 60), b.animate({scrollTop: a(c).offset().top - d}, 1e3)
//             }
//             return !1
//         });
//         var c = location.hash.replace("#", "");
//         "" != c && a("#" + c).length > 0 && b.animate({scrollTop: a("#" + c).offset().top - 60}, 1e3)
//     }, c.topbar = function () {
//         var c = a("body");
//         a(b).on("scroll", function () {
//             if (a(document).scrollTop() > 10) {
//                 c.addClass("body-scrolled");
//
//
//                 // $('#navbar-primary').removeClass("navbar-dark");
//                 // $('#navbar-primary').addClass("navbar-light");
//                 $('#navbar-transparent-header').addClass("navbar-transparent-black");
//
//             } else {
//                 c.removeClass("body-scrolled");
//
//                 // $('#navbar-primary').removeClass("navbar-light");
//                 // $('#navbar-primary').addClass("navbar-dark");
//                 $('#navbar-transparent-header').removeClass("navbar-transparent-black");
//
//             }
//         })
//     }, b.m = c
// }(jQuery, window), $(function () {
//     /*    if (window.location.pathname.indexOf('') < 0) return false; */
//     m.init()
// });
//
//


//window.VueCtkDateTimePicker = VueCtkDateTimePicker;


//var moment = require('moment');
window.moment = moment;
