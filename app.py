import streamlit as st

from bbquoteCD.lib import get_quote

quote, author = get_quote()

f"{quote}, {author}"