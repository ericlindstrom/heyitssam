/* Author:
Eric Lindstrom
*/

//$('body,html').animate({scrollTop: 0}, 800);
$(function() {
    $('header nav ul li ul li a').click(function() {
	//check against IE/FF
	link = $(this).attr('href');
	$('body,html').animate({scrollTop: $(link).offset().top-40}, 800);
	return false;
    });
});
