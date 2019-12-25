const dialogue = $('.dialogue');
let nbResponse = 0;

// insert loader icone and hide it
let loading = $('#loading');
let loader = $('<img id="thinking" src="/static/img/engrenages.gif" alt="thinking"/>');
loader.prependTo(loading);
loader.hide();


$(document).ready(function onSubmit(){

  // define keypress enter as a submit when focus on textarea
  $('form').keypress(function(e){
    if(e.which == 13) {
      $('form').submit();
      e.preventDefault();
    }
  });

  // on submit
  $('form').on('submit', function(event){

    // show loader icone
    loader.show();

    // Create question block and insert question in the block
    let questRow = $('<div class="block_question row text-center">');
    let questCol = $('<div class="col-md-7 col-xs-12 alert alert-info"">');
    let questP = $('<p class="user_question">');
    questRow.prependTo(dialogue);
    questCol.appendTo(questRow);
    questP.appendTo(questCol);
    questP.text('Moi : ' + $('#query').val());

    // send user_input to server
    $.ajax({
  		data : {user_input : $('#query').val()},
      type : 'POST',
      url : '/process',
  		})

    //get response from server
    .done(function(data) {

      // Create response block and insert reponse in the block
      let respRow = $('<div class="block_response row text-center">');
      let respCol = $('<div class="col-xs-12 offset-md-5 col-md-7 alert alert-success">');
      let respResult = $('<p class="grandpy_response">');
      respRow.insertAfter(questRow);
      respRow.append(respCol);
      respCol.append(respResult);

      // load response about geolocalisation of the request
      // can be adress or not found answer
      $('.grandpy_response:first').text(data.geoloc);

      if (data.response){
        // Create additionnal response block (map and story) if response == True
        let respMap = $('<div class="map">');
        let respWiki = $('<p class="grandpy_story">');
        respCol.append(respMap);
        respCol.append(respWiki);

        // update number of requests and so number of responses
        nbResponse += 1;
        // Add an id where the map will be
        let divIdMap = 'map' + nbResponse;
        $('.map:first').attr("id", divIdMap);
        // load the map with the google map API
        initMap(data.lat, data.lng, divIdMap);

        // load media wiki datas
        $('.grandpy_story:first').text(data.story);
        reset()
      } else {
        reset()
      };
    });
    // prevent to submit the data twice
    event.preventDefault();
    });
  });

// https://developers.google.com/maps/documentation/javascript/markers
function initMap(lat, lng, id) {
  let myLatLng = {lat: lat, lng: lng};

  let map = new google.maps.Map(document.getElementById(id), {
    zoom: 4,
    center: myLatLng
  });

  let marker = new google.maps.Marker({
    position: myLatLng,
    map: map,
    title: id
  });
}

function reset(){
  // reset form after submission
  $("form").trigger("reset");
  // remove focus from form
  // $('textarea').blur();  // don't work on iphone...
  // scroll up to the top of the section
  let section = $("section");
  let top = section.scrollTop() // Get position
  if(top!=0){
  section.animate({scrollTop:0}, '500');
  }
  // hide loader icone
  loader.hide();
}
