var dropdownElementList = [].slice.call(document.querySelectorAll('.dropdown-toggle'))
var dropdownList = dropdownElementList.map(function(dropdownToggleEl) {
  return new bootstrap.Dropdown(dropdownToggleEl)
})

var exampleModal = document.getElementById('exampleModal')
exampleModal.addEventListener('show.bs.modal', function(event) {

  var button = event.relatedTarget

  var recipient = button.getAttribute('data-bs-whatever')

  var modalTitle = exampleModal.querySelector('.modal-title')
  var modalBodyInput = exampleModal.querySelector('.modal-body input')

  modalTitle.textContent = 'New message to ' + recipient
  modalBodyInput.value = recipient
})

$(document).ready(function() {

  $(".sidebar").mCustomScrollbar({
    theme: "minimal"
  });

  $('.sidebarCollapse').on('click', function(e) {
    let $sidebar = $('#sidebar');
    $sidebar.toggleClass('active');

    if (!$sidebar.hasClass('active')) {
      $('#sidebar-2, #sidebar-2 ul').removeClass('active');
    }

    $('.overlay').toggleClass('active');
  });

  $('.sidebar .close').on('click', function(e) {
    let $sidebar = $(this).closest('.sidebar');
    $sidebar.removeClass('active');
    $('#sidebar-2 ul').removeClass('active');

    if ($sidebar.attr('id') === 'sidebar') {
      $('.overlay').toggleClass('active');
      $('#sidebar-2').removeClass('active');
    }
  });

  $('.overlay').on('click', function(e) {
    let $sidebar = $(this).closest('.sidebar');
    $sidebar.removeClass('active');
    $('#sidebar-2 ul').removeClass('active');

      $('.overlay').toggleClass('active');
      $('#sidebar').removeClass('active');
      $('#sidebar-2').removeClass('active');
  });

  $(document).keyup(function(e) {
     if (e.key === "Escape") { // escape key maps to keycode `27`
       let $sidebar = $(this).closest('.sidebar');
       $sidebar.removeClass('active');
       $('#sidebar-2 ul').removeClass('active');

         $('.overlay').toggleClass('active');
         $('#sidebar').removeClass('active');
         $('#sidebar-2').removeClass('active');
    }
});

  $('#sidebar li a').on('click', function(e) {

    // убираем все активные сабменю
    $('#sidebar-2 ul').removeClass('active');

    let $this = $(this);

    // получаем сабменю
    let $category = $($this.attr('href'));

    // если существует, показываем
    if ($category.length) {
      e.preventDefault();
      $('#sidebar-2 h4').text($this.text());
      $('#sidebar-2').addClass('active');
      $category.toggleClass('active');
    }
    // если  нет, прячем сабменю и ничего не делаем
    else {
      $('#sidebar-2').removeClass('active');
    }

  });

});


var Site = {};

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

Site.log_in = function(form) {
  // console.log(form.elements["email"].value)
  // console.log(form.elements["password"].value)
  // console.log(form.elements["remember_me"].checked)

  $.ajax({
    url: "/api/log_in/",
    method: "POST",
    data: {
      csrfmiddlewaretoken: Site.getCookie('csrftoken'),
      email: form.elements["email"].value,
      password: form.elements["password"].value,
      remember_me: form.elements["remember_me"].checked
    },
    success: function(response) {
      if (response) {
        if (response.code == 200) {
          toastr["success"]("Успешная авторизация!")
          location.href = "/home"
        }
      }
      console.log(response)
    },
    error: function(error) {
      toastr["error"](error.responseJSON.error)
    }
  });

}

Site.newReview = function(form) {
  $.ajax({
    url: "/api/NewReview/",
    method: "POST",
    data: {
      csrfmiddlewaretoken: Site.getCookie('csrftoken'),
      data: $(form).serialize(),
    },
    success: function(response) {
      toastr["success"](response.response)
    },
    error: function(error) {
      toastr["error"](error.responseJSON.error)
    }

  });
}

Site.PymentDetail = function(form) {
  $.ajax({
    url: "/api/PymentDetail/",
    method: "POST",
    data: {
      csrfmiddlewaretoken: Site.getCookie('csrftoken'),
      data: $(form).serialize(),
    },
    success: function(response) {
      toastr["success"](response.response)
    },
    error: function(error) {
      toastr["error"](error.responseJSON.error)
    }

  });
}

Site.registration = function(form, type) {

  // if (!Site.formValidation(form)) {
  //   toastr["error"]("Заполните все поля, это привлечёт больше клиентов.")
  //   return false;
  // }

  switch (type) {
    case "lbi":
      $.ajax({
        url: "/api/registration/buyer_individ/",
        method: "POST",
        data: {
          csrfmiddlewaretoken: Site.getCookie('csrftoken'),
          data: $(form).serialize(),
        },
        success: function(response) {
          console.log(response)
          location.href = "/home"
        },
        error: function(error) {
          toastr["error"](error.responseJSON.error)
        }

      });
    break;

    case "lbe":
      $.ajax({
        url: "/api/registration/buyer_entity/",
        method: "POST",
        data: {
          csrfmiddlewaretoken: Site.getCookie('csrftoken'),
          data: $(form).serialize(),
        },
        success: function(response) {
          console.log(response)
          location.href = "/home"
        },
        error: function(error) {
          toastr["error"](error.responseJSON.error)
        }
      });
    break;

    case "lpi":
      $.ajax({
        url: "/api/registration/provider_individ/",
        method: "POST",
        data: {
          csrfmiddlewaretoken: Site.getCookie('csrftoken'),
          data: $(form).serialize(),
        },
        success: function(response) {
          console.log(response)
          location.href = "/home"
        },
        error: function(error) {
          toastr["error"](error.responseJSON.error)
        }
      });
    break;

    case "lpe":
      $.ajax({
        url: "/api/registration/provider_entity/",
        method: "POST",
        data: {
          csrfmiddlewaretoken: Site.getCookie('csrftoken'),
          data: $(form).serialize(),
        },
        success: function(response) {
          console.log(response)
          location.href = "/home"
        },
        error: function(error) {
          toastr["error"](error.responseJSON.error)
        }
      });
    break;

  }
}

Site.formValidation = function(form) {
  for (var i = 0, element; element = form.elements[i++];) {
    if (element.tagName == "INPUT") {
      if (element.value == "") {
        return false;
      }
    }

    if (element.tagName == "SELECT") {
      if (element.value == "") {
        return false;
      }
      if (element.value == "0") {
        return false;
      }
    }

  }

  return true;

}
