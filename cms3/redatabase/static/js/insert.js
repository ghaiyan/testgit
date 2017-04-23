/**
 * Created by haiyan on 2017/4/18.
 */
/**
 * Created by haiyan on 2017/4/18.
 */
$(document).ready(function () {
    $("#insert").click(function () {
      alert('插入数据成功')
    })

    $(':input').dblclick(function () {
        if ($(this).val()==''){
            $('#Formula').html('please enter '+$(this).attr('name'));
        }
    })

    $('#insertform').submit(function () {
        var a=new Array();
        var fname=new Array();
        $('#insertform:input[type=text]').each(function (e) {
        fname=this.name;
        a[e]=fname+':'+$(this).val();
            var myfinal=a;
            alert(myfinal);
    })
    })

})