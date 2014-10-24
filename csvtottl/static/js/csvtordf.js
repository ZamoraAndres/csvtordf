var selectedButton = ",";
var headers = false;

$(document).ready(function(){
	if(document.getElementById('upload')){
		document.getElementById("upload").style.visibility = 'hidden';
	}

    $(".btn").first().button("toggle");

    $('body').on('click', '.btn-group button', function (e) {
        $(this).addClass('active');
        $(this).siblings().removeClass('active');
        selectedButton = this.innerHTML;
        //do any other button related things
    });

    $('input').on('ifChecked', function(event){
        headers = true;  
    });
})


function showUpload() {
	document.getElementById("upload").style.visibility = 'visible';
}

function convertAndDownloadFile() {
	/**
    $.fileDownload("/media/output.ttl", {
        preparingMessageHtml: "We are preparing your report, please wait...",
        failMessageHtml: "There was a problem generating your report, please try again."
    });
    return false; //this is critical to stop the click event which will trigger a normal file download! (argument) {
    	*/
    //window.alert("sometext");

    var csrftoken = $.cookie('csrftoken');
    $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        //if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        //}
    }
    });    
    $.ajax({
            csrfmiddlewaretoken: csrftoken,
            type: "POST",
            url: "/csvtottl/convertFile/",
            dataType: "json", 
            data: {"separator": selectedButton,
                    "headers": headers},
            success: function(data) {
                //alert(data["something"]);
                //window.alert("awesome ajax"+JSON.stringify(data));
                window.alert("Your file has been converted");
                window.open("/media/"+data["filename"]+".ttl", '_blank');
            },
            error: function(xhr, textStatus, errorThrown) {
                //alert("Please report this error: "+errorThrown+xhr.status+xhr.responseText);
                window.alert("Your file or settings are invalid, try again");
            }
            });
    
    
    //window.alert("sometext2");
    //$.fileDownload('/media/output.ttl')
    //.done(function () { window.alert("done"); });
}