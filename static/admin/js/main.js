var Site = {}
Site.registration = function(form, type) {
  switch (type) {
    case "np":
      $.ajax({
        url: "/api/registration/new_person/",
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
          toastr["error"](error.responseJSON.error)
        }
      });
    break;
