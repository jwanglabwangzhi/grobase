jQuery(function($) {
	"use strict";
	// Author Code Here
	var ratio = 2;
	// Window Load
	$(window).load(function() {
		// Header Init
		$('header').height(160);
		// Navbar Init
		$('nav').addClass('original').clone().insertAfter('nav').addClass('navbar-fixed-top').css('position', 'fixed').css('top', '0').css('margin-top', '0').removeClass('original');
	});
	// Window Scroll
	function onScroll() {
		if ($(window).scrollTop() > 50) {
			$('nav.original').css('opacity', '0');
			$('nav.navbar-fixed-top').css('opacity', '1');
		} else {
			$('nav.original').css('opacity', '1');
			$('nav.navbar-fixed-top').css('opacity', '0');
		}
	}
	window.addEventListener('scroll', onScroll, false);
});