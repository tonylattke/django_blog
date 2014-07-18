#Imports from Django
from django.http      				import HttpResponse
from django.shortcuts 				import render
from django.core.mail 				import EmailMessage
from django.shortcuts 				import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth         	import authenticate, login, logout
from django.core.urlresolvers       import reverse

#Imports from Python
from datetime		import datetime

#Imports from User
from website.models	import *

################################### Helpers ###################################
def get_posts(page_number, posts):
	post_per_page = 2
	first = (page_number-1)*post_per_page
	last = first + post_per_page
	return posts[first:last], first, last

def years_posted(posts, len_post):
	years = []
	if len_post > 0:
		newer_year = posts[0].date.year
		older_year = posts[-1].date.year
		years.append(newer_year)
		if not(older_year == newer_year):
			for x in range(older_year, newer_year):
				years.append(x)
	return years

def newInfo(first, current_page):
	newer = False
	if first > 0:
		newer = True
	
	newer_ = current_page - 1
	if newer_ < 0:
		newer_= 1

	return {
			'status': newer,
			'number': newer_,
		}

def oldInfo(last, len_post, current_page):
	older = False
	if last < len_post:
		older = True

	older_ = current_page + 1

	return {
			'status': older,
			'number': older_,
		}

def error_page(msg):
	context = {
		'error_msg'	: msg,
	}
	return render(request, 'error.html', context)

###############################################################################
################################# Log IN & OUT ################################
def login_usr(request, status=True):
	if request.user.is_authenticated():
		return redirect(reverse(index))
	web_file	= 'login.html'
	context = {
		'status': status,
	}
	return render(request, web_file, context)

def login_usr_do(request):
	username = request.POST['username']
	password = request.POST['password']
	user 	 = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return redirect(reverse(index))
	return login_usr(request,False)

@login_required(login_url='/login')
def logout_usr(request):
	logout(request)
	return redirect(reverse(login_usr))

###############################################################################
################################### Home ######################################
def index(request, page=1):
	web_file= 'home.html'
	posts = []
	all_posts = list(Post.objects.all())
	len_post = len(all_posts)
	if page:
		current_page = int(page)
	else:
		current_page = 1
	posts_selected, first, last = get_posts(current_page, all_posts)
	for post in posts_selected:
		aux = {
			'name'	: post.name,
			'id' 	: post.id,
			'text'	: post.text,
			'date'	: post.date
		}
		posts.append(aux)

	context = {
		'posts' 	: posts,
		'newer'		: newInfo(first,current_page),
		'older'		: oldInfo(last,len_post,current_page),
		'years'		: years_posted(all_posts,len_post)
	}
	return render(request, web_file, context)

###############################################################################
################################### Year ######################################
def year(request, year=2014,page=1):
	#validate year
	if int(year) >= 1900:
		web_file= 'year_posts.html'
		posts = []
		all_posts = list(Post.objects.filter(date__year=year))
		len_post = len(all_posts)
		if page:
			current_page = int(page)
		else:
			current_page = 1
		posts_selected, first, last = get_posts(current_page, all_posts)
		for post in posts_selected:
			aux = {
				'name'	: post.name,
				'id' 	: post.id,
				'text'	: post.text,
				'date'	: post.date
			}
			posts.append(aux)

		all_posts = list(Post.objects.all())
		len_post_all = len(all_posts)

		context = {
			'posts' 		: posts,
			'newer'			: newInfo(first,current_page),
			'older'			: oldInfo(last,len_post,current_page),
			'current_year'	: year,
			'years'			: years_posted(all_posts,len_post_all)

		}
		return render(request, web_file, context)
	#Error
	return error_page('Year no accepted')

###############################################################################
################################### Post ######################################
def post(request,post_id):
	web_file	= 'post.html'
	all_posts 	= list(Post.objects.all())
	len_post 	= len(all_posts)
	post_backup = None
	post_id 	= int(post_id)

	for aux in all_posts:
		if post_id == aux.id:
			post = {
				'id'   : aux.id,
				'name' : aux.name,
				'date' : aux.date,
				'text' : aux.text,
			}
			post_backup = aux
			break
	if post_backup:
		comments = Comment.objects.filter(post=post_backup)
		comments_exit = []
		for comment in comments:
			aux = {
				'name' 	: comment.name,
				'date'	: comment.date,
				'text'	: comment.text
			}
			comments_exit.append(aux)
		context = {
			'post' 		: post,
			'comments'	: comments_exit,
			'years'		: years_posted(all_posts,len_post)
		}
		return render(request, web_file, context)
	#Error
	return error_page('invalid post')

