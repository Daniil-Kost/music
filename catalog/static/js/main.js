//Code for different parts of application
//------------------------------------

function initEditModalPage(){
  //a - tag <a>, modal-edit-form-link  - class in this tag
  $('a.modal-edit-form-link').click(function(event){
    var link =$(this);
    $.ajax({
      'url': link.attr('href'),
      'dataType': 'html',
      'type': 'get',
      'success': function(data, status, xhr){
        //check if we got successull response from the server
        if (status != 'success'){
          alert(gettext('There was an error on the server. Please try again a bit later.'));
          return false;
        }

        //update modal window with arrived content from the server
        // is id from base.html at tag <div>  in Modal Boilerplate
        var modal = $('#myModal'); 
        var html = $(data);
        // find() -method of search in html code
        var form = html.find('#ajax_form');
        modal.find('.modal-title').html(html.find(
          '#content-column h2').text());
        
        modal.find('.modal-body').html(form);

        //init our edit form
        initEditModalForm(form, modal);

        //setup and show modal window finally
        //Forbids closing the window
        //Disable the background behind the modal window
        modal.modal({
          //'keyboard': false,
          'backdrop': false,
          'show': true});
      },
      'error': function(){
        alert(gettext('There was an error on the server. Please try again a bit later.'));
        return false;
      }
    });

    return false;
  });

}

function initEditModalForm(form, modal){

  //close modal window on Cancel button click
  form.find('button[name="home_button"]').click(function(event){
    modal.modal('hide');
    return false;
  });

  //make form work in AJAX mode from jQuery Form
  form.ajaxForm({
    'dataType': 'html',
    'error': function(){
      alert(gettext('There was an error on the server. Please try again a bit later.'));
      return false;
    },
    'success': function(data, status, xhr){
      var html =$(data);
      var newform =html.find('#content-column form');

      //copy alert to modal window
      modal.find('.modal-body').html(html.find('.alert'));

      //copy form to modal if we found it in server response
      if (newform.length >0){
        modal.find('.modal-body').append(newform);

        //initialize form fields and buttons
        initEditModalForm(newform, modal);
      }else{
        //if no form, it means success and we need to reload page
        //to get updated students list;
        //reload after 2 seconds, so that user can read
        //success message
        setTimeout(function(){location.reload(true);}, 500);
      }
    }
  });
}

function initGenreSelector(){
  // look up select element with genre and attach our even handler
  // on field "change" event
  $('#genre-selector select').change(function(event) {
    //get value of currently selected genre option
    var genre =$(this).val();

    if (genre){
      //set cookie with expiration date 1 year since now;
      //cookie creation function takes period in days
      $.cookie('current_genre', genre, {'path': '/', 'expires': 365});
    }else{
      //otherwise we  delete the cookie
      $.removeCookie('current_genre', {'path': '/'});
    }

    //and reload a page
    location.reload(true);

    return true;

  });
}

$(document).ready(function(){

  initEditModalPage();
  initGenreSelector();

});