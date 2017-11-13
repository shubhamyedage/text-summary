function trainData() {
var data = {
"data": $("#boxText").val(),
"summary": $("#boxSumm").val()
}
$.ajax({
  url: "/",
  type: "POST",
  contentType:"application/json; charset=utf-8",
  dataType: "json",
  data: JSON.stringify(data),
  success: function(data){
  $("#boxResultText").text(data.summary)
  },
  error: function(data){
  alert("Error");
  }
});
}