from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

class AboutImageInline(admin.TabularInline):
	"""yana rasm qoshish uchun"""
	model = AboutImageModel
	extra = 0


class AboutAdmin(TranslationAdmin):
	list_display = [field.name for field in AboutPageModel._meta.fields]
	inlines = [AboutImageInline]

	class Meta:
		model = AboutPageModel

admin.site.register(AboutPageModel,AboutAdmin)


class AboutImageAdmin(admin.ModelAdmin):
	list_display = [field.name for field in AboutImageModel._meta.fields]

	class Meta:
		model = AboutImageModel

admin.site.register(AboutImageModel,AboutImageAdmin)



class IndexAdmin(TranslationAdmin):
	list_display = [field.name for field in IndexFirstModel._meta.fields]


	class Meta:
		model = IndexFirstModel
		
admin.site.register(IndexFirstModel,IndexAdmin)



class IndexMiddleAdmin(TranslationAdmin):
	list_display = [field.name for field in IndexMiddlePage._meta.fields]


	class Meta:
		model = IndexMiddlePage
		
admin.site.register(IndexMiddlePage,IndexMiddleAdmin)



class IndexENdAdmin(TranslationAdmin):
	list_display = [field.name for field in IndexNewsPage._meta.fields]


	class Meta:
		model = IndexNewsPage
		
admin.site.register(IndexNewsPage,IndexENdAdmin)




class RukavotstvaAdmin(TranslationAdmin):
	list_display = [field.name for field in Rukavotstva._meta.fields]


	class Meta:
		model = Rukavotstva
		
admin.site.register(Rukavotstva,RukavotstvaAdmin)


class KafedraAdmin(TranslationAdmin):
	list_display = [field.name for field in Kafedra._meta.fields]


	class Meta:
		model = Kafedra
		
admin.site.register(Kafedra,KafedraAdmin)


class AchivementAdmin(TranslationAdmin):
	list_display = [field.name for field in Achivments._meta.fields]


	class Meta:
		model = Achivments
		
admin.site.register(Achivments,AchivementAdmin)



class GalleryImageInline(admin.TabularInline):
	"""yana rasm qoshish uchun"""
	model = GalleryImageModel
	extra = 0


class GalleryAdmin(TranslationAdmin):
	list_display = [field.name for field in GalleryModel._meta.fields]
	inlines = [GalleryImageInline]

	class Meta:
		model = GalleryModel

admin.site.register(GalleryModel,GalleryAdmin)


class GalleryImageAdmin(TranslationAdmin):
	list_display = [field.name for field in GalleryImageModel._meta.fields]

	class Meta:
		model = GalleryImageModel

admin.site.register(GalleryImageModel,GalleryImageAdmin)




class ReceptionAdmin(TranslationAdmin):
	list_display = [field.name for field in Reception._meta.fields]


	class Meta:
		model = Reception
		
admin.site.register(Reception,ReceptionAdmin)


class EventsAdmin(TranslationAdmin):
	list_display = [field.name for field in EventsModel._meta.fields]


	class Meta:
		model = EventsModel
		
admin.site.register(EventsModel,EventsAdmin)


class YangliklarAdmin(TranslationAdmin):
	list_display = [field.name for field in YangliklarModel._meta.fields]


	class Meta:
		model = YangliklarModel
		
admin.site.register(YangliklarModel,YangliklarAdmin)



class Lesson_Table_Admin(admin.ModelAdmin):
	list_display = [field.name for field in Lesson_table._meta.fields]


	class Meta:
		model = Lesson_table
		
admin.site.register(Lesson_table,Lesson_Table_Admin)



class QuestionsAdmin(TranslationAdmin):
	list_display = [field.name for field in Questions._meta.fields]


	class Meta:
		model = Questions
		
admin.site.register(Questions,QuestionsAdmin)


class Question_categoryAdmin(TranslationAdmin):
	list_display = [field.name for field in Question_category._meta.fields]


	class Meta:
		model = Question_category
		
admin.site.register(Question_category,Question_categoryAdmin)

class Result_reception_Admin(TranslationAdmin):
	list_display = [field.name for field in Result_reception._meta.fields]


	class Meta:
		model = Result_reception
		
admin.site.register(Result_reception,Result_reception_Admin)


class ResultsAdmin(TranslationAdmin):
	list_display = [field.name for field in Results._meta.fields]


	class Meta:
		model = Results
		
admin.site.register(Results,ResultsAdmin)


class ContactAdmin(TranslationAdmin):
	list_display = [field.name for field in Contact._meta.fields]


	class Meta:
		model = Contact
		
admin.site.register(Contact,ContactAdmin)

admin.site.register(Togaraklar_category)
admin.site.register(Togaraklar)