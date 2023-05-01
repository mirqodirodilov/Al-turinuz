from django.shortcuts import render
from .models import *
from django.views.generic import DetailView



def events_detailView(request,events_id):
	news_detail = IndexNewsPage.objects.filter(id=events_id)
	news_all = IndexNewsPage.objects.all()
	news_details = news_detail[0]
	context = {
		'news_details':news_details,
		'news_all':news_all,
	}
	return render(request,'events-detail.html',context)


def news_detailView(request,news_id):
	model = IndexMiddlePage.objects.filter(id=news_id)
	all_new = IndexMiddlePage.objects.all()
	middle_detail = model[0]
	context = {
		'middle_detail':middle_detail,
		'all_new':all_new,
	}
	return render(request,'news-detail.html',context)

#index
def indexpageview(request):
	page = IndexFirstModel.objects.all()
	middle = IndexMiddlePage.objects.all()
	news_final = IndexNewsPage.objects.all()
	ctx = {
	'page':page,
	'middle':middle,
	'news_final':news_final,
	}
	return render(request,'index.html',ctx)


#about
def aboutpageview(request):
	page = AboutPageModel.objects.all()
	ctx = {
	'page':page,
	}
	return render(request,'about.html',ctx)



#about
def achievementspageview(request):
	aciv = Achivments.objects.all()
	ctx = {
	'aciv':aciv
	}
	return render(request,'achievements.html',ctx)



#contact
def contactpageview(request):
	kontact = Contact.objects.all()
	ctx = {
	'kontact':kontact,
	}
	return render(request,'contact.html',ctx)



# events_detail
def events_detailepageview(request,event_id):
	model = EventsModel.objects.filter(id=event_id)
	events_detail = model[0]
	context = {
		'events_detail':events_detail,
	}
	return render(request,'events-detaile.html',context)


	
#events
def eventspageview(request):
	even = EventsModel.objects.all()
	ctx = {
	'even':even
	}
	return render(request,'events.html',ctx)



#gallery
def gallerypageview(request):
	rasm = GalleryModel.objects.all()
	ctx = {
	'rasm':rasm,
	}
	return render(request,'gallery.html',ctx)



#lesson_table
def lesson_tablepageview(request):
	lessons = Lesson_table.objects.all()
	ctx = {
	'lessons':lessons
	}
	return render(request,'lesson-table.html',ctx)



# mugs
def mugspageview(request):
	mugu = Togaraklar_category.objects.all()
	mugss = Togaraklar.objects.all()
	ctx = {
	'mugu':mugu
	}
	return render(request,'mugs.html',ctx)



#news_detaile
def news_detailepageview(request,newsd_id):
	model = YangliklarModel.objects.filter(id=newsd_id)
	news_detail_all = YangliklarModel.objects.all()
	news_detaila = model[0]
	ctx = {
	'news_detaila':news_detaila,
	'news_detail_all':news_detail_all,
	}
	return render(request,'news-detaile.html',ctx)


# news
def newspageview(request):
	news = YangliklarModel.objects.all()
	ctx = {
	'news':news
	}
	return render(request,'news.html',ctx)



# personal
def personalpageview(request):
	person = Rukavotstva.objects.all()
	teacer = Kafedra.objects.all()
	ctx = {
	'person':person,
	'teacer':teacer
	}
	return render(request,'personal.html',ctx)



# question
def questionpageview(request):
	ques = Question_category.objects.all()
	ctx = {
	'ques':ques
	}
	return render(request,'question.html',ctx)



# reception
def receptionpageview(request):
	recep = Reception.objects.all()
	ctx = {
	'recep':recep
	}
	return render(request,'reception.html',ctx)



# results-reception
def results_receptionpageview(request):
	objet = Result_reception.objects.all()
	ctx = {
	'objet':objet
	}
	return render(request,'results-reception.html',ctx)


# results
def resultspageview(request):
	resultss = Results.objects.all()
	ctx = {
	'resultss':resultss
	}
	return render(request,'results.html',ctx)



class Lesson_table_detailview(DetailView):
	model = Lesson_table
	template_name = "lesson-table-detail.html"



