import streamlit as st
from PIL import Image
import base64
import pages.Agendamento as pgs




st.set_page_config(
    page_icon=":barber",
    page_title="BarberApp",
)

st.sidebar.title('Menu')
page_cliente = st.sidebar.selectbox('Agendamento', ['Agendamento', 'Credenciamento', 'Gestão de horários'])
    


    
#st.sidebar.success('Selecione  a página ')
col1, col2,col3 = st.columns([1,2,1])

col2.markdown("# :blue[Bem vindo ao BarberApp]:blue[ ]")
col2.markdown("#  ") 

st.video("https://www.youtube.com/watch?v=n77aCvR6D-A")


texto1 = st.text('Espaço de Beleza BarberShop. WhatsApp (77)9.9999-9999')

if page_cliente:
    st.write('Selecione a  página')
    
    
if st.button('Agendamento'):
    Agendamento ={
        'Barber Family': page_cliente,
        
    }
        
    


