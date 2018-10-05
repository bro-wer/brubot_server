function turnOffInputs() {
  setDisabledOnAllInputs(true);
}

function turnOnInputs() {
  setDisabledOnAllInputs(false);
}

function setDisabledOnAllInputs(disabledValue) {
  inputs = document.getElementsByTagName('input');
  for (index = 0; index < inputs.length; ++index) {
    inputs[index].disabled=disabledValue;
  }
}

function findTorrents() {
  console.log("findTorrents");
  turnOffInputs();
  document.getElementById('possibleTorrentsWrapper').style.display="block";
  const torrentName = document.getElementById('torrentNameInput').value;

  $.ajax({
      url : "findTorrents",
      type : "GET",
      data : { torrentName : torrentName},

      // handle a successful response
      success : function(json) {
          $('#post-text').val('');
          console.log("success"); // another sanity check
          document.getElementById('possibleTorrentsTable').innerHTML = json;
      },

      // handle a non-successful response
      error : function(xhr,errmsg,err) {
          $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
              " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
          console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
          document.getElementById('possibleTorrentsTable').innerHTML = '<div class="alert alert-danger" role="alert"> <a href="#" class="alert-link">Failed to find torrents!</a> </div>';
      }
  });


  turnOnInputs();
}
