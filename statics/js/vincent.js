function SwalConfirm(Callbacks, titles, tit) {
    let Swalconfirmtext = { title: titles === undefined ? "确定删除吗?" : titles, text: "", icon: "question", showCancelButton: !0, confirmButtonColor: "#34c38f", cancelButtonColor: "#f46a6a", confirmButtonText: "确定", cancelButtonText: "取消" };
    Swal.fire(Swalconfirmtext)
        .then((t) => {
            if (t.value) {
                Callbacks();
            }
        }
        )
}
function MyPromise(url, data, method) {
    return new Promise((resolve, reject) => {
        $.ajax({
            type: method == undefined ? "GET" : method,
            url: url,
            data: data,
            success: function (data) {
                resolve(data);
            },
            error: function (error) {
                reject(error);
            }
        });
    })
}

//提示
function msgAlert(msg) {
    $("#msg").show();
    $("#msg_info").html(msg);
}
//成功
function succAlert(msg) {
    $("#suc").show();
    $("#msg_succ").html(msg);
}
//错误
function errAlert(msg) {
    $("#err").show();
    $("#msg_err").html(msg);
}

//警告
function warnAlert(msg) {
    $("#warn").show();
    $("#msg_warn").html(msg);
}

//关闭警告
function warnAlertClose() {
    $("#warn").hide();
    $("#msg_warn").html("");
}

//清空弹窗
function clearAlert() {
    $("#msg").hide();
    $("#err").hide();
    $("#warn").hide();
    $("#suc").hide();
}


//弹窗提示
function msgModelAlert(msg) {
    $(".msgModel").show();
    $(".msgModel_info").html(msg);
}
//弹窗提示
function succModelAlert(msg) {
    $(".succModel").show();
    $(".msgModel_succ").html(msg);
}
//弹窗错误提示
function errModelAlert(msg) {
    $(".errModel").show();
    $(".msgModel_err").html(msg);
}

//弹窗警告提示
function warnModelAlert(msg) {
    $(".warnModel").show();
    $(".msgModel_warn").html(msg);
}

//清空弹窗
function clearModelAlert() {
    $(".msgModel").hide();
    $(".errModel").hide();
    $(".warnModel").hide();
    $(".succModel").hide();
}

//获取Querystring
Request = {
    QueryString: function (item) {
        var svalue = location.search.match(new RegExp("[\?\&]" + item + "=([^\&]*)(\&?)", "i"));
        return svalue ? svalue[1] : svalue;
    }
}

// 时间控件显示
function showLaydate()
{
    lay('#version').html('-v' + laydate.v);
    lay('.select-input').each(function () {
        laydate.render({
            elem: this, //指定元素
            type: 'time',
            format: 'HH:mm',
            range: '至'
        });
    });
    lay('.select-input2').each(function () {
        laydate.render({
            elem: this, //指定元素
            type: 'time',
            format: 'HH:mm',
        });
    });
}
// 时间比较
function time_to_sec(time) {
    if (time !== null) {
        var s = "";
        var hour = time.split(":")[0];
        var min = time.split(":")[1];
        s = Number(hour * 3600) + Number(min * 60);
        return s;
    }
}
