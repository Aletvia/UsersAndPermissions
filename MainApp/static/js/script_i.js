
STATIC_URL = '/static/'

$( document ).ready(main);

function main(){
	$(window).scroll(scrollMenu);
	isMobileDevice();
}

function scrollMenu(){
	var secciones = $("#change").offset().top;

	if($(this).scrollTop() < secciones-100){
		if( navigator.userAgent.match(/Android/i)
		|| navigator.userAgent.match(/webOS/i)
		|| navigator.userAgent.match(/iPhone/i)
		|| navigator.userAgent.match(/iPad/i)
		|| navigator.userAgent.match(/iPod/i)
		|| navigator.userAgent.match(/BlackBerry/i)
		|| navigator.userAgent.match(/Windows Phone/i))
		{
			$("#body nav").eq(0).addClass("color1");
		}else{
			$("#body nav").eq(0).addClass("color");
		}
	}
	else{
		$("#body nav").eq(0).removeClass("color");
		$("#body nav").eq(0).removeClass("color1");
	}
}
function isMobileDevice() {
	var element = document.getElementById("img_banner1");
	if( navigator.userAgent.match(/Android/i)
	|| navigator.userAgent.match(/webOS/i)
	|| navigator.userAgent.match(/iPhone/i)
	|| navigator.userAgent.match(/iPod/i)
	|| navigator.userAgent.match(/BlackBerry/i)
	|| navigator.userAgent.match(/Windows Phone/i))
	{
		element.classList.remove("img_phone");
		element.classList.add("height_0");
		$("#body nav").eq(0).addClass("color1");
	}else{
		$("#body nav").eq(0).addClass("color");
	}
};

function select_(n){
	document.getElementById("act").innerHTML=parseInt(n) - parseInt(1);
	document.getElementById("i"+n).click();
	document.getElementById("txt"+n).click();
}

$('#carousel-multi').bind('slide.bs.carousel', function (e) {
	console.log('Hola')
	act=document.getElementById("act").innerHTML;
	pass=document.getElementById("pass").innerHTML;
	if(pass!=0){
		document.getElementById("ph_"+pass).src=STATIC_URL+'img/drive/b_'+pass+'.png';
	}
	if(act<5){
		n= parseInt(act) + parseInt(1);
	}else{
		n = 1;
	}
	document.getElementById("pass").innerHTML=n;
	document.getElementById("act").innerHTML=n;
	document.getElementById("ph_"+n).src=STATIC_URL+'img/drive/a_'+n+'.png';
});
