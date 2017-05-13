$("thead").find("th").on("click", function() {
      $(this).closest("table").find("tbody").toggle();
    });
$("section").find("span").on("click", function() {
      $(this).closest("section").find("main").toggle();
    });