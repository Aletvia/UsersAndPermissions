
STATIC_URL = '/static/'

const title=["Título 1", "Título 2", "Título 3", "Título 4", "Título 0"]
const txt=["Este es un texto para el <b>título 1</b>. Texto texto texto texto texto texto texto texto textotexto texto texto.",
	"Este es un texto para el <b>título 2</b>. Texto texto texto texto texto texto texto texto textotexto texto texto.",
	"Este es un texto para el <b>título 3</b>. Texto texto texto texto texto texto texto texto textotexto texto texto.",
	"Este es un texto para el <b>título 4</b>. Texto texto texto texto texto texto texto texto textotexto texto texto.",
	"Este es un texto para el <b>título 0</b>. Texto texto texto texto texto texto texto texto textotexto texto texto."]

$( document ).ready(main);

function main(){
	$(window).scroll(scrollMenu);
	isMobileDevice();
}

const scrollMenu = () => {
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
const isMobileDevice = () => {
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

$('#carousel-multi').bind('slide.bs.carousel', function (e) {
	const currentIndex = $(this).find('.active').index();
	const pass=document.getElementById("pass").innerHTML;
	
	document.getElementById("ph_"+pass).src=STATIC_URL+'img/drive/b_'+pass+'.png';
	document.getElementById("ph_"+currentIndex).src=STATIC_URL+'img/drive/a_'+currentIndex+'.png';
	document.getElementById("title_desc").innerHTML=title[currentIndex];
	document.getElementById("txt_desc").innerHTML=txt[currentIndex];
	document.getElementById("pass").innerHTML=currentIndex;
	console.log('ACT: '+currentIndex+' PASS: '+pass)
});
