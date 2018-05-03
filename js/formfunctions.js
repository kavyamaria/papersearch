function mysubmit(){
  var query = document.getElementById("querysearch").value;
  var e = document.getElementById("topic");
  var topic = e.options[e.selectedIndex].text;
  alert(topic)

  function go(){
    $.ajax({
      type:"GET",
      url: "../runquery.py",
      dataType:json, //if you want json
          success: function(data) {
           alert(data)
          },
          error: function(request, status, error) {
            alert(data)
          }
    })
  }



}
