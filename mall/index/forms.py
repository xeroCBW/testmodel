from .models import *
from django import forms

class ProductModelForm(forms.ModelForm):

    # productId = forms.CharField(max_length=20,label='产品序号')

    class Meta:
        model = Product
        fields = ['name','weight','size','type']

        labels = {
            'name':'产品名称',
            'weight':'重量',
            'size':'尺寸',
            'type':'产品类型',
        }

        error_messages = {

            '__all__':{
                'required':'请输入内容',
                'invalid':'请检查输入内容',
            }
        }

    def clean_weight(self):
        data = self.cleaned_data['weight']
        return data + 'g'

