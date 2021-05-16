from num2words import num2words
import streamlit as st
from annotated_text import annotated_text
import pandas as pd
from babel.numbers import format_currency


st.set_page_config(page_title= "Deposit Information", layout='wide', initial_sidebar_state='collapsed')
st.title("Deposit Information")
st.header("Deposit Slip Information Filling System")


denominations=[2000,500,200,100,50,20,10]

# Dividing things in two columns
left_column_1, right_column_1 = st.beta_columns(2)


def number_of_notes():
    """
    Function for input of Number of Denomination.
    """
    number_of_notes=[]
    
    with left_column_1:
        st.text("Currency Notes Details")
        with st.form(key='my_form'):
            st.text("Enter number of Cash notes of:")
            for denomination in denominations:
                deno = st.number_input("Denomination of {}:".format(denomination), 0)
                number_of_notes.append(deno)
            submit_button = st.form_submit_button(label='Submit')

    return number_of_notes

amount_list= []
def amount(number_of_notes,denominations=denominations):
    """
    Function to calculate the total amount.
    """
    sum=0
    with right_column_1:
        st.text("Amount Details Details")
        
        for cashnotes, deno in zip(number_of_notes, denominations):
            
            amt=deno*cashnotes
            amount_list.append(amt)
            sum+=amt

    return sum


#Calling both the functions
number_of_notes=number_of_notes()
sum=amount(number_of_notes)

# Right column
with right_column_1:
    df = pd.DataFrame(list(zip(number_of_notes, denominations,amount_list)),columns=["Number of Notes", "Denomination", "Amount"])
    df.index = [""] * len(df)
    st.table(df)
    st.header("Amount is "+ str(format_currency(sum, 'INR', locale='en_IN')))
    str ="Amount in word is: "+num2words(str(sum), to="currency", lang="en_IN",currency='INR').title()
    annotated_text((str,"","#faa"))

#Footer HTML
footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}
a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://github.com/sanskarvijpuria" target="_blank">Sanskar Vijpuria</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
