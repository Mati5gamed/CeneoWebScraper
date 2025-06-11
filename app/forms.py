from wtforms import Form, StringField, SubmitField, validators
class ProductForm(Form):
        product_id = StringField( "kod Produktu",
                                name = 'product_id',
                                id = 'product_id',
                                validators =[
                                            validators.DataRequired(message= "kod produktu jest wymagany"),
                                            validators.Regexp("^[0-9]"),
                                            validators.length(min=5,max = 10, message = "kod produktu powinien")
                                ])
        
        
        submit = SubmitField("pobierz opinie")