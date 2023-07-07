from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from .models import Items, Product_code

INPUT_CLASSES = 'w-full py-3 px-3 flex justify-between rounded border'
class XYZ_DateInput(forms.DateInput):  
    input_type = "date"
    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        # kwargs["format"] = "%d-%m-%Y"
        super().__init__(**kwargs)
        
# class phone(forms.TextInput):
    
        
class NewItemForm(forms.ModelForm):
    # Contact = PhoneNumberField(
    # #    label=('phone number'),
    #    required=True,
    #    widget=PhoneNumberPrefixWidget(
    #         initial='CN',
    #         attrs={'placeholder': ('Phone number')})),
    class Meta:
        model = Items
        fields = ['id','Patient_name','Vendor','Product_name','Product_code','Issue_date','Rent_start_date', 'Rent_end_date', 'Amount','Technician','Contact','Reference','Address']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['name'].widget.attrs['class'] = 'form-control'
    #     self.fields['description'].widget.attrs['class'] = 'form-control'
    #     self.fields['price'].widget.attrs['class'] = 'form-control'
    #     self.fields['image'].widget.attrs['class'] = 'form-control'
   


        widgets = {
            'Product_name': forms.Select(attrs = {
                'class': INPUT_CLASSES,
            }),
            'Product_code': forms.Select(attrs = {
                'class': INPUT_CLASSES,
            }),
            'Technician': forms.Select(attrs = {
                'class': INPUT_CLASSES,
            }),
            'Issue_date':XYZ_DateInput(format=["%Y-%m-%d"], attrs = {
                'class': INPUT_CLASSES,
            }),
            'Rent_start_date':XYZ_DateInput(format=["%Y-%m-%d"], attrs = {
                'class': INPUT_CLASSES,
            }),
            'Rent_end_date':XYZ_DateInput(format=["%Y-%m-%d"], attrs = {
                'class': INPUT_CLASSES,
            }),  
            'Patient_name': forms.TextInput(attrs = {
                'class': INPUT_CLASSES,
            }),
            'Vendor': forms.TextInput(attrs = {
                'class': INPUT_CLASSES,
            }),
            'Address': forms.Textarea(attrs = {
                'class': INPUT_CLASSES,
            }),
            'Amount': forms.TextInput(attrs = {
                'class': INPUT_CLASSES,
            }),
            'Contact': PhoneNumberPrefixWidget(
            initial='IN',
            attrs={'placeholder': ('Phone number'), 'class':' py-3 px-3  rounded border'}),
            'Reference': forms.TextInput(attrs = {
                'class': INPUT_CLASSES,
            }),
           
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Product_code'].queryset = Product_code.objects.all()

        if 'Product_name' in self.data:
            try:
                Product_name_id = int(self.data.get('Product_name'))
                self.fields['Product_code'].queryset = Product_code.objects.filter(Product_name_id=Product_name_id).order_by('name')
            except (ValueError, TypeError):
                pass 
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['Patient_name', 'Amount', 'is_sold','Vendor','Reference','Address', 'Issue_date','Rent_start_date', 'Rent_end_date', 'Contact']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['name'].widget.attrs['class'] = 'form-control'
    #     self.fields['description'].widget.attrs['class'] = 'form-control'
    #     self.fields['Amount'].widget.attrs['class'] = 'form-control'
    #     self.fields['image'].widget.attrs['class'] = 'form-control'

        widgets = {
            'Patient_name': forms.TextInput(attrs = {
                'class': INPUT_CLASSES,
            }),
            'Issue_date':XYZ_DateInput(format=["%Y-%m-%d"], attrs = {
                'class': INPUT_CLASSES,
            }),
            'Issue_date':XYZ_DateInput(format=["%Y-%m-%d"], attrs = {
                'class': INPUT_CLASSES,
            }),
            'Issue_date':XYZ_DateInput(format=["%Y-%m-%d"], attrs = {
                'class': INPUT_CLASSES,
            }),
            'Contact': forms.TextInput(attrs = {
                'class': INPUT_CLASSES,
            }),
            'Address': forms.Textarea(attrs = {
                'class': INPUT_CLASSES,
            }),
            'Vendor': forms.TextInput(attrs = {
                'class': INPUT_CLASSES,
            }),
            
            'Reference': forms.TextInput(attrs = {
                'class': INPUT_CLASSES,
            }),
          
        }

