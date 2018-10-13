$("#div_digg .action").on("click", function () {
    if ($(".info").attr("username")) {
        // 数据
        var is_up = $(this).hasClass("diggit");
        var article_id = $(".info").attr("article_id");

        $.ajax({
            url: "/blog/up_down/",
            type: "post",
            data: {
                is_up: is_up,
                article_id: article_id,
                csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
            },
            success: function (data) {
                // console.log(data.first_action);
                if (data.status) {   // 赞或灭成功
                    if (is_up) {
                        var digg_count = $("#digg_count").text();
                        digg_count = parseInt(digg_count) + 1;
                        $("#digg_count").text(digg_count);
                    } else {
                        var bury_count = $("#bury_count").text();
                        bury_count = parseInt(bury_count) + 1;
                        $("#bury_count").text(bury_count);
                    }


                } else { // 重复提交
                    if (data.first_action) {
                        $("#digg_tips").html("你已经赞过了");
                    } else {
                        $("#digg_tips").html("你已经踩过了");
                    }

                    // 一段时间后提示自动消失
                    setTimeout(function () {
                        $("#digg_tips").html("");
                    }, 1000);

                }
            }
        })
    } else {
        location.href = "/login/"
    }
});
