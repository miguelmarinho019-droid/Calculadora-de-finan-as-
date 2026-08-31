import streamlit as st

# Título do aplicativo na págimport streamlit as st

# Título do aplicativo na página
st.title("📊 Calculadora de Finanças Pessoais")

# Criamos um formulário para agrupar todas as entradas de dados
with st.form("formulario_financas"):
    st.subheader("Entrada de Dados")
    
    # Entradas de dados adaptadas
    nome = st.text_input("Olá, qual é o seu nome?")
    salario = st.number_input("Para começarmos, informe sua faixa salarial (R$):", min_value=0.0, step=100.0, format="%.2f")
    gf = st.number_input("Quantos são seus gastos fixos (ex: luz, água, internet, compras)?", min_value=0.0, step=50.0, format="%.2f")
    gv = st.number_input("Quais são seus gastos variáveis (ex: lazer, roupas, lanches)?", min_value=0.0, step=50.0, format="%.2f")
    
    # Botão para enviar e calcular
    botao_calcular = st.form_submit_button("Calcular Finanças")

# Processamento e Saída (só executa quando clicar no botão)
if botao_calcular:
    if nome.strip() == "":
        st.warning("Por favor, digite seu nome acima para continuar.")
    else:
        # Processamento
        sobra = salario - gf - gv
        
        # Resultados na tela
        st.divider()
        st.subheader(f"Resultado para {nome}:")
        
        if sobra < 0:
            st.error(f"Atenção, {nome}! Suas despesas superam seu salário. No final do mês você fica com um saldo negativo de R$ {sobra:.2f}.")
        else:
            st.success(f"{nome}, subtraindo valores e realizando operações sobre esses gastos, podemos dizer que entre seu salário e contas, no final obtemos o valor de **R$ {sobra:.2f}**.")
            
            # Cálculo dos 20% recomendados para reserva
            reserva = sobra * 0.20
            livre = sobra * 0.80
            
            st.info(f"💡 **Recomendação de Reserva:** É recomendado que 20% deste valor (**R$ {reserva:.2f}**) seja guardado para casos de emergência (essa porcentagem pode variar de acordo com o quanto você pretende guardar).")
            st.write(f"O restante (**R$ {livre:.2f}**) você pode fazer um uso livre, desde que não comprometa seu salário com contas superiores a ele.")