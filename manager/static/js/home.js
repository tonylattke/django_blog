$(document).ready(function(){
	
	$(".delete_post").click(function(e) {
        var conf = confirm("Are you sure?");
        e.preventDefault();
        if(conf) {
        	var post_id = $(this).parent().attr("id");
			var form =$("#form_delete_post");
			
			//Authorized
			appendInfoForm(form,'authorized',true);
			
			//Return page
			appendInfoForm(form,'return_page','home');

			form.submit();
        }
    });

});