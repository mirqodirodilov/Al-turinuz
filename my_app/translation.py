from modeltranslation.translator import translator, TranslationOptions
from .models import *



class IndexpagemodelTrans(TranslationOptions):
    fields = ('title', )

class AboutPageModelTrans(TranslationOptions):
    fields = ('text',)

class IndexMiddlePageTrans(TranslationOptions):
    fields = ('user_name','title','description',)


class IndexNewsPageTrans(TranslationOptions):
    fields = ('user_name','title','description',)


class RukavotstvaTrans(TranslationOptions):
    fields = ('lavozm','name',)


# rinkishikemotekeshi


class KafedraTrans(TranslationOptions):
    fields = ('lavozm','name',)


class GalleryModelTrans(TranslationOptions):
    fields = ('text',)

class GalleryImageModelTrans(TranslationOptions):
    fields = ('text',)


class EventsModelTrans(TranslationOptions):
    fields = ('user_name','title','description',)

class YangliklarModelTrans(TranslationOptions):
    fields = ('user_name','title','description',)


class Togaraklar_categoryTrans(TranslationOptions):
    fields = ('fanlar_nomi',)

class AchivmentsTrans(TranslationOptions):
    fields = ('name','achivment')

class TogaraklarTrans(TranslationOptions):
    fields = ('ustoz_f_i_sh','togarak_vaqtlari','togarak_xonasi',)

class Question_categoryTrans(TranslationOptions):
    fields = ('fanlar_nomi',)

class QuestionsTrans(TranslationOptions):
    fields = ('title','author',)

class Result_receptionTrans(TranslationOptions):
    fields = ('text',)

class ReceptionTrans(TranslationOptions):
    fields = ('title','text',)

class ResultsTrans(TranslationOptions):
    fields = ('title',)

class ContactTrans(TranslationOptions):
    fields = ('contact_text',)

translator.register(IndexFirstModel, IndexpagemodelTrans)
translator.register(AboutPageModel, AboutPageModelTrans)
translator.register(IndexMiddlePage, IndexMiddlePageTrans)
translator.register(IndexNewsPage, IndexNewsPageTrans)
translator.register(Rukavotstva, RukavotstvaTrans)
translator.register(Kafedra, KafedraTrans)
translator.register(Achivments, AchivmentsTrans)
translator.register(GalleryModel, GalleryModelTrans)
translator.register(GalleryImageModel, GalleryImageModelTrans)
translator.register(Reception, ReceptionTrans)#######
translator.register(EventsModel, EventsModelTrans)
translator.register(YangliklarModel, YangliklarModelTrans)
translator.register(Togaraklar_category, Togaraklar_categoryTrans)
translator.register(Togaraklar, TogaraklarTrans)
translator.register(Question_category, Question_categoryTrans)
translator.register(Questions, QuestionsTrans)
translator.register(Result_reception, Result_receptionTrans)
translator.register(Results, ResultsTrans)
translator.register(Contact, ContactTrans)