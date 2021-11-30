from django import forms
from django.core.mail import EmailMessage, message
from django.forms import fields

from accounts.models import CustomUser
from .models import Taro
# from phonenumber_field.modelfields import PhoneNumberField
# from .models import taro

class InquiryForm(forms.Form):
    name = forms.CharField(label='お名前',max_length=30)
    email = forms.EmailField(label='メールアドレス')
    phone = forms.CharField(label='電話番号',max_length=15)
    message = forms.CharField(max_length=500,label='メッセージ',widget=forms.Textarea)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['class']='form-control col-9'
        self.fields['name'].widget.attrs['placeholder']='お名前をここに入力してください。'

        self.fields['email'].widget.attrs['class']='form-control col-11'
        self.fields['email'].widget.attrs['placeholder']='メールをここに入力してください。'

        self.fields['phone'].widget.attrs['class']='form-control col-11'
        self.fields['phone'].widget.attrs['placeholder']='電話番号をここに入力してください。'

        self.fields['message'].widget.attrs['class']='form-control col-12'
        self.fields['message'].widget.attrs['placeholder']='メッセージをここに入力してください。'

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        phone = self.cleaned_data['phone']
        message = self.cleaned_data['message']

        subject = 'お問い合わせ'
        message = '送信署名:{0}\nメールアドレス：{1}\n電話番号\n{2}メッセージ\n{3}'.format(name,email,phone,message)
        from_email ='admin@example.com'
        to_list = ['test@example.com']
        cc_list = [email]

        message = EmailMessage(subject=subject,body=message,
        from_email=from_email,to=to_list,cc=cc_list)
        message.send()

class InquiryForm1(forms.Form):
    name = forms.CharField(label='お名前',max_length=30)
    email = forms.EmailField(label='メールアドレス')
    phone = forms.CharField(label='電話番号',max_length=15)
    tag = forms.CharField(max_length=15,label='タグ',widget=forms.Textarea)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['class']='form-control col-9'
        self.fields['name'].widget.attrs['placeholder']='お名前をここに入力してください。'

        self.fields['email'].widget.attrs['class']='form-control col-11'
        self.fields['email'].widget.attrs['placeholder']='メールをここに入力してください。'

        self.fields['phone'].widget.attrs['class']='form-control col-11'
        self.fields['phone'].widget.attrs['placeholder']='電話番号をここに入力してください。'

        self.fields['tag'].widget.attrs['class']='form-control col-12'
        self.fields['tag'].widget.attrs['placeholder']='追加してほしいタグを箇条書きで入力して下さい'

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        phone = self.cleaned_data['phone']
        tag = self.cleaned_data['tag']

        subject = 'タグ追加依頼'
        message = '送信署名:{0}\nメールアドレス：{1}\n電話番号\n{2}タグ\n{3}'.format(name,email,phone,tag)
        from_email ='admin@example.com'
        to_list = ['test@example.com']
        cc_list = [email]

        message = EmailMessage(subject=subject,body=message,
        from_email=from_email,to=to_list,cc=cc_list)
        message.send()


class InquiryForm2(forms.Form):
    name = forms.CharField(label='お名前',max_length=30)
    email = forms.EmailField(label='メールアドレス')
    phone = forms.CharField(label='電話番号',max_length=15)
    reason = forms.CharField(max_length=500,label='理由',widget=forms.Textarea)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['class']='form-control col-9'
        self.fields['name'].widget.attrs['placeholder']='お名前をここに入力してください。'

        self.fields['email'].widget.attrs['class']='form-control col-11'
        self.fields['email'].widget.attrs['placeholder']='メールをここに入力してください。'

        self.fields['phone'].widget.attrs['class']='form-control col-11'
        self.fields['phone'].widget.attrs['placeholder']='電話番号をここに入力してください。'

        self.fields['reason'].widget.attrs['class']='form-control col-12'
        self.fields['reason'].widget.attrs['placeholder']='追加してほしいタグを箇条書きで入力して下さい'

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        phone = self.cleaned_data['phone']
        reason = self.cleaned_data['reason']

        subject = 'タグ追加依頼'
        message = '送信署名:{0}\nメールアドレス：{1}\n電話番号\n{2}reason\n{3}'.format(name,email,phone,reason)
        from_email ='admin@example.com'
        to_list = ['test@example.com']
        cc_list = [email]

        message = EmailMessage(subject=subject,body=message,
        from_email=from_email,to=to_list,cc=cc_list)
        message.send()

class UserInfoCreateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (  'first_name',
                    'last_name',
                    'email',
                    'age',
                    'sex',
                    'image',)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class TaroCreateForm(forms.ModelForm):
    class Meta:
        model = Taro
        fields = (  'areaname',
                    'eki',
                    'kenmei',
                    'okane',
                    'tag',
                    'naiyou',
                    'photo1',
                    'photo2',
                    'photo3',)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'      