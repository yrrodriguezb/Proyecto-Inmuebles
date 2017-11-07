$(document).ready(function(){

  var btnMenu = $("#btn-menu")
  var menu = $(".navegacion .menu");
  var navegacion = $(".navegacion");
  var itemmenu = $(".navegacion .menu > .item-submenu a");
  var goback = $(".navegacion .submenu li.go-back");
  var submenu = $(".navegacion .submenu");

  btnMenu.on("click", function(){
    var self = $(this);

    if (self.attr("class") == "fa fa-bars"){
        self.removeClass("fa fa-bars").addClass("fa fa-close");
        menu.animate({"left": "0"});
        navegacion.css({"width": "100%", "background": "rgba(0, 0, 0, .3)"});
    }
    else {
      self.removeClass("fa fa-close").addClass("fa fa-bars");
      submenu.animate({"left": "-320px"});
      menu.animate({"left": "-320px"});
      navegacion.css({"width": "0%", "background": "rgba(0, 0, 0, .0)"});
    }
  });

  itemmenu.on("click", function(){
    var self = $(this);
    var posicionMenu = self.parent().attr("menu");

    $(".item-submenu[menu='" + posicionMenu +"'] .submenu").animate({"left": "0"});
  });

  goback.on("click", function(){
    var self = $(this);

    self.parent().animate({"left": "-320px"});
  })

});
