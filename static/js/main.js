$('.myorder .menu-button').click(function () {
	$('#main .orders-detailed').removeClass("hidden");
	$('#main .menu').addClass("hidden");
	$(this).addClass("hidden");
	$('.edit-button').removeClass("hidden");
	$('.pay-button').removeClass("hidden");	
	$('.myorder ul li img').remove();
});

$('.myorder .edit-button').click(function () {
	$('#main .menu').removeClass("hidden");
	$('#main .orders-detailed').addClass("hidden");
	$(this).addClass("hidden");	
	$('.pay-button').addClass("hidden");
	$('.menu-button').removeClass("hidden");
	$('.myorder ul li').prepend('<img src="/static/img/x.svg">');
});

$('.menu button').click(function () {
	var html = '<li><img src="/static/img/x.svg"> ';
	html += $(this).html();
	html += '</li>'
	$('.myorder ul').append(html);
	updatePrice();
});

$('.myorder ul').on("click", "img", function () {
	console.log('working')
	$(this).parent().remove();
	updatePrice();
});

function updatePrice() {
	var total = 0;
	$('.myorder ul li span').each(function () {
		total += parseFloat($(this).text());
	});
	total = total.toFixed(2);
	$('.myorder .myorder-total').html('Total: ' + total)
}
