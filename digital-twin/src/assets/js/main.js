
//-----------------Slide In desde la Arriba Bajo----------------
$(document).ready(function(){
    // Slide in elements on scroll
    $(window).scroll(function() {
        $(".slideanim").each(function(){
            var pos = $(this).offset().top;

            var winTop = $(window).scrollTop();
            if (pos < winTop + 600) {
                $(this).addClass("slide");
            }
        });
    });
})
//-----------------Slide In desde la Arriba Bajo----------------
$(document).ready(function() {
    $(window).scroll(function() {
        $(".RevealLeft").each(function() {
            var pos = $(this).offset().top;
            var winTop = $(window).scrollTop();
            if (pos < winTop + 700) {
                $(this).addClass("revealLeft");
            }
        });
    });
});