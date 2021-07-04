function shortenUrl(){
var value = $('.input1').val();
if(value==""){
   return ""
}
$.ajax({
  type: 'POST',
  url: "http://127.0.0.1:5000/get_short_url",
  data: JSON.stringify(value),
  contentType: 'application/json',
  success: function(data){
    document.getElementById("kom").value = data;
    document.getElementById("cbtn").style.display="block";
  }
});
}

