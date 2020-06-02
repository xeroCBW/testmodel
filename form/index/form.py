from django import forms

from .models import *
from django.core.exceptions import  ValidationError

def weight_validate(value):
    if not str(value).isdigit():
        raise ValidationError('请输入正确的重量')

class ProductForm(forms.Form):

    #设置错误信息并设置样式

    name = forms.CharField(max_length=20,
                           label='名字',
                           widget=forms.widgets.TextInput({
                               'class':'c1'
                           }),
                           error_messages={'required':'名字不能为空'}
                           )

    # 使用自定义数据验证
    weight = forms.CharField(max_length=50,label='重量',validators=[weight_validate])
    size  = forms.CharField(max_length=50,label='尺寸')

    choices_list = [(i+1,v['name'])for i,v in enumerate(Type.objects.values('name'))]

    type = forms.ChoiceField(widget=forms.widgets.Select(attrs={
        'class':'type',
        'size':'4'
    }),choices=choices_list,label='产品类型')

# class ProductModelForm(forms.ModelForm):
#
#     def __init__(self,*args,**kwargs):
#         super(ProductModelForm,self).__init__(*args,**kwargs)
#
#         type_obj = Type.objects.values('name')
#         choices_list = [(i + 1, v['name']) for i, v in enumerate(Type.objects.values('name'))]
#         self.fields['type'].choices = choices_list
#         self.fields['name'].initial = '我的手机'
#
#         # 添加模型外的表单字段
#         productId = forms.CharField(max_length=20, label='产品序号', initial='NO1')
#
#         # 模型与表单设置
#         class Meta:
#             # 绑定模型
#             model = Product
#             # fields属性是设置转换字段，'__all__'是将全部模型字段转换成表单字段
#             # fields = '__all__'
#             fields = ['name', 'weight', 'size', 'type']
#             # exclude是禁止模型字段转换表单字段
#             exclude = []
#             # labels设置HTML元素控件的label标签
#             labels = {
#                 'name': '产品名称',
#                 'weight': '重量',
#                 'size': '尺寸',
#                 'type': '产品类型'
#             }
#             # 定义widgets，设置表单字段的CSS样式
#             widgets = {
#                 'name': forms.widgets.TextInput(attrs={'class': 'c1'}),
#             }
#             # 定义字段的类型,一般情况下模型的字段会自动转换成表单字段
#             field_classes = {
#                 'name': forms.CharField
#             }
#             # 帮助提示信息
#             help_texts = {
#                 'name': ''
#             }
#             # 自定义错误信息
#             error_messages = {
#                 # __all__设置全部错误信息
#                 '__all__': {'required': '请输入内容',
#                             'invalid': '请检查输入内容'},
#                 # 设置某个字段错误信息
#                 'weight': {'required': '请输入重量数值',
#                            'invalid': '请检查数值是否正确'}
#             }
#
#
#     def clean_weight(self):
#         data = self.cleaned_data['weight']
#         return data + 'g'