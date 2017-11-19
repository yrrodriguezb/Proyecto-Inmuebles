$(document).on("ready", function () {
  pagina.load();
});

var pagina = {
  controles: {
    btnIniciarSesion: null,
    btnmenu: null,
    goback: null,
    itemmenu: null,
    lnkIniciarSesion: null,
    masterpage_modal: null,
    menu: null,
    navegacion: null,
    submenu: null
  },
  fn: {
    referenciarControles: function () {
      pagina.controles.btnIniciarSesion = $("[id=masterpage_btnIniciarSesion]");
      pagina.controles.btnmenu = $("#btn-menu"),
      pagina.controles.goback = $(".navegacion .submenu li.go-back");
      pagina.controles.itemmenu = $(".navegacion .menu > .item-submenu a");
      pagina.controles.lnkIniciarSesion = $("[id=lnkIniciarSesion]");
      pagina.controles.masterpage_modal = $("[id=dvModalIniciarSesion]");
      pagina.controles.menu = $(".navegacion .menu");
      pagina.controles.navegacion = $(".navegacion");
      pagina.controles.submenu = $(".navegacion .submenu");
    },
    referenciarEventos: function () {
      //pagina.controles.btnIniciarSesion.on("click", validarUsuario);
      pagina.controles.btnmenu.on("click", vermenu);
      pagina.controles.itemmenu.on("click", versubmenu);
      pagina.controles.goback.on("click", regresarmenu);
      pagina.controles.masterpage_modal.modal();
    },
    serviciohttp: function (jsonConfig) {
      consultaAJAX(jsonConfig);
    }
  },
  load: function () {
    pagina.fn.referenciarControles();
    pagina.fn.referenciarEventos();
  },
  servicios: {
    wsUsuarioLogin: "/usuario/login"
  }
};

var validarUsuario = (function () {
  var csrftoken = getCookie('csrftoken');

  var configAjax = {
    ws: pagina.servicios.wsUsuarioLogin,
    params: {
      username: $("[id=masterpage_username]").val(),
      password: $("[id=masterpage_password]").val(),
      csrfmiddlewaretoken: csrftoken//$("input[type=hidden][name=csrfmiddlewaretoken]").val()
    },
    fn: {
      Error: httpResquestError,
      Ok: getUsuario
    }
  };

  pagina.controles.fn.serviciohttp(configAjax);
});



var consultaAJAX = (function (obj) {
  var config = {
    url: location.origin + obj.ws,
    type: "POST",
    contentType: "application/json, charset=uft-8",
    dataType: "json",
    data: JSON.stringify(obj.params),
    error: obj.fn.Error,
    success: obj.fn.Ok
  };

  $.ajax(config);
});

var httpResquestError = (function (jqXHR, textStatus, errorThrown) {
  console.error(jqXHR);
  console.error(textStatus);
  console.error(errorThrown);
});

var getCookie = (function (name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
        var cookie = $.trim(cookies[i]);
  // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) == (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
    }
  }
 return cookieValue;
});

var getUsuario = (function (data) {
  console.log(data);
});

var vermenu = (function () {
  var self = $(this);

  if (self.attr("class") == "fa fa-bars"){
      self.removeClass("fa fa-bars").addClass("fa fa-close");
      pagina.controles.menu.animate({"left": "0"});
      pagina.controles.navegacion.css({"width": "100%", "background": "rgba(0, 0, 0, .3)"});
  }
  else {
    self.removeClass("fa fa-close").addClass("fa fa-bars");
    pagina.controles.submenu.animate({"left": "-320px"});
    pagina.controles.menu.animate({"left": "-320px"});
    pagina.controles.navegacion.css({"width": "0%", "background": "rgba(0, 0, 0, .0)"});
  }
});

var versubmenu = (function () {
  var self = $(this);
  var posicionMenu = self.parent().attr("menu");

  $(".item-submenu[menu='" + posicionMenu +"'] .submenu").animate({"left": "0"});
});

var regresarmenu = (function () {
  var self = $(this);

  self.parent().animate({"left": "-320px"});
});
