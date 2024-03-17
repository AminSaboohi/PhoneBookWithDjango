from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()


class MyBaseModel(models.Model):
    is_active = models.BooleanField(
        default=True,
        verbose_name='Is active'
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created date'
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated date'
    )

    class Meta:
        abstract = True
        ordering = ('pk',)

    def __str__(self):
        raise NotImplementedError('Implement __str__ method')


class Province(MyBaseModel):
    name = models.CharField(max_length=250,
                            blank=False,
                            null=False,
                            verbose_name="Name",
                            )

    @property
    def get_cities(self):
        return self.citiss.filter().values(
            'id',
            'title',
            'description',
            'created_date',
            'updated_date',
        )

    class Meta:
        verbose_name = "Province"
        verbose_name_plural = "Provinces"

    def __str__(self):
        return self.name


class City(MyBaseModel):
    province = models.ForeignKey(Province,
                                 related_name='cities',
                                 on_delete=models.PROTECT,
                                 verbose_name="Province",
                                 )
    name = models.CharField(max_length=250,
                            blank=False,
                            null=False,
                            verbose_name="Name",
                            )

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return f'{self.name}({self.province.name})'


class Person(MyBaseModel):
    city = models.ForeignKey(City,
                             related_name='persons',
                             on_delete=models.PROTECT,
                             verbose_name="City",
                             )
    first_name = models.CharField(max_length=255,
                                  null=False,
                                  verbose_name='First name',
                                  )
    last_name = models.CharField(max_length=255,
                                 null=False,
                                 verbose_name='Last name',
                                 )

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"

    def __str__(self):
        return f'{self.first_name} {self.last_name}({self.city.name})'


class PhoneBookRow(MyBaseModel):
    person = models.ForeignKey(Person,
                               related_name='phone_book_rows',
                               on_delete=models.PROTECT,
                               verbose_name="Person",
                               )
    phone_number = models.CharField(max_length=11,
                                    null=False,
                                    verbose_name='Phone number',
                                    )

    author = models.ForeignKey(User,
                               related_name='phone_book_rows',
                               on_delete=models.PROTECT,
                               verbose_name="Author",
                               )

    class Meta:
        verbose_name = "PhoneBookRow"
        verbose_name_plural = "PhoneBookRows"

    def __str__(self):
        return (f'{self.phone_number} '
                f'({self.person.__str__()}) '
                f'created by {self.author.name}')
