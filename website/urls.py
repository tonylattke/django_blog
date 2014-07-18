from django.conf.urls import patterns, url

from website import views

urlpatterns = patterns('',
	# home
	url(r'^$'												, views.index),			#/
	url(r'^home$'											, views.index),			#/home
	url(r'^page=(?P<page>[0-9]+)?$' 						, views.index),			#Page

	#Posts in year
	url(r'^year/(?P<year>[0-9]+)?$' 						, views.year,name='year'),			#Year
	url(r'^year/(?P<year>[0-9]+)/page=(?P<page>[0-9]+)?$' 	, views.year,name='year_page' ),	#Year page

	url(r'^post/(?P<post_id>[0-9]+)?$' 						, views.post),			#Post

	url(r'^make_comment/(?P<post_id>[0-9]+)?$' 				, views.make_comment),	#Create comment

	url(r'^add_post$'										, views.add_post),		#Testing create post

	#Log in & out
	url(r'^login$'											, views.login_usr),		#Login
	url(r'^do_login$'										, views.login_usr_do),	#Login do
	url(r'^logout$'											, views.logout_usr),	#Logout

	#Admin
	url(r'^post/new$' 										, views.post_new),		#Post New
	url(r'^post/new_do$' 									, views.post_new_do),	#Post New do
	url(r'^post/edit/(?P<post_id>[0-9]+)?$' 				, views.post_edit),		#Post Edit
	url(r'^post/modify/(?P<post_id>[0-9]+)?$' 				, views.post_modify),	#Post Modify
	url(r'^(.+/)?post/delete/(?P<post_id>[0-9]+)?$' 		, views.post_delete),	#Post Delete
)