function trainData() {
var data = {
"data": $("#trainText").val(),
"summary": $("#sumText").val()
}
$.ajax({
  url: "/",
  type: "POST",
  contentType:"application/json; charset=utf-8",
  dataType: "json",
  data: JSON.stringify(data),
  success: function(data){
  $("#outDiv #outText").text(data)
  },
  error: function(data){
  alert("Error");
  }
});
}