$(document).ready(function(){

	$("#create_post").click(function(e) {
        var post_name = $("#post_name").val();
        var post_text = $("#post_text").val();
        if (post_name.length > 0 && 
        	post_text.length > 0) {
	        
	        var conf = confirm("Are you sure?");
	        e.preventDefault();
	        if(conf) {
				var form =$("#form_new_post");
			
				//Authorized
				appendInfoForm(form,'authorized',true);
				
				form.submit();
	        }
	    } else {
	    	alert("The post must have a name and text");
	    }
    });
	 
});