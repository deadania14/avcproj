from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms import Textarea
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin.widgets import AdminTimeWidget, AdminSplitDateTime
from ajax_select.fields import AutoCompleteSelectField, AutoCompleteSelectMultipleField
from ajax_select import make_ajax_field
from .models import Article, Practice, Kelas, PracticeAttendance, Inventory, Meeting, Administrasi, AdministrationType
from public.models import SettingsVariable, Event, UserProfile

class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='Judul',required=True)
    image = forms.ImageField(label = 'Gambar', required=False)
    class Meta:
        model = Article
        fields = ('title','text',
        'image',)

class MainArticleForm(forms.ModelForm):
    image = forms.ImageField(label = 'Gambar', required=False)
    class Meta:
        model = Article
        fields = ('text',
        'image',)

class SchedulesForm(forms.ModelForm):
    date = forms.SplitDateTimeField(label='Tanggal Latihan', required=True, widget=AdminSplitDateTime)
    place = forms.CharField(label='Tempat', required=True)

    class Meta:
        model = Practice
        exclude = ('created_date',)

class NewClassForm(forms.ModelForm):
    nama_kelas = forms.CharField(label='Nama Kelas', max_length=100, required=True)
    note = forms.CharField(label='Deskripsi Kelas', widget=forms.Textarea, required=True)
    class Meta:
        model = Kelas
        exclude = ('updated_date',)
        widget = {
             'note': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

class EditUserClassForm(forms.ModelForm):
    # user_kelas = forms.ModelMultipleChoiceField(
    #     label='Pilih Kelas',
    #     queryset=Kelas.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=False
    # )
    class Meta:
        model = UserProfile
        fields = ('user_kelas',)

class AbsensiForm(forms.ModelForm):
    is_present = forms.ModelMultipleChoiceField(
        label='Daftar Kehadiran',
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    tutor_pendamping = forms.ModelMultipleChoiceField(
        label='Asisten Tutor',
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    class Meta:
        model = PracticeAttendance
        fields = ('is_present', 'tutor_pendamping',)

class AbsensiPeopleForm(forms.ModelForm):
    daftar_orang = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    tutor_pendamping = forms.ModelMultipleChoiceField(
        queryset=User.objects.filter(profile__tipe_user='tutor'),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    class Meta:
        model = PracticeAttendance
        fields = ('daftar_orang','tutor_pendamping')

class AbsensiKelasForm(forms.ModelForm):
    class Meta:
        model = PracticeAttendance
        fields = ('practice','kelas','tutor')

class AVCContactForm(forms.Form):
    address = forms.CharField(label='Alamat',  required=True)
    phone1 = forms.CharField(label='Telepon Utama',  required=True)
    phone2 = forms.CharField(label='Telepon Bantuan', required=True)
    email = forms.EmailField(label='E-mail',  required=True)
    facebook = forms.CharField(label='Facebook',  required=True)
    twitter = forms.CharField(label='Twitter',  required=True)
    instagram = forms.CharField(label='Instagram', required=True)
    youtube = forms.CharField(label='Youtube', required=True)

class NewEventForm(forms.ModelForm):
    event_name = forms.CharField(label='Nama Acara',  required=True)
    desc = forms.CharField(label='Deskripsi', widget=forms.Textarea, required=True)
    image = forms.ImageField(label = 'Gambar', required=False)
    event_date = forms.DateField(
        widget=SelectDateWidget(
            empty_label=("Choose Year", "Choose Month", "Choose Day"),
        )
    )
    class Meta:
        model = Event
        fields = ['event_name', 'desc', 'image', 'event_date',]
        widget = {
             'note': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

class EditEventForm(forms.ModelForm):
    event_name = forms.CharField(label='Nama Acara',  required=True)
    desc = forms.CharField(label='Deskripsi', widget=forms.Textarea, required=True)
    image = forms.ImageField(label = 'Gambar', required=False)
    event_date = forms.DateField(
        widget=SelectDateWidget(
            empty_label=("Choose Year", "Choose Month", "Choose Day"),
        )
    )
    class Meta:
        model = Event
        exclude = ('email','corporate', 'phone', 'created_date','published_date','event_status',)
        widget = {
             'note': Textarea(attrs={'cols': 80, 'rows': 20}),
        }


class NewBarangForm(forms.ModelForm):
    thingsname = forms.CharField(label='Nama Barang', required=True)
    detail = forms.CharField(label='Keterangan', widget=forms.Textarea, required=True)
    note = forms.CharField(label='Catatan', widget=forms.Textarea, required=True)
    class Meta:
        model = Inventory
        exclude = ('created_date','updated_date',)
        widget = {
             'note': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

class EditBarangForm(forms.ModelForm):
    detail = forms.CharField(label='Keterangan', widget=forms.Textarea, required=True)
    note = forms.CharField(label='Catatan', widget=forms.Textarea, required=True)
    class Meta:
        model = Inventory
        exclude = ('thingsname','created_date','updated_date',)
        widget = {
             'note': Textarea(attrs={'cols': 80, 'rows': 20}),
        }


class NewMeetingForm(forms.ModelForm):
    title = forms.CharField(label='Judul', required=True)
    place = forms.CharField(label='Tempat', required=True)
    user = forms.ModelMultipleChoiceField(
        label='Daftar Hadir',
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    note = forms.CharField(label='Catatan', widget=forms.Textarea, required=True)
    date_meet = forms.DateField(
        widget=SelectDateWidget(
            empty_label=("Choose Year", "Choose Month", "Choose Day"),
        )
    )
    class Meta:
        model = Meeting
        exclude = ('created_date', 'updated_date',)
        widget = {
             'note': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

class EditMeetingForm(forms.ModelForm):
    user = forms.ModelMultipleChoiceField(
        label='Daftar Hadir',
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    note = forms.CharField(label='Catatan', required=True)
    place = forms.CharField(label='Tempat', required=True)
    class Meta:
        model = Meeting
        fields = ('place', 'user', 'note',)

class EditUser(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user_kelas',)
    class Meta:
        model = User
        fields = ('is_active',)

class NewPaymentForm(forms.ModelForm):
    class Meta:
        model = Administrasi
        exclude = ['created_date', 'image','nominal',]

class EditPaymentForm(forms.ModelForm):
    class Meta:
        model = Administrasi
        exclude = ['created_date', 'image',]

class NewPaymentTypeForm(forms.ModelForm):
    class Meta:
        model = AdministrationType
        exclude = ['created_date', 'updated_date',]

class EditPaymentTypeForm(forms.ModelForm):
    class Meta:
        model = AdministrationType
        exclude = ['paymentstype', 'created_date', 'updated_date',]
