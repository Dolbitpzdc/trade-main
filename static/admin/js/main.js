var Site = {}

Site.getCookie = function(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

Site.registration = function(form, type) {
      $.ajax({
        url: "/api/regNew/",
        method: "POST",
        data: {
          csrfmiddlewaretoken: Site.getCookie('csrftoken'),
          data: $(form).serialize(),
        },
        success: function(response) {
          console.log(response)
          location.href = "/admin"
        },
        error: function(error) {
          console.log("ERROR TEST")
        }
      });

}

Site.log_inAdmin = function(form){
  $.ajax({
    url: "/api/log_inAdmin/",
    method: "POST",
    data: {
      csrfmiddlewaretoken: Site.getCookie('csrftoken'),
      email: form["email"].value,
      password: form["password"].value,
    },
    success: function(response) {
      console.log(response)
      location.href = "/admin/"
    },
    error: function(error) {
      console.log("ERROR TEST")
    }
  });
}
