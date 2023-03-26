from django.db import models


class UserNationality(models.Model):
    DEFAULT_PK = 60

    nationality = models.CharField(max_length=50)

    def __str__(self):
        return self.nationality

    class Meta:
        ordering = ['nationality']


class MainInfoResume(models.Model):
    user_gender = [('Female', 'Женский'), ('Male', 'Мужской')]

    photo = models.ImageField(upload_to='photos/user_id', verbose_name='Фотография', blank=True)
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    middle_name = models.CharField(max_length=50, verbose_name='Отчество', blank=True)
    birthday = models.DateField(verbose_name='Дата рождения')
    gender = models.CharField(max_length=10, choices=user_gender, verbose_name='Пол')
    city = models.CharField(max_length=50, verbose_name='Город проживания')
    email = models.EmailField(max_length=50, verbose_name='Email')
    phone = models.CharField(max_length=13, verbose_name='Телефон')
    nationality = models.ForeignKey('UserNationality', on_delete=models.PROTECT,
                                    default=UserNationality.DEFAULT_PK,
                                    verbose_name='Гражданство')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовать')

# class DesiredPositionResume(models.Model):
#     vacancy = models.CharField(max_length=255)
#     salary = models.IntegerField()
#     work_city = models.CharField(max_length=255)
#     business_trip = models.BooleanField(default=False)
#
#
# class TypeOfEmploymentResume(models.Model):
#     full_time = models.BooleanField(default=False)
#     project_work = models.BooleanField(default=False)
#     internship = models.BooleanField(default=False)
#     part_time = models.BooleanField(default=False)
#     volunteering = models.BooleanField(default=False)
#
#
# class WorkScheduleResume(models.Model):
#     full_time = models.BooleanField(default=False)
#     flexible_schedule = models.BooleanField(default=False)
#     shift_method = models.BooleanField(default=False)
#     shift_schedule = models.BooleanField(default=False)
#     remote_work = models.BooleanField(default=False)
#
#
# class WorkExperienceResume(models.Model):
#     company = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     specialization = models.CharField()
#     site = models.URLField()
#     vacancy = models.CharField(max_length=255)
#     mont_start_work = models.IntegerField()
#     year_star_work = models.IntegerField()
#     month_end_work = models.IntegerField()
#     year_end_work = models.IntegerField()
#     charges = models.TextField()
#
#
# class EducationResume(models.Model):
#     level_of_education = models.CharField()
#     education_institution = models.CharField()
#     faculty = models.CharField()
#     specialization = models.CharField()
#     year_end_education = models.IntegerField()
#
#
# class ProfessionalSkillsResume(models.Model):
#     skill = models.CharField()
#
#
# class AboutUserResume(models.Model):
#     about = models.TextField()
#
#
# class AdvancedTrainingResume(models.Model):
#     education_institution = models.CharField()
#     company = models.CharField()
#     specialization = models.CharField()
#     year_end_education = models.IntegerField()
#
#
# class PortfolioResume(models.Model):
#     portfolio = models.FileField()
#
#
# class CarAndDriversLicense(models.Model):
#     a_category = models.BooleanField(default=False)
#     b_category = models.BooleanField(default=False)
#     c_category = models.BooleanField(default=False)
#     d_category = models.BooleanField(default=False)
#     e_category = models.BooleanField(default=False)
#     be_category = models.BooleanField(default=False)
#     ce_category = models.BooleanField(default=False)
#     de_category = models.BooleanField(default=False)
#     tm_category = models.BooleanField(default=False)
#     tb_category = models.BooleanField(default=False)
#     have_car = models.BooleanField(default=False)
