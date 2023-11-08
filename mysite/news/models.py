from django.db import models


class News(models.Model): #Створюється клас з полями в базі данних
    title = models.CharField(max_length=150, verbose_name='Назва')#Створюється поле типу рядок
    content = models.TextField(blank=True, verbose_name='Зміст')# великий рядок
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публікації')# Дата і час
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')
    photo = models.ImageField(upload_to='photos/%Y%m%d/', verbose_name='Фото', blank=True)#Фото. Див. також settings як зробити збереження фото
    is_published = models.BooleanField(default=True, verbose_name='Опубліковано')#
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name= 'Назва категорії')#Якщо первинна модель (class Category) об'явлена після, тоді треба вставити її в одинарні лапки '' у вигляді строки. Якщо до - лапки ставити не потрібно

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новина' #Змінює в панелі admin множину і однину
        verbose_name_plural = 'Новини'
        ordering = ['-created_at'] #Сортування за датою створення і редагування


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Назва категорії')# атрибут db_index - індексує поле, робить більш швидшим для пошуку

    class Meta:
        verbose_name = 'Категорія' #Змінює в панелі admin множину і однину
        verbose_name_plural = 'Категорії'
        ordering = ['title'] #Сортування за датою створення і редагування

    def __str__(self):
        return self.title

