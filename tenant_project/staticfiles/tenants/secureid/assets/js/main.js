(function($){
	"use strict";
	jQuery(document).on('ready', function () {

		// Header Sticky
		$(window).on('scroll',function() {
            if ($(this).scrollTop() > 120){  
                $('.navbar').addClass("is-sticky");
            }
            else{
                $('.navbar').removeClass("is-sticky");
            }
		});

        // Navbar Menu JS
        $('.navbar .navbar-nav li a, .scroll-down').on('click', function(e){
            var anchor = $(this);
            $('html, body').stop().animate({
                scrollTop: $(anchor.attr('href')).offset().top - 50
            }, 1500);
            e.preventDefault();
		});
		$('.navbar .navbar-nav li a').on('click', function(){
			$('.navbar-collapse').collapse('hide');
		});

		// Featured Cars Slides
		$('.featured-cars-slides').owlCarousel({
			loop: true,
			nav: true,
			dots: false,
			autoplayHoverPause: true,
            autoplay: true,
            navText: [
                "<i class='fas fa-chevron-left'></i>",
                "<i class='fas fa-chevron-right'></i>"
            ],
			responsive: {
                0: {
                    items:1,
                },
                768: {
                    items:2,
                },
                1200: {
                    items:3,
				}
            }
        });

        // Pricing Plan Active
        $('.pricing-area').on('mouseover', '.single-pricing', function() {
            $('.single-pricing.active').removeClass('active');
            $(this).addClass('active');
        });
		
		// Partner Slides
		$('.partner-slides').owlCarousel({
			loop: true,
			nav: false,
			dots: false,
			autoplayHoverPause: true,
			autoplay: true,
            navText: [
                "<i class='fas fa-angle-left'></i>",
                "<i class='fas fa-angle-right'></i>"
            ],
			responsive: {
                0: {
                    items:2,
                },
                768: {
                    items:3,
                },
                1024: {
                    items: 4,
                },
                1200: {
                    items:6,
				}
            }
		});

		// Feedback Slides
		$('.feedback-slides').owlCarousel({
			loop: true,
			nav: false,
			dots: false,
			autoplayHoverPause: true,
			autoplay: true,
            navText: [
                "<i class='fas fa-angle-left'></i>",
                "<i class='fas fa-angle-right'></i>"
            ],
			responsive: {
                0: {
                    items:1,
                },
                768: {
                    items:2,
                },
                1200: {
                    items:3,
				}
            }
        });
        
        // Services Slides
		$('.services-slides').owlCarousel({
			loop: true,
			nav: false,
			dots: true,
			autoplayHoverPause: true,
			autoplay: true,
            navText: [
                "<i class='fas fa-angle-left'></i>",
                "<i class='fas fa-angle-right'></i>"
            ],
			responsive: {
                0: {
                    items:1,
                },
                768: {
                    items:2,
                },
                1200: {
                    items:3,
				}
            }
		});

		// Testimonial Slides
		$('.testimonial-slides').owlCarousel({
			loop: true,
			nav: false,
			dots: true,
			autoplayHoverPause: true,
			autoplay: true,
            navText: [
                "<i class='icofont-rounded-left'></i>",
                "<i class='icofont-rounded-right'></i>"
            ],
			responsive: {
                0: {
                    items:1,
                },
                768: {
                    items:1,
                },
                1024: {
                    items:2,
                },
                1200: {
                    items:2,
				}
            }
		});

        // Popup Video
		$('.popup-youtube').magnificPopup({
			disableOn: 320,
			type: 'iframe',
			mainClass: 'mfp-fade',
			removalDelay: 160,
			preloader: false,
			fixedContentPos: false
        });
        
        // Count Time 
        function makeTimer() {
            var endTime = new Date("July 23, 2019 17:00:00 PDT");			
            var endTime = (Date.parse(endTime)) / 1000;
            var now = new Date();
            var now = (Date.parse(now) / 1000);
            var timeLeft = endTime - now;
            var days = Math.floor(timeLeft / 86400); 
            var hours = Math.floor((timeLeft - (days * 86400)) / 3600);
            var minutes = Math.floor((timeLeft - (days * 86400) - (hours * 3600 )) / 60);
            var seconds = Math.floor((timeLeft - (days * 86400) - (hours * 3600) - (minutes * 60)));
            if (hours < "10") { hours = "0" + hours; }
            if (minutes < "10") { minutes = "0" + minutes; }
            if (seconds < "10") { seconds = "0" + seconds; }
            $("#days").html(days + "<span>Days</span>");
            $("#hours").html(hours + "<span>Hours</span>");
            $("#minutes").html(minutes + "<span>Minutes</span>");
            $("#seconds").html(seconds + "<span>Seconds</span>");
        }
        setInterval(function() { makeTimer(); }, 1000);
		
		// Tabs
        (function ($) {
            $('.tab ul.tabs').addClass('active').find('> li:eq(0)').addClass('current');
            $('.tab ul.tabs li a').on('click', function (g) {
                var tab = $(this).closest('.tab'), 
                index = $(this).closest('li').index();
                tab.find('ul.tabs > li').removeClass('current');
                $(this).closest('li').addClass('current');
                tab.find('.tab_content').find('div.tabs_item').not('div.tabs_item:eq(' + index + ')').slideUp();
                tab.find('.tab_content').find('div.tabs_item:eq(' + index + ')').slideDown();
                g.preventDefault();
            });
		})(jQuery);
		
		// FAQ Accordion
        $(function() {
            $('.accordion').find('.accordion-title').on('click', function(){
                // Adds Active Class
                $(this).toggleClass('active');
                // Expand or Collapse This Panel
                $(this).next().slideToggle('fast');
                // Hide The Other Panels
                $('.accordion-content').not($(this).next()).slideUp('fast');
                // Removes Active Class From Other Titles
                $('.accordion-title').not($(this)).removeClass('active');		
            });
		});
		
        // Popup Image
		$('.popup-btn').magnificPopup({
            type: 'image',
            gallery: {
                enabled:true
            }
		});

		// MixItUp Shorting
		$(function(){
            $('.shorting').mixItUp();
        });
        
        // Blog Slides
		$('.blog-slides').owlCarousel({
			loop: true,
			nav: false,
			dots: true,
			autoplayHoverPause: true,
			autoplay: true,
            navText: [
                "<i class='fas fa-angle-left'></i>",
                "<i class='fas fa-angle-right'></i>"
            ],
			responsive:{
                0: {
                    items:1,
                },
                768: {
                    items:2,
                },
                1200: {
                    items:3,
				}
            }
        });

        // Subscribe form
		$(".newsletter-form").validator().on("submit", function (event) {
			if (event.isDefaultPrevented()) {
			// handle the invalid form...
				formErrorSub();
				submitMSGSub(false, "Please enter your email correctly.");
			} else {
				// everything looks good!
				event.preventDefault();
			}
		});
		function callbackFunction (resp) {
			if (resp.result === "success") {
				formSuccessSub();
			}
			else {
				formErrorSub();
			}
		}
		function formSuccessSub(){
			$(".newsletter-form")[0].reset();
			submitMSGSub(true, "Thank you for subscribing!");
			setTimeout(function() {
				$("#validator-newsletter").addClass('hide');
			}, 4000)
		}
		function formErrorSub(){
			$(".newsletter-form").addClass("animated shake");
			setTimeout(function() {
				$(".newsletter-form").removeClass("animated shake");
			}, 1000)
		}
		function submitMSGSub(valid, msg){
			if(valid){
				var msgClasses = "validation-success";
			} else {
				var msgClasses = "validation-danger";
			}
			$("#validator-newsletter").removeClass().addClass(msgClasses).text(msg);
		}
		// AJAX MailChimp
		$(".newsletter-form").ajaxChimp({
			url: "https://envytheme.us20.list-manage.com/subscribe/post?u=60e1ffe2e8a68ce1204cd39a5&amp;id=42d6d188d9", // Your url MailChimp
			callback: callbackFunction
		});

		// Particles JS
		if(document.getElementById("particles-js")) particlesJS("particles-js", {
            "particles": {
                "number": {
                    "value": 110,
                    "density": {
                        "enable": true,
                        "value_area": 1000
                    }
                },
                "color": {
                    "value": ["#aa73ff", "#f8c210", "#83d238", "#33b1f8"]
                },
                "shape": {
                    "type": "circle",
                    "stroke": {
                        "width": 0,
                        "color": "#fff"
                    },
                    "polygon": {
                        "nb_sides": 5
                    },
                    "image": {
                        "src": "img/github.svg",
                        "width": 100,
                        "height": 100
                    }
                },
                "opacity": {
                    "value": 0.6,
                    "random": false,
                    "anim": {
                        "enable": false,
                        "speed": 1,
                        "opacity_min": 0.1,
                        "sync": false
                    }
                },
                "size": {
                    "value": 2,
                    "random": true,
                    "anim": {
                        "enable": false,
                        "speed": 40,
                        "size_min": 0.1,
                        "sync": false
                    }
                },
                "line_linked": {
                    "enable": true,
                    "distance": 120,
                    "color": "#ffffff",
                    "opacity": 0.4,
                    "width": 1
                },
            },
            "interactivity": {
                "detect_on": "canvas",
                "events": {
                    "onhover": {
                        "enable": true,
                        "mode": "grab"
                    },
                    "onclick": {
                        "enable": false
                    },
                    "resize": true
                },
                "modes": {
                    "grab": {
                        "distance": 140,
                        "line_linked": {
                            "opacity": 1
                        }
                    },
                    "bubble": {
                        "distance": 400,
                        "size": 40,
                        "duration": 2,
                        "opacity": 8,
                        "speed": 3
                    },
                    "repulse": {
                        "distance": 200,
                        "duration": 0.4
                    },
                    "push": {
                        "particles_nb": 4
                    },
                    "remove": {
                        "particles_nb": 2
                    }
                }
            },
            "retina_detect": true
        });
        
        // Progress Bar
		if($('.progress-line').length){
			$('.progress-line').appear(function(){
				var el = $(this);
				var percent = el.data('width');
				$(el).css('width',percent+'%');
			},{accY: 0});
		}
		if($('.count-box').length){
			$('.count-box').appear(function(){
				var $t = $(this),
					n = $t.find(".count-text").attr("data-stop"),
					r = parseInt($t.find(".count-text").attr("data-speed"), 10);

				if (!$t.hasClass("counted")) {
					$t.addClass("counted");
					$({
						countNum: $t.find(".count-text").text()
					}).animate({
						countNum: n
					}, {
						duration: r,
						easing: "linear",
						step: function() {
							$t.find(".count-text").text(Math.floor(this.countNum));
						},
						complete: function() {
							$t.find(".count-text").text(this.countNum);
						}
					});
				}
				
			},{accY: 0});
        }

		// Go to Top
        $(function(){
            //Scroll event
            $(window).on('scroll', function(){
                var scrolled = $(window).scrollTop();
                if (scrolled > 300) $('.go-top').fadeIn('slow');
                if (scrolled < 300) $('.go-top').fadeOut('slow');
            });  
            //Click event
            $('.go-top').on('click', function() {
                $("html, body").animate({ scrollTop: "0" },  500);
            });
		});

	});

    // Odometer JS
    $('.odometer').appear(function(e) {
        var odo = $(".odometer");
        odo.each(function() {
            var countNumber = $(this).attr("data-count");
            $(this).html(countNumber);
        });
    });

	// WOW JS
	$(window).on ('load', function (){
        if ($(".wow").length) { 
            var wow = new WOW({
            boxClass: 'wow', // animated element css class (default is wow)
            animateClass: 'animated', // animation css class (default is animated)
            offset: 20, // distance to the element when triggering the animation (default is 0)
            mobile: true, // trigger animations on mobile devices (default is true)
            live: true, // act on asynchronously loaded content (default is true)
          });
          wow.init();
        }
	});
	
	// Preloader Area
	jQuery(window).on('load', function() {
	    $('.preloader').fadeOut();
	});
}(jQuery));