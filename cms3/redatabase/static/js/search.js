$(document).ready(function () {
    var test=$('#info').text();
    $('#searchform').submit(function () {
        var mysearch=$('#query').val();
        mysearch=$.trim(mysearch);
        var myreplace='<span class="hilite"> '+mysearch+'</span>';
        var reg=new RegExp(mysearch,"g");
        test1=test.replace(reg,myreplace);
        $('#info').html(test1);
        mysearch='search:'+mysearch;
        $('#show1').html(mysearch).wrap('<h1></h1>');
        $('#info').hide();
confirmation()
        function confirmation() {
            var answer=confirm(mysearch)
            if(answer){
                alert("OK...waiting....");
                $('#info').show('slow');
            }
            else {
                $('#info').html(test).show('slow');
            }
        }
        return false
    })
})