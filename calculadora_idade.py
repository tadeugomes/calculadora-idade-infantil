import streamlit as st

def calculate_future_age(current_age, current_year, target_year):
    """Calcula a idade futura com base no ano atual e no ano alvo."""
    age_difference = target_year - current_year
    future_age = current_age + age_difference
    return future_age

# Interface do Streamlit
st.title("Calculadora de Idade para Crianças Curiosas")

# Entrada de dados pelo usuário
current_age = st.number_input("Qual é sua idade atual?", min_value=0, max_value=150, value=6, step=1)
current_year = st.number_input("Em que ano estamos?", min_value=1900, max_value=2100, value=2024, step=1)
target_year = st.number_input("Para qual ano você quer saber sua idade?", min_value=1900, max_value=2100, value=2030, step=1)

# Verificar inputs válidos
if target_year < current_year:
    st.error("O ano futuro deve ser maior ou igual ao ano atual.")
else:
    # Cálculo da idade no ano futuro
    future_age = calculate_future_age(current_age, current_year, target_year)
    st.success(f"No ano {target_year}, você terá {future_age} anos!")

# Adicionar uma imagem local
st.image("desenho.jpg", caption="Arte do Edu",  use_container_width =True)