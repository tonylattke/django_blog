$(document).ready(function(){
	
	$(".delete_post").click(function(e) {
        var conf = confirm("Are you sure?");
        e.preventDefault();
        if(conf) {
        	var post_id = $(this).parent().attr("id");
			var form =$("#form_delete_post");
			
			//Authorized
			appendInfoForm(form,'authorized',true);

			//Current year
			appendInfoForm(form,'current_year',current_year);

			//Return page
			appendInfoForm(form,'return_page','year_posts');
			
			form.submit();
        }
    });

});