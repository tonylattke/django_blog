from django.contrib import admin
from django import forms

from website.models import *

''' ******************************* Helpers ******************************* '''
#Form Format
class Text_Form(forms.ModelForm):
	text = forms.CharField( widget=forms.Textarea )

#Inlines
class CommentInline(admin.TabularInline):
	model = Comment
	extra = 0

''' ********************************* Post ******************************** '''
class Post_Admin(admin.ModelAdmin):
	form = Text_Form
	fieldsets 	= [
		('Post name'	,	{'fields': ['name']}),
		('Text'			,	{'fields': ['text']}),
		('Date'			,	{'fields': ['date']}),
	]
	list_display= ('id', 'name', 'date')
	inlines = [CommentInline]

''' ******************************* Comment ******************************* '''
class Comment_Admin(admin.ModelAdmin):
	form = Text_Form
	fieldsets 	= [
		('Post'			,	{'fields': ['post']}),
		('Author name'	,	{'fields': ['name']}),
		('Text'			,	{'fields': ['text']}),
		('Date'			,	{'fields': ['date']}),
	]
	list_display= ('id', 'post_tag', 'name', 'date')


''' *********************************************************************** '''
''' ****************************** Imports ******************************** '''
admin.site.register(Post, Post_Admin)
admin.site.register(Comment, Comment_Admin)