from django import forms

CHOICES = [
    ("AAPL","AAPL"), ("ABBV","ABBV"), ("ABT","ABT"), ("ACN","ACN"), ("ADBE","ADBE"), ("AIG","AIG"), ("AMD","AMD"), ("AMGN","AMGN"), ("AMT","AMT"), ("AMZN","AMZN"), ("AVGO","AVGO"), ("AXP","AXP"), ("BA","BA"), ("BAC","BAC"), ("BK","BK"), ("BKNG","BKNG"), ("BLK","BLK"), ("C","C"), ("CAT","CAT"), ("CHTR","CHTR"), ("CL","CL"), ("CMCSA","CMCSA"), ("COF","COF"), ("COP","COP"), ("COST","COST"), ("CRM","CRM"), ("CSCO","CSCO"), ("CVS","CVS"), ("CVX","CVX"), ("DHR","DHR"), ("DIS","DIS"), ("DOW","DOW"), ("DUK","DUK"), ("EMR","EMR"), ("EXC","EXC"), ("F","F"), ("FDX","FDX"), ("GD","GD"), ("GE","GE"), ("GILD","GILD"), ("GM","GM"), ("GOOG","GOOG"), ("GOOGL","GOOGL"), ("GS","GS"), ("HD","HD"), ("HON","HON"), ("IBM","IBM"), ("INTC","INTC"), ("JNJ","JNJ"), ("JPM","JPM"), ("KHC","KHC"), ("KO","KO"), ("LIN","LIN"), ("LLY","LLY"), ("LMT","LMT"), ("LOW","LOW"), ("MA","MA"), ("MCD","MCD")
]

class indexForm(forms.Form):
    article = forms.CharField(widget=forms.Textarea)
    date = forms.DateField()
    symbol = forms.CharField(widget=forms.Select(choices=CHOICES))