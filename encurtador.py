import streamlit as st
import pyshorteners

def main():
    st.title('Encurtador de Link')

    long_url = st.text_input("Insira o Link")

    botao = st.button('Encurtar')
    if botao:
        encurta(long_url)
    


def encurta(long_url):
    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(long_url)

    #print("A URL encurtada é: " + short_url)
    st.write("A URL encurtada é: " + short_url)


if __name__ == '__main__':
    main()    