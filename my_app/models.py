from django.db import models



class IndexFirstModel(models.Model):
	title = models.CharField(max_length=255,blank=True,null=True)
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return "%s" % self.title


	class Meta:
		verbose_name = "Bosh sahifa"
		verbose_name_plural = 'Bosh sahifalar'

class AboutPageModel(models.Model):
	text = models.TextField()
	
	def __str__(self):
		return "%s" % self.text

	class Meta:
		verbose_name = "malumot"
		verbose_name_plural = 'malumotlar'


class AboutImageModel(models.Model):
	images = models.ForeignKey(AboutPageModel,blank=True,null=True,on_delete=models.CASCADE)
	image = models.ImageField(upload_to='images/')


class IndexMiddlePage(models.Model):
	user_name = models.CharField(max_length=25)
	title = models.CharField(max_length=255,blank=True,null=True)
	description = models.TextField(blank=True,null=True)
	image = models.ImageField(upload_to='images/')
	date = models.DateField(auto_now=True)
	views = models.CharField(max_length=25)


	def __str__(self):
		return "%s" % self.user_name



class IndexNewsPage(models.Model):
	user_name = models.CharField(max_length=25)
	title = models.CharField(max_length=255,blank=True,null=True)
	description = models.TextField(blank=True,null=True)
	image = models.ImageField(upload_to='images/')
	date = models.DateField(auto_now=True)
	views = models.CharField(max_length=25)


	def __str__(self):
		return "%s" % self.user_name


class Rukavotstva(models.Model):
	lavozm = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return "%s" % self.name

	class Meta:
		verbose_name = "Руководство"
		verbose_name_plural = 'Руководство'


class Kafedra(models.Model):
	lavozm = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return "%s" % self.name

	class Meta:
		verbose_name = "Руководители кафедра"
		verbose_name_plural = 'Руководители кафедра'



class Achivments(models.Model):
	name = models.CharField(max_length=50)
	achivment = models.CharField(max_length=50)
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return "%s" % self.name

	class Meta:
		verbose_name = "Достижения"
		verbose_name_plural = 'Достижения'




class GalleryModel(models.Model):
	text = models.CharField(max_length=125,blank=True,null=True)
	video = models.FileField(upload_to ="video/%y",blank=True)

	def __str__(self):
		return "%s" % self.text

	class Meta:
		verbose_name = "Фотогалерея"
		verbose_name_plural = 'Фотогалерея'


class GalleryImageModel(models.Model):
	images = models.ForeignKey(GalleryModel,blank=True,null=True,on_delete=models.CASCADE)
	image = models.ImageField(upload_to='images/')
	text = models.CharField(max_length=50,blank=True,null=True)


class Reception(models.Model):
	title = models.CharField(max_length=50,blank=True,null=False)
	image = models.ImageField(upload_to='images/')
	text = models.TextField()

	def __str__(self):
		return "%s" % self.title

	class Meta:
		verbose_name = "ПРИЕМ В АКАДЕМИЧЕСКИЙ ЛИЦЕЙ"
		verbose_name_plural = 'ПРИЕМ В АКАДЕМИЧЕСКИЙ ЛИЦЕЙ'



class EventsModel(models.Model):
	user_name = models.CharField(max_length=25)
	title = models.CharField(max_length=255,blank=True,null=True)
	description = models.TextField(blank=True,null=True)
	image = models.ImageField(upload_to='images/')
	date = models.DateField(auto_now=True)
	views = models.CharField(max_length=25)

	def __str__(self):
		return "%s" % self.user_name

	class Meta:
		verbose_name = "Cобытия"
		verbose_name_plural = 'Cобытия'



class YangliklarModel(models.Model):
	user_name = models.CharField(max_length=25)
	title = models.CharField(max_length=255,blank=True,null=True)
	description = models.TextField(blank=True,null=True)
	image = models.ImageField(upload_to='images/')
	date = models.DateField(auto_now=True)
	views = models.CharField(max_length=25)


	def __str__(self):
		return "%s" % self.user_name


	class Meta:
		verbose_name = "Объявления"
		verbose_name_plural = 'Объявления'


class Lesson_table(models.Model):
	group = models.CharField(max_length=255)
	year = models.CharField(max_length=255)
	image = models.ImageField(upload_to='images/')


	def __str__(self):
		return "%s" % self.group

	class Meta:
		verbose_name = "Расписание занятий"
		verbose_name_plural = 'Расписание занятий'


class Togaraklar_category(models.Model):
	fanlar_nomi = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "%s" % self.fanlar_nomi

	class Meta:
		verbose_name = "круги"
		verbose_name_plural = 'круги'


class Togaraklar(models.Model):
	id_raqami = models.CharField(max_length=255)
	ustoz_f_i_sh = models.CharField(max_length=255)
	togarak_vaqtlari = models.CharField(max_length=255)
	togarak_xonasi = models.CharField(max_length=255)
	category = models.ForeignKey(Togaraklar_category,blank=False, null=True, related_name="togaraklar", on_delete=models.SET_NULL)
	created_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "%s" % self.ustoz_f_i_sh

	class Meta:
		verbose_name = "учителя кружка"
		verbose_name_plural = 'учителя кружка'



class Question_category(models.Model):
	fanlar_nomi = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "%s" % self.fanlar_nomi

	class Meta:
		verbose_name = "Задания category"
		verbose_name_plural = 'Задания category'

class Questions(models.Model):
	title = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now=True)
	author = models.CharField(max_length=255)
	files = models.FileField(upload_to='files/')
	category = models.ForeignKey(Question_category,blank=False, null=True, related_name="question", on_delete=models.SET_NULL)

	def __str__(self):
		return "%s" % self.title


	class Meta:
		verbose_name = "Задания teachers"
		verbose_name_plural = 'Задания teachers'



class Result_reception(models.Model):
	text = models.CharField(max_length=50,blank=True,null=True)
	upload = models.FileField(upload_to ='files/')

	def __str__(self):
		return "%s" % self.id

	class Meta:
		verbose_name = "РЕЗУЛЬТАТЫ ПРИЕМА"
		verbose_name_plural = 'РЕЗУЛЬТАТЫ ПРИЕМА'


class Results(models.Model):
	title = models.CharField(max_length=50,blank=True,null=True)
	upload = models.FileField(upload_to ='files/')


	def __str__(self):
		return "%s" % self.title

	class Meta:
		verbose_name = 'Результаты временного контроля'
		verbose_name_plural = 'Результаты временного контроля'


class Contact(models.Model):
	contact_text = models.TextField(blank=True,null=False)

	def __str__(self):
		return "%s" % self.contact_text

	class Meta:
		verbose_name = 'Контакт'
		verbose_name_plural = 'Контакт'