################################# Post - New ##################################
@login_required(login_url='/login')
def post_new(request):
	web_file	= 'admin/post_new.html'
	all_posts 	= list(Post.objects.all())
	len_post 	= len(all_posts)
	context = {
		'years'		: years_posted(all_posts,len_post)
	}
	return render(request, web_file, context)

############################### Post - Do New #################################
@login_required(login_url='/login')
def post_new_do(request):
	if request.POST['authorized']:
		post = Post(
				name=request.POST['name'],
				text=request.POST['text'],
				date=datetime.now()
			)
		try:
			post.save()
		except Exception, e:
			pass
		return redirect(reverse(index))
	#Error
	return error_page('No authorized to create post')

################################ Post - Edit ##################################
@login_required(login_url='/login')
def post_edit(request,post_id):
	web_file	= 'admin/post_edit.html'
	all_posts 	= list(Post.objects.all())
	len_post 	= len(all_posts)
	post_id 	= int(post_id)

	for aux in all_posts:
		if post_id == aux.id:
			post = {
				'id'   : aux.id,
				'name' : aux.name,
				'date' : aux.date,
				'text' : aux.text,
			}
			context = {
				'post' 		: post,
				'years'		: years_posted(all_posts,len_post)
			}
			return render(request, web_file, context)

	#Error
	return error_page('Invalid post edit')

############################### Post - Modify #################################
@login_required(login_url='/login')
def post_modify(request,post_id):
	if request.POST['authorized']:
		all_posts 	= list(Post.objects.all())
		len_post 	= len(all_posts)
		post_id 	= int(post_id)

		for aux in all_posts:
			if post_id == aux.id:
				aux.name = request.POST['name']
				aux.text = request.POST['text']
				aux.save()
				return post(request, post_id)
	#Error
	return error_page('Invalid post modify')

############################### Post - Delete #################################
@login_required(login_url='/login')
def post_delete(request,post_id):
	if request.POST['authorized']:
		all_posts 	= list(Post.objects.all())
		post_id 	= int(post_id)

		for aux in all_posts:
			if post_id == aux.id:
				try:
					aux.delete()
				except Exception, e:
					pass
				if request.POST['return_page'] == 'year_posts':
					return redirect('year', year=int(request.POST['current_year']))
				else:
					return redirect(reverse(index))

	#Error
	return error_page('Invalid post delete')

###############################################################################
############################### Make Comment ##################################
def make_comment(request,post_id):
	all_posts = list(Post.objects.all())
	post_id = int(post_id)
	for aux in all_posts:
		if post_id == aux.id:
			post_backup = aux
			break

	if post_backup:
		comment = Comment(
			post = post_backup,
			name = request.POST["comment_name"],
			text = request.POST["comment_text"],
			date = datetime.now()
		)
		try:
			comment.save()
		except Exception, e:
			pass
	
		return redirect('/post/' + str(post_backup.id))
	#Error
	return error_page('Invalid action')

###############################################################################
################################## Testing ####################################
def add_post(request):
	post = Post(
			name = "Lorem ipsum",
			text = """Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
					sed diam nonumy eirmod tempor invidunt ut labore et dolore 
					magna aliquyam erat, sed diam voluptua. At vero eos et 
					accusam et justo duo dolores et ea rebum. Stet clita kasd 
					gubergren, no sea takimata sanctus est Lorem ipsum dolor 
					sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing 
					elitr, sed diam nonumy eirmod tempor invidunt ut labore et 
					dolore magna aliquyam erat, sed diam voluptua. At vero eos 
					et accusam et justo duo dolores et ea rebum. Stet clita 
					kasd gubergren, no sea takimata sanctus est Lorem ipsum 
					dolor sit amet.""",
			date = datetime.now()
		)
	try:
		post.save()
	except Exception, e:
		pass
	return index(request)