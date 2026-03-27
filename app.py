import streamlit as st

st.title("Python demo aplikacija")

# unos teksta
tekst = st.text_input("Unesi neki tekst:")

# unos broja
broj = st.number_input("Unesi broj:", step=1)

if st.button("Pokreni program"):

    st.write("### Rezultat")

    # ispis teksta
    st.write("Tekst:", tekst)

    # provera parnosti
    if broj % 2 == 0:
        st.write("Broj je PARAN")
    else:
        st.write("Broj je NEPARAN")

    # ispis brojeva
    st.write("Brojevi do", broj, ":")
    for i in range(1, int(broj) + 1):
        st.write(i)
