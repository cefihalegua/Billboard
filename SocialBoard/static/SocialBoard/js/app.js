$(document).ready(function () {
    $("#ask_to_add").click(function () {
    $("#newpostform").css("display", "block")
    $("#plus").css("display", "none")
    });

    $("#close").click(function () {
        $("#newpostform").css("display", "none")
        $("#plus").css("display", "flex")
        $("#ask_to_add").css("display", "inline-block")
    })

})