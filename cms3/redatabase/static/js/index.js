$(document).ready(function() {
	
		var nd = $("#ndid").val();
		$.ajax({
			type:"GET",
			url:"/CMS/pureElement",
			dataType:"xml",
			data:"MaterNumbers="+nd,
			success:responseResultInfo
		});
		function responseResultInfo(data) {
			var MaterName = $(data).children().find("MaterName").text();
			var Structure = $(data).children().find("Structure").text();
			var Size = $(data).children().find("Size").text();
			var TransPoint = $(data).children().find("Transpoint").text();
			var MeasureTemperature = $(data).children().find("MeasureTemperature").text();
			var Resistivity = $(data).children().find("Resistivity").text();
			var Conductivity = $(data).children().find("Conductivity").text();
			var Cp = $(data).children().find("Cp").text();
			var TEC = $(data).children().find("TEC").text();
			var YModulus = $(data).children().find("YModulus").text();
			var Microhardness = $(data).children().find("Microhardness").text();
			var Remark = $(data).children().find("Remark").text();
			$("#neMaterial").append("<p><font color=red>"+MaterName+"</font></p>");
			$("#neTemperature").append("<p><font color=red>"+MeasureTemperature+"</font></p>");
			$("#neSize").append("<p><font color=red>"+Size+"</font></p>");
			$("#neStructure").append("<p><font color=red>"+Structure+"</font></p>");
			$("#neTransformation").append("<p><font color=red>"+TransPoint+"</font></p>");
			$("#neResistivity").append("<p><font color=red>"+Resistivity+"</font></p>");
			$("#neConductivity").append("<p><font color=red>"+Conductivity+"</font></p>");
			$("#neCapacity").append("<p><font color=red>"+Cp+"</font></p>");
			$("#neTEC").append("<p><font color=red>"+TEC+"</font></p>");
			$("#neElastic").append("<p><font color=red>"+YModulus+"</font></p>");
			$("#neMicrohardness").append("<p><font color=red>"+Microhardness+"</font></p>");
		}
});