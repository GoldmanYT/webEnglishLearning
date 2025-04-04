import streamlit as st
from english_learning import *


def get_column_by_index(index, columns):
    return columns[index // 2]


st.title(TITLE)
st.write(HINT)

if 'word' not in st.session_state:
    st.session_state.word = get_word()
    st.session_state.variants = get_variants(st.session_state.word)

word = st.session_state.word
variants = st.session_state.variants
answer = st.session_state.get('answer')

if answer is None:
    st.warning(word)
elif answer is True:
    st.success(word)
elif answer is False:
    st.error(word)
answer_columns = st.columns(COLUMN_COUNT)

for i, variant in enumerate(variants):
    column = get_column_by_index(i, answer_columns)
    if check_correct(word, variant):
        if column.button(variant, key=i, disabled=answer is not None):
            st.session_state.answer = True
            st.rerun()
    else:
        if column.button(variant, key=i, disabled=answer is not None):
            st.session_state.answer = False
            st.rerun()

if answer is not None:
    label_text = CORRECT if answer else WRONG
    if answer is True:
        st.success(label_text)
    elif answer is False:
        st.error(label_text + words[word])
    if st.button(NEXT, key=-1):
        st.session_state.answer = None
        del st.session_state.word
        st.rerun()
