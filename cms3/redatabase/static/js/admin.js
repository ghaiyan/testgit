$(document).ready(function() {
	
	//点击进入about.html
	$("#about_p").click(function() {
		//alert("hello");
		window.location = "/redatabase/About";
	});
	
	//登陆显示已访问人数
	$.ajax({
		type:"POST",
		url:"/redatabase/total",
		dataType:"xml",
		success:total
	});
	function total(data) {
			var sum = $(data).children().find("sum").text();
		$("#main_counter").append("<font color='red'>"+sum+"</font>");
	}


	$("#login1").click(function() {
		
		var username = $("#username").val();
	var password = $("#password").val();
		if(username == "") {
			$("#username_info").text("");
			$("#username_info").append("<font color='red'>You must enter the username.</font>");
			$("#username").focus();	
		}else {
			$("#username_info").text("");
			
			$.ajax({
				type:"POST",
				url:"/redatabase/check",
				dataType:"xml",
				data:"username="+username+"&password="+password,
				success:responseResultInfo
			});		
		}
		function responseResultInfo(data) {
			var res = $(data).children().find("res").text();
			var admin = $(data).children().find("admin").text();
			if(res == 0) {
				$("#username_info").append("<font color='red'>The username or password you entered does not match our records. Please try again.</font>");
			}
			if(res == 1) {
				$("#username_info").append("<font color='yellow'>Login successfully!</font>");
				window.location = "/redatabase/select";
				
			}
		}
		
	})
	
	//更改密码
	$("#change").click(function() {
		var admin = $("#admin").val();
		var opwd = $("#opwd").val();
		var pwd = $("#pwd").val();
		var pwd2 = $("#pwd2").val();
		if(pwd != pwd2) {
			window.alert("Please Enter Same Password");
			$("#pwd").val("");
			$("#pwd").focus();
			$("#pwd2").val("");
			$("#change_info").text("");
		}else {
				$.ajax({
				type:"POST",
				url:"/redatabase/change",
				dataType:"xml",
				data:"admin="+admin+"&opwd="+opwd+"&pwd="+pwd+"&pwd2="+pwd2,
				success:responsePWD
			});		
			$("#opwd").val("");
			$("#pwd").val("");
			$("#pwd2").val("");	
		}
			function responsePWD(data) {
				var res = $(data).children().find("res").text();
				var res0 = $(data).children().find("res0").text();
				$("#change_info").append("");
				if(res == 1 && res0 == 2) {	
					$("#change_info").text("");
					$("#change_info").append("<font color='red'>Change password successful!</font>");
					window.location="/CMS/main.jsp?admin="+admin;
				}else{		
					$("#change_info").append("<font color='red'>error</font>");
									}
			}
			
			
	});
	//注册信息
	$("#registry").click(function() {
		window.location = "/redatabase/registry";
	})
	$("#login").click(function() {
		window.location = "/redatabase/index/";
	})
})


