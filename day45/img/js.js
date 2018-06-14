/**
 * Created by hairui on 2017/2/17.
 */
tp = 0;//全局变量
$(function () {
    var time=setInterval(lb,1000);
    console.log($('#lb a.left'));
    $('#lb').mouseover(function () {
        $('#lb a.left').removeClass('hide').next().removeClass('hide');
       clearInterval(time);
       time=undefined;
       //鼠标单击按钮显示当前图片
        $('span').mouseover(function () {
            tp=$('span').index($(this));
            $(this).addClass('s1').siblings().removeClass('s1');
            $('.tp li').eq(tp).removeClass('hide').siblings().addClass('hide')
        });
    }).mouseleave(function () {
            $('#lb>a').addClass('hide')
            time = setInterval(lb,1000)
            });//去除左右的按钮,出现轮播
});

//轮播设置
function lb() {
        if (tp==7){
            tp=0;
            $('li.potion').eq(tp).fadeIn(1000).siblings().fadeOut(1000);
            $('.tb span').eq(tp).addClass('s1').siblings().removeClass('s1');
        }else {
            $('li.potion').eq(tp).fadeOut(1000).next().fadeIn(1000);
            $('.tb span').eq(tp+1).addClass('s1').siblings().removeClass('s1');
            tp++
        }
};

function qh() {
            $('li.potion').eq(tp).removeClass('hide').siblings().addClass('hide');
            $('.tb span').eq(tp).addClass('s1').siblings().removeClass('s1');
}

$('a.left').click(function () {
        if (tp>0){tp--;}else {tp=7;}
        qh()
        });

$('a.right').click(function () {
        if (tp<7){tp++;}else {tp=0;}
        qh()
        });